/*
Custom JavaScript for BlogPost Admin Interface
Provides dynamic content creation helpers and validation
*/

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 SegriTech Blog Admin Enhancement Loaded');
    
    // Initialize all features
    initializeJSONValidation();
    initializeContentPreview();
    initializeImageHelpers();
    initializeReadTimeCalculator();
    addHelpfulPlaceholders();
    
    // JSON Validation for gallery_images and content_sections
    function initializeJSONValidation() {
        const jsonFields = ['gallery_images', 'content_sections'];
        
        jsonFields.forEach(fieldName => {
            const field = document.getElementById(`id_${fieldName}`);
            if (field) {
                field.addEventListener('blur', function() {
                    validateJSONField(this, fieldName);
                });
                
                // Add helpful examples
                addJSONExamples(field, fieldName);
            }
        });
    }
    
    function validateJSONField(field, fieldName) {
        const value = field.value.trim();
        if (value === '') return; // Empty is OK
        
        try {
            const parsed = JSON.parse(value);
            showFieldSuccess(field, `✅ Valid JSON format for ${fieldName}`);
            
            // Validate structure based on field type
            if (fieldName === 'gallery_images') {
                validateGalleryImagesStructure(parsed, field);
            } else if (fieldName === 'content_sections') {
                validateContentSectionsStructure(parsed, field);
            }
        } catch (error) {
            showFieldError(field, `❌ Invalid JSON: ${error.message}`);
        }
    }
    
    function validateGalleryImagesStructure(data, field) {
        if (!Array.isArray(data)) {
            showFieldError(field, '❌ Gallery images must be an array');
            return;
        }
        
        for (let i = 0; i < data.length; i++) {
            const item = data[i];
            if (!item.url) {
                showFieldError(field, `❌ Item ${i + 1} missing required "url" field`);
                return;
            }
        }
        showFieldSuccess(field, `✅ Valid gallery images format (${data.length} images)`);
    }
    
    function validateContentSectionsStructure(data, field) {
        if (!Array.isArray(data)) {
            showFieldError(field, '❌ Content sections must be an array');
            return;
        }
        
        const validTypes = ['text', 'image', 'video', 'chart', 'quote'];
        for (let i = 0; i < data.length; i++) {
            const item = data[i];
            if (!item.type || !validTypes.includes(item.type)) {
                showFieldError(field, `❌ Item ${i + 1} has invalid type. Must be one of: ${validTypes.join(', ')}`);
                return;
            }
            if (!item.content) {
                showFieldError(field, `❌ Item ${i + 1} missing required "content" field`);
                return;
            }
        }
        showFieldSuccess(field, `✅ Valid content sections format (${data.length} sections)`);
    }
    
    function showFieldError(field, message) {
        clearFieldMessages(field);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error';
        errorDiv.style.cssText = 'background: #fed7d7; border: 1px solid #feb2b2; color: #c53030; padding: 8px; margin-top: 5px; border-radius: 4px; font-size: 12px;';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }
    
    function showFieldSuccess(field, message) {
        clearFieldMessages(field);
        const successDiv = document.createElement('div');
        successDiv.className = 'field-success';
        successDiv.style.cssText = 'background: #c6f6d5; border: 1px solid #9ae6b4; color: #2f855a; padding: 8px; margin-top: 5px; border-radius: 4px; font-size: 12px;';
        successDiv.textContent = message;
        field.parentNode.appendChild(successDiv);
    }
    
    function clearFieldMessages(field) {
        const parent = field.parentNode;
        const existingMessages = parent.querySelectorAll('.field-error, .field-success');
        existingMessages.forEach(msg => msg.remove());
    }
    
    // Add JSON examples
    function addJSONExamples(field, fieldName) {
        let example = '';
        if (fieldName === 'gallery_images') {
            example = JSON.stringify([
                {
                    "url": "/static/images/blog/chart1.png",
                    "caption": "Sales Growth Chart 2024",
                    "alt": "Chart showing 40% sales growth"
                },
                {
                    "url": "/static/images/blog/team.jpg", 
                    "caption": "Our Research Team",
                    "alt": "SegriTech research team photo"
                }
            ], null, 2);
        } else if (fieldName === 'content_sections') {
            example = JSON.stringify([
                {
                    "type": "text",
                    "content": "<h3>Market Analysis</h3><p>Our research shows...</p>",
                    "style": "background: #f8f9fa; padding: 20px;",
                    "order": 1
                },
                {
                    "type": "image", 
                    "content": "/static/images/blog/market-chart.png",
                    "style": "width: 100%; border-radius: 8px;",
                    "order": 2
                },
                {
                    "type": "quote",
                    "content": "Innovation is the key to agricultural transformation",
                    "style": "font-size: 24px; color: #4CAF50;",
                    "order": 3
                }
            ], null, 2);
        }
        
        field.placeholder = `Example:\n${example}`;
    }
    
    // Content preview functionality
    function initializeContentPreview() {
        const contentField = document.getElementById('id_content');
        if (contentField) {
            const previewButton = document.createElement('button');
            previewButton.type = 'button';
            previewButton.textContent = '👁️ Preview Content';
            previewButton.style.cssText = 'background: #3182ce; color: white; border: none; padding: 8px 16px; border-radius: 4px; margin-top: 10px; cursor: pointer;';
            
            previewButton.addEventListener('click', function() {
                showContentPreview(contentField.value);
            });
            
            contentField.parentNode.appendChild(previewButton);
        }
    }
    
    function showContentPreview(content) {
        const previewDiv = document.getElementById('content-preview') || createPreviewDiv();
        previewDiv.innerHTML = content || '<p style="color: #718096; font-style: italic;">No content to preview</p>';
    }
    
    function createPreviewDiv() {
        const previewDiv = document.createElement('div');
        previewDiv.id = 'content-preview';
        previewDiv.className = 'content-preview';
        previewDiv.style.cssText = 'border: 2px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-top: 15px; background: white; max-height: 400px; overflow-y: auto;';
        
        const title = document.createElement('h4');
        title.textContent = '📖 Content Preview';
        title.style.cssText = 'margin: 0 0 15px 0; color: #4a5568; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;';
        
        previewDiv.appendChild(title);
        document.getElementById('id_content').parentNode.appendChild(previewDiv);
        return previewDiv;
    }
    
    // Image upload helpers
    function initializeImageHelpers() {
        const imageField = document.getElementById('id_featured_image');
        if (imageField) {
            imageField.addEventListener('change', function(e) {
                if (e.target.files && e.target.files[0]) {
                    showImagePreview(e.target.files[0], imageField);
                }
            });
        }
    }
    
    function showImagePreview(file, field) {
        const reader = new FileReader();
        reader.onload = function(e) {
            let previewImg = field.parentNode.querySelector('.image-preview');
            if (!previewImg) {
                previewImg = document.createElement('img');
                previewImg.className = 'image-preview';
                previewImg.style.cssText = 'max-width: 200px; max-height: 200px; border-radius: 8px; margin-top: 10px; border: 2px solid #e2e8f0;';
                field.parentNode.appendChild(previewImg);
            }
            previewImg.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
    
    // Reading time calculator
    function initializeReadTimeCalculator() {
        const contentField = document.getElementById('id_content');
        const readTimeField = document.getElementById('id_estimated_read_time');
        
        if (contentField && readTimeField) {
            contentField.addEventListener('input', function() {
                const wordCount = getWordCount(this.value);
                const estimatedTime = Math.max(1, Math.ceil(wordCount / 200)); // 200 words per minute
                readTimeField.value = estimatedTime;
                
                // Show word count info
                showWordCountInfo(contentField, wordCount, estimatedTime);
            });
        }
    }
    
    function getWordCount(text) {
        // Remove HTML tags and count words
        const cleanText = text.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
        return cleanText ? cleanText.split(' ').length : 0;
    }
    
    function showWordCountInfo(field, wordCount, readTime) {
        let infoDiv = field.parentNode.querySelector('.word-count-info');
        if (!infoDiv) {
            infoDiv = document.createElement('div');
            infoDiv.className = 'word-count-info';
            infoDiv.style.cssText = 'background: #e6fffa; border: 1px solid #4fd1c7; color: #234e52; padding: 8px; margin-top: 5px; border-radius: 4px; font-size: 12px;';
            field.parentNode.appendChild(infoDiv);
        }
        infoDiv.textContent = `📊 ${wordCount} words • ${readTime} min read`;
    }
    
    // Add helpful placeholders
    function addHelpfulPlaceholders() {
        const placeholders = {
            'id_custom_css': '<style>\n.custom-highlight {\n    background: linear-gradient(135deg, #4CAF50, #66BB6A);\n    color: white;\n    padding: 20px;\n    border-radius: 10px;\n}\n\n.chart-container {\n    text-align: center;\n    margin: 30px 0;\n}\n</style>',
            'id_custom_js': '<script>\ndocument.addEventListener(\'DOMContentLoaded\', function() {\n    // Add interactive features\n    console.log(\'Blog post enhanced!\');\n    \n    // Example: Smooth scroll for anchor links\n    document.querySelectorAll(\'a[href^="#"]\').forEach(anchor => {\n        anchor.addEventListener(\'click\', function (e) {\n            e.preventDefault();\n            const target = document.querySelector(this.getAttribute(\'href\'));\n            if (target) {\n                target.scrollIntoView({ behavior: \'smooth\' });\n            }\n        });\n    });\n});\n</script>',
            'id_tags': 'agriculture, technology, innovation, segritech, farming, automation',
            'id_meta_description': 'Discover how SegriTech is revolutionizing agriculture through innovative technology solutions...'
        };
        
        Object.entries(placeholders).forEach(([id, placeholder]) => {
            const field = document.getElementById(id);
            if (field) {
                field.placeholder = placeholder;
            }
        });
    }
    
    // Add quick action buttons
    function addQuickActions() {
        const publishField = document.getElementById('id_is_published');
        const featuredField = document.getElementById('id_is_featured');
        
        if (publishField && featuredField) {
            const quickActionsDiv = document.createElement('div');
            quickActionsDiv.style.cssText = 'background: #f7fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 15px; margin: 15px 0;';
            quickActionsDiv.innerHTML = `
                <h4 style="margin: 0 0 10px 0; color: #4a5568;">🚀 Quick Actions</h4>
                <button type="button" onclick="document.getElementById('id_is_published').checked = true; document.getElementById('id_is_featured').checked = true;" style="background: #48bb78; color: white; border: none; padding: 8px 16px; border-radius: 4px; margin-right: 10px; cursor: pointer;">✨ Publish & Feature</button>
                <button type="button" onclick="document.getElementById('id_is_published').checked = true; document.getElementById('id_is_featured').checked = false;" style="background: #4299e1; color: white; border: none; padding: 8px 16px; border-radius: 4px; margin-right: 10px; cursor: pointer;">📝 Publish Only</button>
                <button type="button" onclick="document.getElementById('id_is_published').checked = false; document.getElementById('id_is_featured').checked = false;" style="background: #a0aec0; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">💾 Save as Draft</button>
            `;
            
            publishField.closest('.form-row').parentNode.insertBefore(quickActionsDiv, publishField.closest('.form-row'));
        }
    }
    
    // Initialize quick actions
    setTimeout(addQuickActions, 1000);
    
    console.log('✅ Blog admin enhancements ready!');
}); 