from ultralytics import YOLO
import os
import cv2
import numpy as np
import uuid
from django.conf import settings

def grade_guava(image_path):
    print(f"Starting guava grading for: {image_path}")
    
    # Load segmentation model (orange model for segmentation)
    seg_model_path = os.path.join(settings.BASE_DIR, 'assets', 'models', 'orange_seg.pt')
    print(f"🔧 Segmentation model path: {seg_model_path}")
    print(f"🔧 Model exists: {os.path.exists(seg_model_path)}")
    
    seg_model = YOLO(seg_model_path)
    
    # Perform segmentation prediction
    results = seg_model.predict(source=image_path, conf=0.25)
    result = results[0]
    
    output = {"predictions": []}
    
    # Check if any masks are detected
    if result.masks is not None:
        print("✅ Mask detected in image")
        
        # Get the coordinates of the first detected mask
        coordinates = result.masks.xy[0]
        coordinates = np.array(coordinates, dtype=np.int32)
        
        # Get original image dimensions
        (height, width) = result.orig_shape
        
        # Create a mask for the segmented area
        mask = np.zeros((height, width), dtype=np.uint8)
        cv2.fillPoly(mask, [coordinates], 255)
        
        # Apply the mask to the original image
        original_image = cv2.imread(image_path)
        segmented_image = cv2.bitwise_and(original_image, original_image, mask=mask)
        
        # Create a white background
        white_bg = np.ones_like(original_image) * 0
        # Combine the segmented image with white background
        result_image = np.where(segmented_image == 0, white_bg, segmented_image)
        
        # Ensure segmented_images directory exists
        segmented_images_dir = os.path.join(settings.MEDIA_ROOT, 'segmented_images')
        os.makedirs(segmented_images_dir, exist_ok=True)
        
        # Generate unique filename for segmented image
        segmented_filename = f"segmented_guava_{uuid.uuid4().hex[:8]}.jpg"
        segmented_image_path = os.path.join(segmented_images_dir, segmented_filename)
        
        print(f"Saving segmented image to: {segmented_image_path}")
        
        # Save the segmented image
        success = cv2.imwrite(segmented_image_path, result_image)
        print(f"Segmented image save successful: {success}")
        
        # Store the URL path for UI display
        output["segmented_image_url"] = f"segmented_images/{segmented_filename}"
        
        # Load GUAVA classification model
        cls_model_path = os.path.join(settings.BASE_DIR, 'assets', 'models', 'guava.pt')
        print(f"🔧 Guava classification model path: {cls_model_path}")
        print(f"🔧 Model exists: {os.path.exists(cls_model_path)}")
        
        guava_model = YOLO(cls_model_path)
        
        # Perform classification on the segmented image using GUAVA model
        classification_results = guava_model.predict(source=segmented_image_path)
        
        # Process classification results to match your original guava structure
        result_obj = classification_results[0]
        
        # Process results with index shifting logic
        if hasattr(result_obj, 'names') and result_obj.names:
            output["available_classes"] = result_obj.names
            
        if hasattr(result_obj, 'probs') and result_obj.probs:
            # Get top1 index and confidence
            top1_index = result_obj.probs.top1
            top1_conf = result_obj.probs.top1conf.item()
            
            # Shift index by +1 (as in your original code)
            shifted_index = top1_index + 1
            
            # Handle out-of-range safely
            if shifted_index >= len(result_obj.names):
                shifted_index = len(result_obj.names) - 1
                
            top1_class = result_obj.names[shifted_index]
            
            print(f"Guava classification result: {top1_class} (confidence: {top1_conf})")
            
            output["top_prediction"] = {
                "class": top1_class,
                "confidence": top1_conf
            }
            
            # Get top 5 predictions also shifted by +1
            top5_indices = result_obj.probs.top5
            top5_confs = result_obj.probs.top5conf
            output["top5_predictions"] = []
            
            for i, (idx, conf) in enumerate(zip(top5_indices, top5_confs)):
                # Shift index by +1
                shifted_idx = idx + 1
                if shifted_idx >= len(result_obj.names):
                    shifted_idx = len(result_obj.names) - 1
                    
                output["top5_predictions"].append({
                    "rank": i+1,
                    "class": result_obj.names[idx],
                    "confidence": conf.item()
                })
        
        else:
            # Fallback to object detection if classification not available
            if hasattr(result_obj, 'boxes') and result_obj.boxes is not None and len(result_obj.boxes) > 0:
                # Get the class index of the first detected object
                class_idx = int(result_obj.boxes.cls[0])
                confidence = float(result_obj.boxes.conf[0])
                
                # Shift index by +1
                shifted_index = class_idx + 1
                if shifted_index >= len(result_obj.names):
                    shifted_index = len(result_obj.names) - 1
                    
                fruit_name = result_obj.names[shifted_index]
                
                print(f"Guava detection result: {fruit_name} (confidence: {confidence})")
                
                output["top_prediction"] = {
                    "class": fruit_name,
                    "confidence": confidence
                }
                
                # Get top 5 detections (or all if less than 5)
                all_detections = []
                for i in range(min(5, len(result_obj.boxes))):
                    class_idx = int(result_obj.boxes.cls[i])
                    confidence = float(result_obj.boxes.conf[i])
                    
                    # Shift index by +1
                    shifted_index = class_idx + 1
                    if shifted_index >= len(result_obj.names):
                        shifted_index = len(result_obj.names) - 1
                    
                    fruit_name = result_obj.names[shifted_index]
                    
                    all_detections.append({
                        "rank": i+1,
                        "class": fruit_name,
                        "confidence": confidence
                    })
                
                output["top5_predictions"] = all_detections
            else:
                output["error"] = "No guavas detected in the segmented image"
        
    else:
        print(" No masks detected in the image")
        output["error"] = "No fruits detected for segmentation"
    
    print(f"Returning output: {output}")
    return output