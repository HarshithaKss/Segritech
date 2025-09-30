import cv2
import numpy as np
from ultralytics import YOLO
import os
import uuid
from django.conf import settings

def grade_pomegranate(image_path):
    print(f"Starting pomegranate grading for: {image_path}")
    
    # Load segmentation model
    seg_model_path = os.path.join(settings.BASE_DIR, 'assets', 'models', 'pomegranate_yolov8m-seg.pt')
    print(f" Segmentation model path: {seg_model_path}")
    print(f" Model exists: {os.path.exists(seg_model_path)}")
    
    seg_model = YOLO(seg_model_path)
    
    # Perform prediction
    results = seg_model.predict(source=image_path, conf=0.25)
    result = results[0]
    
    output = {"predictions": []}
    
    # Check if any masks are detected
    if result.masks is not None:
        print(" Mask detected in image")
        
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
        
        # Create a white background (changed to 255 for white instead of 0 for black)
        white_bg = np.ones_like(original_image) * 0
        # Combine the segmented image with white background
        result_image = np.where(segmented_image == 0, white_bg, segmented_image)
        
        # Ensure segmented_images directory exists
        segmented_images_dir = os.path.join(settings.MEDIA_ROOT, 'segmented_images')
        os.makedirs(segmented_images_dir, exist_ok=True)
        
        # Generate unique filename for segmented image
        segmented_filename = f"segmented_pomegranate_{uuid.uuid4().hex[:8]}.jpg"
        segmented_image_path = os.path.join(segmented_images_dir, segmented_filename)
        
        print(f"Saving segmented image to: {segmented_image_path}")
        
        # Save the segmented image
        success = cv2.imwrite(segmented_image_path, result_image)
        print(f"Segmented image save successful: {success}")
        print(f"Segmented image exists: {os.path.exists(segmented_image_path)}")
        
        # Store the URL path for UI display
        output["segmented_image_url"] = f"segmented_images/{segmented_filename}"
        
        # Load classification model
        cls_model_path = os.path.join(settings.BASE_DIR, 'assets', 'models', 'pomegranate_3cls.pt')
        print(f" Classification model path: {cls_model_path}")
        print(f" Model exists: {os.path.exists(cls_model_path)}")
        
        classification_model = YOLO(cls_model_path)
        
        # Perform classification on the segmented image
        classification_results = classification_model.predict(source=segmented_image_path)
        
        # Process classification results
        if hasattr(classification_results[0], 'probs') and classification_results[0].probs:
            class_idx = classification_results[0].probs.top1
            confidence = classification_results[0].probs.top1conf.item()
            class_name = classification_results[0].names[class_idx]
            
            print(f"Classification result: {class_name} (confidence: {confidence})")
            
            # Use same structure as guava/apple
            output["top_prediction"] = {
                "class": class_name,
                "confidence": confidence
            }
            
            # Get top 5 predictions if available
            if hasattr(classification_results[0].probs, 'top5'):
                top5_indices = classification_results[0].probs.top5
                top5_confs = classification_results[0].probs.top5conf
                output["top5_predictions"] = []
                
                for i, (idx, conf) in enumerate(zip(top5_indices, top5_confs)):
                    output["top5_predictions"].append({
                        "rank": i+1,
                        "class": classification_results[0].names[idx],
                        "confidence": conf.item()
                    })
        
        else:
            # Fallback to object detection if classification not available
            result_obj = classification_results[0]
            if hasattr(result_obj, 'boxes') and result_obj.boxes is not None and len(result_obj.boxes) > 0:
                # Get the class index of the first detected object
                class_idx = int(result_obj.boxes.cls[0])
                confidence = float(result_obj.boxes.conf[0])
                class_name = classification_model.names[class_idx]
                
                print(f"Detection result: {class_name} (confidence: {confidence})")
                
                output["top_prediction"] = {
                    "class": class_name,
                    "confidence": confidence
                }
                
                # Get top 5 detections (or all if less than 5)
                all_detections = []
                for i in range(min(5, len(result_obj.boxes))):
                    class_idx = int(result_obj.boxes.cls[i])
                    confidence = float(result_obj.boxes.conf[i])
                    class_name = classification_model.names[class_idx]
                    
                    all_detections.append({
                        "rank": i+1,
                        "class": class_name,
                        "confidence": confidence
                    })
                
                output["top5_predictions"] = all_detections
            else:
                output["error"] = "No pomegranates detected in the segmented image"
            
    else:
        print("No masks detected in the image")
        output["error"] = "No pomegranates detected in the image"
    
    print(f"Returning output: {output}")
    return output