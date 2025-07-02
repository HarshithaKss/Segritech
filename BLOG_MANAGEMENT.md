# Blog Management - Featured Blogs on Homepage

## Overview

The SegriTech website now has a **Featured Blog** system that allows you to control which blog articles appear on the homepage in the "View All Insights" section. Only blogs marked as both **Published** and **Featured** will be displayed on the homepage.

## How It Works

- **Homepage Display**: Shows up to 3 most recent featured blog posts
- **Admin Control**: Easy management through Django admin interface
- **Command Line Tools**: Management commands for bulk operations

## Managing Featured Blogs

### Option 1: Using Django Admin (Recommended)

1. **Access Admin Panel**
   - Go to: `http://your-domain/admin/`
   - Login with your admin credentials
   - Navigate to: `First > Blog posts`

2. **Set Blog as Featured**
   - Click on any blog post to edit
   - In the "Publishing" section, check the ✅ **"Is featured"** checkbox
   - Make sure ✅ **"Is published"** is also checked
   - Click **"Save"**

3. **Bulk Operations**
   - Select multiple blog posts from the list
   - Choose action: **"Mark selected blogs as featured"**
   - Click **"Go"**

4. **Quick Edit**
   - Use the **"Is featured"** column in the list view for quick editing
   - Check/uncheck boxes directly from the list

### Option 2: Using Management Commands

We've provided helpful command-line tools for managing featured blogs:

#### Check Current Status
```bash
python manage.py manage_featured_blogs --featured-count
```

#### List All Featured Blogs
```bash
python manage.py manage_featured_blogs --list-featured
```

#### Set a Blog as Featured
```bash
python manage.py manage_featured_blogs --set-featured "blog-slug-here"
```

#### Remove from Featured
```bash
python manage.py manage_featured_blogs --unset-featured "blog-slug-here"
```

#### Clear All Featured (Emergency)
```bash
python manage.py manage_featured_blogs --clear-all-featured
```

## Important Rules

### Homepage Display Logic
- **Maximum**: 3 blogs on homepage
- **Order**: Most recently published featured blogs appear first
- **Requirements**: Must be both `is_published=True` AND `is_featured=True`

### What Happens When...

| Scenario | Result |
|----------|--------|
| **0 featured blogs** | ⚠️ Empty insights section on homepage |
| **1-3 featured blogs** | ✅ Perfect! All will show on homepage |
| **4+ featured blogs** | ⚠️ Only 3 most recent will show |
| **Featured but unpublished** | ❌ Won't show anywhere |
| **Published but not featured** | ✅ Shows in /insights/ but not homepage |

## Best Practices

### Content Strategy
1. **Keep 3 Featured**: Maintain exactly 3 featured blogs for optimal homepage display
2. **Rotate Content**: Regularly update featured blogs to keep homepage fresh
3. **Quality First**: Only feature your best, most important content
4. **Recent Content**: Featured blogs should be recent and relevant

### Workflow Recommendations
1. **Create Blog**: Write and save as draft
2. **Review Content**: Ensure quality and accuracy
3. **Publish**: Set `is_published=True`
4. **Feature Decision**: Choose if it should appear on homepage
5. **Monitor**: Use analytics to track performance

## Examples

### Scenario 1: New Blog Launch
```bash
# Create blog in admin, then:
python manage.py manage_featured_blogs --set-featured "new-ai-breakthrough-2024"
python manage.py manage_featured_blogs --featured-count
# Result: ✅ Perfect! 3 featured posts will show on homepage.
```

### Scenario 2: Too Many Featured
```bash
python manage.py manage_featured_blogs --featured-count
# Result: ⚠️ 5 featured posts found - only the 3 most recent will show on homepage.

# Remove older ones:
python manage.py manage_featured_blogs --unset-featured "old-blog-slug"
```

### Scenario 3: Emergency Reset
```bash
# If something goes wrong:
python manage.py manage_featured_blogs --clear-all-featured
# Then re-add the 3 you want:
python manage.py manage_featured_blogs --set-featured "blog-1"
python manage.py manage_featured_blogs --set-featured "blog-2"  
python manage.py manage_featured_blogs --set-featured "blog-3"
```

## Technical Details

### Database Fields
- `is_published`: Boolean - Controls if blog appears anywhere
- `is_featured`: Boolean - Controls if blog appears on homepage
- `published_at`: DateTime - Used for ordering featured blogs

### View Logic
```python
# Homepage query (first/views.py)
blog_posts = BlogPost.objects.filter(
    is_published=True, 
    is_featured=True
).order_by('-published_at', '-created_at')[:3]
```

### Admin Actions Available
- Mark selected blogs as featured
- Unmark selected blogs as featured  
- Mark selected blogs as published
- Mark selected blogs as unpublished

## Troubleshooting

### Problem: No blogs showing on homepage
**Solution**: Check that blogs are both published AND featured
```bash
python manage.py manage_featured_blogs --featured-count
```

### Problem: Wrong blogs showing on homepage
**Solution**: Check publication dates and featured status
```bash
python manage.py manage_featured_blogs --list-featured
```

### Problem: Need to change homepage blogs quickly
**Solution**: Use admin bulk actions or management commands
```bash
# Quick method via admin:
# 1. Go to blog list
# 2. Uncheck "Is featured" for old blogs
# 3. Check "Is featured" for new blogs
```

## Support

For technical issues or questions about blog management:
1. Check this documentation first
2. Use the management commands to diagnose issues
3. Contact the development team with specific error messages

---

**Last Updated**: January 2025  
**Version**: 1.0 