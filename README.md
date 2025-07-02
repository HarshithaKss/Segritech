# SegriTech

SegriTech is a comprehensive web application for an agricultural technology company, showcasing various products and services in the agricultural sector.

## Features

- Product Catalog with categories (Size Graders, Quality Graders, Weight Graders, etc.)
- Career Portal with job listings and application system
- Newsletter Subscription
- Contact Form
- Blog Section
- Media Coverage Section
- Testimonials
- Interactive Product Inquiry System

## Tech Stack

- Django 5.2.2
- Python 3.x
- HTML/CSS/JavaScript
- Bootstrap
- Font Awesome
- AOS (Animate On Scroll)
- Custom CSS for styling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HarshithaKss/segritech.git
cd segritech
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application.

## Project Structure

- `first/` - Main Django app containing core functionality
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files
- `assets/` - Project assets

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
