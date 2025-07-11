"""
Management command to import LinkedIn articles as blog posts.
This script replaces existing blog content with comprehensive articles about:
1. Countries importing fruits & vegetables from India (research category)
2. Export fruits and vegetables to Bangladesh (market-analysis category)  
3. Groundbreaking robots in agriculture (automation category)
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from first.models import BlogPost
import datetime

class Command(BaseCommand):
    help = 'Import LinkedIn articles as blog posts with comprehensive content'

    def handle(self, *args, **options):
        # Clear existing blog posts first
        BlogPost.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing blog posts'))

        # Article 1: Countries importing fruits & vegetables from India
        article1_content = """
        <h1>List of Countries Importing Fruit & Vegetables from India</h1>
        
        <p>India has established itself as a major exporter of fruits and vegetables, reaching over 150 countries worldwide. In the fiscal year 2023-24, the total export value reached approximately <strong>$2.1 billion</strong>, showing a remarkable 20% increase from the previous year.</p>

        <img src="/static/images/blog/List_of_countries.png" alt="Countries Importing Fruit & Vegetables from India" style="max-width: 100%; height: auto; margin: 20px 0; border-radius: 8px;">

        <h2>Export Value Breakdown</h2>
        <p>The $2.1 billion export value is distributed across different categories:</p>
        <ul>
            <li><strong>Fresh Vegetables:</strong> $891 million (18% growth)</li>
            <li><strong>Fresh Fruits:</strong> $863.7 million (22% growth)</li>
            <li><strong>Processed Products:</strong> $652.8 million (15% growth)</li>
        </ul>

        <h2>Major Export Destinations</h2>
        
        <h3>Middle East & Gulf Countries</h3>
        <ul>
            <li><strong>UAE:</strong> $245 million - Primary hub for re-exports</li>
            <li><strong>Saudi Arabia:</strong> $189 million - Growing demand for fresh produce</li>
            <li><strong>Kuwait:</strong> $98 million - Premium fruit market</li>
            <li><strong>Qatar:</strong> $67 million - High-value vegetable imports</li>
        </ul>

        <h3>South Asian Neighbors</h3>
        <ul>
            <li><strong>Bangladesh:</strong> $156 million - Major vegetable importer</li>
            <li><strong>Nepal:</strong> $89 million - Border trade advantage</li>
            <li><strong>Sri Lanka:</strong> $78 million - Spices and processed goods</li>
        </ul>

        <h3>Southeast Asia</h3>
        <ul>
            <li><strong>Malaysia:</strong> $134 million - Diverse product range</li>
            <li><strong>Singapore:</strong> $112 million - High-value market</li>
            <li><strong>Thailand:</strong> $87 million - Processed products focus</li>
        </ul>

        <h3>Europe & Americas</h3>
        <ul>
            <li><strong>United Kingdom:</strong> $98 million - Ethnic food market</li>
            <li><strong>United States:</strong> $76 million - Organic & specialty items</li>
            <li><strong>Germany:</strong> $54 million - Quality-focused market</li>
        </ul>

        <h2>Top Global Importers</h2>
        <p>Here's a chart showing the top countries importing fruits and vegetables from India:</p>
        <img src="/static/web/bar_graph.png" alt="Top 10 Countries Importing from India" style="max-width: 100%; height: auto; margin: 20px 0; border-radius: 8px;">

        <h2>Growth Factors</h2>
        <p>The 20% growth in exports can be attributed to several key factors:</p>
        <ul>
            <li><strong>Seasonal Demand:</strong> Peak exports during October-March coinciding with global winter seasons</li>
            <li><strong>Quality Premium:</strong> Indian produce commands 15-25% premium in Gulf markets</li>
            <li><strong>Processing Growth:</strong> Value-added products showing 30% higher growth rates</li>
            <li><strong>Organic Segment:</strong> Certified organic exports growing at 40% annually</li>
        </ul>

        <h2>SegriTech's Role</h2>
        <p>At SegriTech, our sorting and grading technologies help ensure that Indian agricultural exports meet international quality standards. Our solutions help exporters:</p>
        <ul>
            <li>Achieve consistent quality grades that command premium prices</li>
            <li>Reduce post-harvest losses by up to 40%</li>
            <li>Meet international food safety certifications</li>
            <li>Optimize packaging for long-distance transportation</li>
        </ul>
        <p>With growing global demand for Indian produce, technology-driven quality assurance is crucial for maintaining our competitive edge in international markets.</p>
        """

        blog1 = BlogPost.objects.create(
            title='List of Countries Importing Fruit & Vegetables from India',
            slug='countries-importing-fruits-vegetables-india',
            category='research',
            author_name='Hetendra Singh',
            author_title='CEO & Founder, SegriTech',
            excerpt='India has solidified its position as a leading exporter of fruits and vegetables, reaching over 150 countries worldwide with a market value exceeding $2.1 billion.',
            content=article1_content,
            external_url='https://www.linkedin.com/pulse/list-countries-importing-fruit-vegetables-from-india-segritech-segritech-trgvc/',
            is_published=True,
            published_at=timezone.datetime(2024, 8, 14, tzinfo=timezone.get_current_timezone()),
            views_count=156,
            is_featured=True
        )

        # Article 2: Export fruits and vegetables to Bangladesh
        article2_content = """
        <h1>Export Fruits and Vegetables to Bangladesh</h1>
        
        <p>Bangladesh has emerged as a significant market for Indian agricultural exports. The country's growing population and rising income levels have created substantial demand for fresh produce, making it an important trading partner for India.</p>

        <img src="/static/images/blog/Export_fruit.png" alt="Export Fruits and Vegetables to Bangladesh" style="max-width: 100%; height: auto; margin: 20px 0; border-radius: 8px;">

        <h2>Market Overview</h2>
        <p>Bangladesh's import market for fruits and vegetables shows impressive growth:</p>
        <ul>
            <li><strong>Total Vegetable Imports:</strong> $5.81 billion annually</li>
            <li><strong>Fruit Imports:</strong> $1.1 billion (growing at 8% annually)</li>
            <li><strong>India's Share:</strong> $300 million with significant growth potential</li>
            <li><strong>Annual Growth Rate:</strong> 6% consistent upward trend</li>
        </ul>

        <h2>Import Volume Statistics</h2>
        <ul>
            <li><strong>Total Volume:</strong> 616,000 tonnes of fruits and vegetables imported annually</li>
            <li><strong>Growth Rate:</strong> 19.18% year-on-year increase</li>
            <li><strong>Daily Capacity:</strong> 1,687 tonnes per day average</li>
            <li><strong>Peak Season:</strong> 2,500+ tonnes per day</li>
        </ul>

        <h2>Key Product Categories</h2>
        
        <h3>Vegetables (Major Categories)</h3>
        <ul>
            <li><strong>Onions:</strong> 180,000 tonnes ($89M value)</li>
            <li><strong>Potatoes:</strong> 125,000 tonnes ($45M value)</li>
            <li><strong>Garlic:</strong> 45,000 tonnes ($78M value)</li>
            <li><strong>Ginger:</strong> 32,000 tonnes ($56M value)</li>
            <li><strong>Green Vegetables:</strong> 89,000 tonnes ($92M value)</li>
        </ul>

        <h3>Fruits (High Demand)</h3>
        <ul>
            <li><strong>Apples:</strong> 67,000 tonnes ($156M value)</li>
            <li><strong>Grapes:</strong> 23,000 tonnes ($78M value)</li>
            <li><strong>Oranges:</strong> 34,000 tonnes ($45M value)</li>
            <li><strong>Mangoes:</strong> 18,000 tonnes ($67M value)</li>
            <li><strong>Bananas:</strong> 56,000 tonnes ($34M value)</li>
        </ul>

        <h2>Trade Routes</h2>
        
        <h3>Land Routes (Primary)</h3>
        <ul>
            <li><strong>Petrapole-Benapole:</strong> Main gateway (60% of trade)</li>
            <li><strong>Gede-Darshana:</strong> Secondary route (25% of trade)</li>
            <li><strong>Akhaura-Agartala:</strong> Northeast corridor (15% of trade)</li>
        </ul>
        
        <h3>Sea Routes (Secondary)</h3>
        <ul>
            <li><strong>Kolkata-Chittagong:</strong> For bulk shipments</li>
            <li><strong>Chennai-Chittagong:</strong> Southern India exports</li>
        </ul>

        <h2>Challenges & Solutions</h2>
        <ul>
            <li><strong>Quality Standards:</strong> Inconsistent quality affecting pricing - Solution: Advanced sorting systems</li>
            <li><strong>Transportation:</strong> Long transit times affecting freshness - Solution: Cold chain development</li>
            <li><strong>Documentation:</strong> Complex procedures - Solution: Digital trade platforms</li>
            <li><strong>Payment Terms:</strong> Extended cycles - Solution: Trade finance products</li>
        </ul>

        <h2>Future Outlook (2024-2027)</h2>
        <ul>
            <li>Total market expected to reach <strong>$8.5 billion by 2027</strong></li>
            <li>India's share projected to grow to <strong>$500 million</strong></li>
            <li>Premium segment growing at <strong>12% annually</strong></li>
            <li>Organic produce demand increasing by <strong>25% yearly</strong></li>
        </ul>

        <h2>SegriTech's Solutions for Bangladesh Exports</h2>
        <p>SegriTech's technology solutions address key challenges in Bangladesh export markets:</p>
        <ul>
            <li><strong>Quality Assurance:</strong> AI-powered sorting systems ensure consistent quality, reducing rejection rates by up to 90%</li>
            <li><strong>Optimized Packaging:</strong> Smart packaging solutions that extend shelf life during 24-48 hour transit</li>
            <li><strong>Traceability:</strong> Complete farm-to-fork traceability ensuring food safety compliance</li>
            <li><strong>Processing Efficiency:</strong> Automated systems reduce processing time by 60%</li>
        </ul>
        <p>With our technology, Indian exporters can capture a larger share of Bangladesh's growing fresh produce market while commanding premium prices.</p>
        """

        blog2 = BlogPost.objects.create(
            title='Export Fruits and Vegetables to Bangladesh',
            slug='export-fruits-vegetables-bangladesh',
            category='research',
            author_name='Hetendra Singh',
            author_title='CEO & Founder, SegriTech',
            excerpt='Bangladesh has become a significant importer of fruits and vegetables from India, with imports valued at $2.5B annually and growing at 6% year-on-year.',
            content=article2_content,
            external_url='https://www.linkedin.com/pulse/export-fruits-vegetables-bangladesh-segritech-gqo8c/',
            is_published=True,
            published_at=timezone.datetime(2024, 7, 2, tzinfo=timezone.get_current_timezone()),
            views_count=87,
            is_featured=False
        )

        # Article 3: Groundbreaking Robots in Agriculture
        article3_content = """
        <h1>Groundbreaking Robots in Agriculture</h1>
        
        <p>Agricultural robots are transforming the farming industry by automating various tasks and increasing efficiency. The market value for agriculture robots is expected to reach <strong>$11.58 billion by 2025</strong>.</p>

        <img src="/static/images/blog/Ground.png" alt="Groundbreaking Robots in Agriculture" style="max-width: 100%; height: auto; margin: 20px 0; border-radius: 8px;">

        <h2>Market Growth</h2>
        <ul>
            <li><strong>Market Value 2025:</strong> $11.58 billion (22.8% CAGR)</li>
            <li><strong>Current Adoption:</strong> 15% with rapid expansion</li>
            <li><strong>ROI Timeline:</strong> 18-24 months average payback</li>
        </ul>

        <h2>Types of Agricultural Robots</h2>
        
        <h3>Harvesting Robots</h3>
        <p><strong>Function:</strong> Automated fruit and vegetable picking with precision and speed</p>
        <ul>
            <li><strong>Strawberry Harvesters:</strong> Pick 8-10 berries per minute with 95% accuracy</li>
            <li><strong>Apple Picking Robots:</strong> Harvest 1 apple every 7 seconds</li>
            <li><strong>Citrus Harvesters:</strong> 40% faster than manual picking</li>
            <li><strong>Tomato Robots:</strong> Identify ripeness with 98% accuracy</li>
        </ul>
        <p><strong>Impact:</strong> Reduce labor costs by 50-70% while increasing harvest efficiency</p>

        <h3>Weeding & Plant Care Robots</h3>
        <p><strong>Function:</strong> Precision weed control and plant maintenance using AI vision</p>
        <ul>
            <li><strong>Laser Weeding:</strong> Eliminate weeds without chemicals</li>
            <li><strong>Micro-spray Systems:</strong> 95% reduction in pesticide use</li>
            <li><strong>Plant Health Monitoring:</strong> Early disease detection</li>
            <li><strong>Precision Cultivation:</strong> Soil management around plants</li>
        </ul>
        <p><strong>Impact:</strong> 90% reduction in herbicide use, 60% lower operational costs</p>

        <h3>Autonomous Tractors & Field Robots</h3>
        <p><strong>Function:</strong> Unmanned field operations for planting, cultivation, and maintenance</p>
        <ul>
            <li><strong>Seeding Robots:</strong> Precision planting with GPS accuracy</li>
            <li><strong>Autonomous Cultivators:</strong> 24/7 field operations</li>
            <li><strong>Smart Spraying:</strong> Variable rate application systems</li>
            <li><strong>Soil Analysis Robots:</strong> Real-time soil health monitoring</li>
        </ul>
        <p><strong>Impact:</strong> 30% increase in operational efficiency, 25% fuel savings</p>

        <h2>Industry Leaders</h2>
        <ul>
            <li><strong>Harvest CROO Robotics:</strong> Strawberry harvesting robots - 30 robots replace 180 workers</li>
            <li><strong>John Deere:</strong> Autonomous tractors with See & Spray technology</li>
            <li><strong>Iron Ox:</strong> Robotic greenhouse farming - 30x more productive per square foot</li>
            <li><strong>Abundant Robotics:</strong> Apple harvesting with 90%+ efficiency</li>
        </ul>

        <h2>Key Benefits</h2>
        <ul>
            <li><strong>Economic:</strong> 50-70% reduction in labor costs, 25-40% productivity increase</li>
            <li><strong>Environmental:</strong> 90% reduction in pesticide usage, 40% less water consumption</li>
            <li><strong>Quality:</strong> 95-98% accuracy in sorting, consistent 24/7 operations</li>
            <li><strong>Efficiency:</strong> Weather-independent operations, predictive maintenance</li>
        </ul>

        <h2>Future Outlook (2025-2030)</h2>
        <ul>
            <li>Market value expected to reach <strong>$25.7 billion by 2030</strong></li>
            <li>45% of large farms will adopt robotic systems</li>
            <li>Developing countries will drive 60% of growth</li>
            <li>Small-scale affordable robots will emerge for mid-size farms</li>
        </ul>

        <h2>SegriTech's Innovation</h2>
        <p>At SegriTech, we're developing cutting-edge agricultural robotics solutions:</p>
        <ul>
            <li><strong>AI-Powered Sorting:</strong> 99.2% accuracy in quality assessment, 10x faster processing</li>
            <li><strong>Modular Platforms:</strong> Customizable robots for different crops and farm sizes</li>
            <li><strong>Data Analytics:</strong> Comprehensive farm management with predictive analytics</li>
            <li><strong>Edge Computing:</strong> Real-time processing for remote locations</li>
        </ul>
        <p>Through our robotic solutions, we're helping Indian farmers increase yields by 35-50%, reduce losses from 30% to under 5%, and achieve international quality standards for export markets.</p>
        """

        blog3 = BlogPost.objects.create(
            title='Groundbreaking Robots in Agriculture',
            slug='groundbreaking-robots-agriculture',
            category='automation',
            author_name='Hetendra Singh',
            author_title='CEO & Founder, SegriTech',
            excerpt='Agricultural robots are transforming the farming industry by automating various tasks and increasing efficiency. The market value for agriculture robots is expected to reach $11.58 billion by 2025.',
            content=article3_content,
            external_url='https://www.linkedin.com/pulse/groundbreaking-robots-agriculture-segritech-1xiuc/',
            is_published=True,
            published_at=timezone.datetime(2024, 5, 27, tzinfo=timezone.get_current_timezone()),
            views_count=19,
            is_featured=False
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {BlogPost.objects.count()} LinkedIn articles:'))
        self.stdout.write(f'1. {blog1.title} - {blog1.category}')
        self.stdout.write(f'2. {blog2.title} - {blog2.category}') 
        self.stdout.write(f'3. {blog3.title} - {blog3.category}')
        self.stdout.write(self.style.SUCCESS('All articles imported successfully!')) 