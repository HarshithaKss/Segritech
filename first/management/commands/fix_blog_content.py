from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Fix blog content formatting'

    def handle(self, *args, **options):
        blogs = BlogPost.objects.all()
        for blog in blogs:
            # Check if content is already properly formatted HTML
            if not blog.content.strip().startswith('<'):
                # Convert plain text to HTML with proper formatting
                content = blog.content.strip()
                paragraphs = content.split('\n\n')
                formatted_content = []
                
                for p in paragraphs:
                    if p.strip():
                        if p.strip().endswith(':'):
                            # This is likely a heading
                            formatted_content.append(f'<h3>{p.strip()}</h3>')
                        elif p.strip().startswith('•'):
                            # This is a bullet list
                            items = p.split('\n')
                            formatted_content.append('<ul>')
                            for item in items:
                                if item.strip():
                                    formatted_content.append(f'<li>{item.strip().lstrip("•").strip()}</li>')
                            formatted_content.append('</ul>')
                        elif any(line.strip().startswith(str(i)+'.') for i in range(1,10) for line in p.split('\n')):
                            # This is a numbered list
                            items = p.split('\n')
                            formatted_content.append('<ol>')
                            for item in items:
                                if item.strip():
                                    # Remove the number and dot from the start
                                    clean_item = '.'.join(item.split('.')[1:]).strip()
                                    if clean_item:
                                        formatted_content.append(f'<li>{clean_item}</li>')
                            formatted_content.append('</ol>')
                        else:
                            # Regular paragraph
                            formatted_content.append(f'<p>{p.strip()}</p>')
                
                blog.content = '\n'.join(formatted_content)
                blog.save()
                self.stdout.write(self.style.SUCCESS(f'Fixed content for blog: {blog.title}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Blog already has HTML content: {blog.title}')) 