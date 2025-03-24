import os
import sys
import django
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
import shutil
from decimal import Decimal

# Lấy đường dẫn hiện tại của script
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Thêm đường dẫn dự án vào sys.path
sys.path.insert(0, project_root)

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuvidaivietapp.settings')
django.setup()

from news.models import Category, News, NewsImage
from courses.models import CourseCategory, Course, Lesson
from taggit.models import Tag

def create_media_directories():
    """Tạo các thư mục media cần thiết"""
    media_dirs = [
        'news/thumbnails',
        'news/images',
        'courses/thumbnails'
    ]
    
    for dir_path in media_dirs:
        full_path = os.path.join(project_root, 'media', dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created directory: {full_path}")

def populate_data():
    # Tạo thư mục media
    create_media_directories()
    
    # Tạo admin user
    admin_user, _ = User.objects.get_or_create(username='admin', defaults={
        'email': 'admin@example.com',
        'is_staff': True,
        'is_superuser': True
    })
    admin_user.set_password('admin123')
    admin_user.save()
    print("Created admin user")

    # Tạo categories cho tin tức
    news_categories = [
        {
            'name': 'Công nghệ',
            'slug': 'cong-nghe',
            'description': 'Tin tức về công nghệ, AI, blockchain và các xu hướng mới nhất trong lĩnh vực công nghệ.'
        },
        {
            'name': 'Giáo dục',
            'slug': 'giao-duc',
            'description': 'Tin tức về giáo dục, phương pháp học tập, và các chính sách giáo dục mới.'
        },
        {
            'name': 'Thể thao',
            'slug': 'the-thao',
            'description': 'Tin tức thể thao trong nước và quốc tế, các giải đấu lớn.'
        },
        {
            'name': 'Kinh tế',
            'slug': 'kinh-te',
            'description': 'Tin tức về kinh tế, tài chính, đầu tư và thị trường.'
        },
        {
            'name': 'Văn hóa',
            'slug': 'van-hoa',
            'description': 'Tin tức về văn hóa, nghệ thuật, ẩm thực và lối sống.'
        }
    ]

    for cat_data in news_categories:
        category, _ = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': cat_data['slug'],
                'description': cat_data['description']
            }
        )
        print(f"Created category: {category.name}")

    # Tạo tin tức
    news_data = [
        {
            'title': 'AI Đang Thay Đổi Thế Giới Như Thế Nào',
            'slug': 'ai-dang-thay-doi-the-gioi-nhu-the-nao',
            'category': Category.objects.get(name='Công nghệ'),
            'thumbnail': 'news/thumbnails/ai_world.jpg',
            'content': '''
                Trí tuệ nhân tạo (AI) đang thay đổi cách chúng ta sống và làm việc một cách chưa từng có. 
                Từ việc chẩn đoán bệnh chính xác hơn đến việc tối ưu hóa quy trình sản xuất, AI đang mở ra những khả năng mới cho nhân loại.

                Trong lĩnh vực y tế, AI đang giúp các bác sĩ chẩn đoán bệnh chính xác hơn và nhanh hơn. 
                Các thuật toán AI có thể phân tích hàng nghìn hình ảnh y tế trong vài giây, giúp phát hiện các dấu hiệu bệnh tật mà mắt thường có thể bỏ sót.

                Trong lĩnh vực giáo dục, AI đang tạo ra các khóa học được cá nhân hóa, 
                giúp học viên học tập hiệu quả hơn dựa trên tốc độ và phong cách học tập của họ.

                Tuy nhiên, sự phát triển của AI cũng đặt ra những thách thức về đạo đức và việc làm. 
                Chúng ta cần đảm bảo rằng AI được phát triển và sử dụng một cách có trách nhiệm, 
                vì lợi ích của toàn nhân loại.
            ''',
            'tags': ['AI', 'Công nghệ', 'Tương lai', 'Đổi mới', 'Kỹ thuật'],
            'images': [
                ('news/images/ai_image1.jpg', 'Xe tự lái sử dụng AI'),
                ('news/images/ai_image2.jpg', 'Trợ lý ảo AI'),
                ('news/images/ai_image3.jpg', 'AI trong y tế')
            ]
        },
        {
            'title': 'Kỳ Thi Đại Học 2025 Sẽ Có Gì Mới?',
            'slug': 'ky-thi-dai-hoc-2025-se-co-gi-moi',
            'category': Category.objects.get(name='Giáo dục'),
            'thumbnail': 'news/thumbnails/exam_2025.jpg',
            'content': '''
                Bộ Giáo dục vừa công bố một số thay đổi quan trọng trong kỳ thi đại học 2025, 
                nhằm đánh giá toàn diện năng lực của học sinh và phù hợp với xu hướng giáo dục hiện đại.

                Những thay đổi chính bao gồm:
                - Thêm bài thi đánh giá năng lực tư duy
                - Tăng cường phần thi thực hành
                - Đa dạng hóa hình thức thi
                - Tích hợp kiến thức liên môn

                Các chuyên gia giáo dục cho rằng những thay đổi này sẽ giúp:
                - Đánh giá chính xác hơn năng lực thực tế của học sinh
                - Giảm áp lực học tập và thi cử
                - Khuyến khích tư duy sáng tạo
                - Chuẩn bị tốt hơn cho môi trường đại học
            ''',
            'tags': ['Giáo dục', 'Đại học', 'Thi cử', 'Cải cách', 'Học tập'],
            'images': [
                ('news/images/exam_image1.jpg', 'Học sinh ôn thi'),
                ('news/images/exam_image2.jpg', 'Phòng thi hiện đại')
            ]
        },
        {
            'title': 'Việt Nam Vô Địch AFF Cup 2024',
            'slug': 'viet-nam-vo-dich-aff-cup-2024',
            'category': Category.objects.get(name='Thể thao'),
            'thumbnail': 'news/thumbnails/aff_cup_2024.jpg',
            'content': '''
                Đội tuyển Việt Nam đã giành chức vô địch AFF Cup 2024 sau chiến thắng ấn tượng trước Thái Lan 
                trong trận chung kết tại sân vận động quốc gia Mỹ Đình.

                Trận đấu diễn ra căng thẳng và kịch tính, với những pha bóng đẹp mắt từ cả hai đội. 
                Đội trưởng Quế Ngọc Hải đã ghi bàn quyết định ở phút 85, 
                giúp Việt Nam lên ngôi vô địch lần thứ 3 trong lịch sử.

                Chiến thắng này không chỉ là niềm tự hào của người hâm mộ bóng đá Việt Nam, 
                mà còn khẳng định vị thế mới của bóng đá nước nhà trên đấu trường khu vực.
            ''',
            'tags': ['Thể thao', 'Bóng đá', 'Việt Nam', 'AFF Cup', 'Vô địch'],
            'images': [
                ('news/images/football_image1.jpg', 'Khoảnh khắc ăn mừng'),
                ('news/images/football_image2.jpg', 'Đội trưởng Quế Ngọc Hải ghi bàn')
            ]
        }
    ]

    for news_item in news_data:
        news = News.objects.create(
            title=news_item['title'],
            slug=news_item['slug'],
            category=news_item['category'],
        author=admin_user,
            thumbnail=news_item['thumbnail'],
            content=news_item['content'],
        status='published',
        published_at=timezone.now() - timedelta(days=4),
        views_count=150,
        is_featured=True
    )
        news.tags.add(*news_item['tags'])
        
        for image_path, caption in news_item['images']:
            NewsImage.objects.create(news=news, image=image_path, caption=caption)
        print(f"Created news: {news.title}")

    # Tạo categories cho khóa học
    course_categories = [
        {
            'name': 'Lập trình',
            'slug': 'lap-trinh',
            'description': 'Các khóa học về lập trình, phát triển phần mềm và công nghệ thông tin.'
        },
        {
            'name': 'Ngoại ngữ',
            'slug': 'ngoai-ngu',
            'description': 'Các khóa học ngoại ngữ cho mọi trình độ và mục đích học tập.'
        },
        {
            'name': 'Kỹ năng mềm',
            'slug': 'ky-nang-mem',
            'description': 'Các khóa học về kỹ năng mềm, giao tiếp và phát triển bản thân.'
        },
        {
            'name': 'Kinh doanh',
            'slug': 'kinh-doanh',
            'description': 'Các khóa học về kinh doanh, marketing và quản lý.'
        },
        {
            'name': 'Thiết kế',
            'slug': 'thiet-ke',
            'description': 'Các khóa học về thiết kế đồ họa, UI/UX và thiết kế web.'
        }
    ]

    for cat_data in course_categories:
        category, _ = CourseCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': cat_data['slug'],
                'description': cat_data['description']
            }
        )
        print(f"Created course category: {category.name}")

    # Tạo khóa học
    course_data = [
        {
            'title': 'Lập trình Python Cơ Bản',
            'slug': 'lap-trinh-python-co-ban',
            'category': CourseCategory.objects.get(name='Lập trình'),
            'thumbnail': 'courses/thumbnails/python_basic.jpg',
            'description': '''
                Khóa học Python cơ bản dành cho người mới bắt đầu, cung cấp nền tảng vững chắc về lập trình.
                
                Bạn sẽ học được:
                - Cú pháp cơ bản của Python
                - Các kiểu dữ liệu và cấu trúc dữ liệu
                - Lập trình hướng đối tượng
                - Xử lý file và dữ liệu
                - Làm việc với thư viện chuẩn
                
                Sau khi hoàn thành khóa học, bạn sẽ có thể:
                - Viết các chương trình Python cơ bản
                - Hiểu và sử dụng các khái niệm lập trình cơ bản
                - Chuẩn bị cho việc học các khóa nâng cao
            ''',
            'price': Decimal('500000.00'),
            'discount_price': Decimal('450000.00'),
            'duration': timedelta(hours=10),
            'lessons': [
                ('Giới thiệu về Python', '''
                    - Python là gì?
                    - Tại sao nên học Python?
                    - Cài đặt môi trường Python
                    - Chạy chương trình Python đầu tiên
                ''', 1, True, 'https://example.com/video1.mp4'),
                ('Cú pháp cơ bản', '''
                    - Biến và kiểu dữ liệu
                    - Toán tử
                    - Câu lệnh điều kiện
                    - Vòng lặp
                ''', 2, False, 'https://example.com/video2.mp4'),
                ('Cấu trúc dữ liệu', '''
                    - List và Tuple
                    - Dictionary
                    - Set
                    - String
                ''', 3, False, 'https://example.com/video3.mp4')
            ]
        },
        {
            'title': 'Tiếng Anh Giao Tiếp',
            'slug': 'tieng-anh-giao-tiep',
            'category': CourseCategory.objects.get(name='Ngoại ngữ'),
            'thumbnail': 'courses/thumbnails/english_communication.jpg',
            'description': '''
                Khóa học tiếng Anh giao tiếp giúp bạn tự tin trong giao tiếp hàng ngày và công việc.
                
                Nội dung khóa học:
                - Phát âm chuẩn
                - Từ vựng thông dụng
                - Ngữ pháp cơ bản
                - Kỹ năng nghe nói
                - Giao tiếp trong môi trường công sở
                
                Phương pháp học:
                - Học qua video
                - Thực hành với giáo viên bản ngữ
                - Bài tập thực tế
                - Kiểm tra định kỳ
            ''',
            'price': Decimal('600000.00'),
            'duration': timedelta(hours=15),
            'lessons': [
                ('Từ vựng cơ bản', '''
                    - Chào hỏi và giới thiệu
                    - Số đếm và thời gian
                    - Màu sắc và hình dạng
                    - Gia đình và bạn bè
                ''', 1, True, 'https://example.com/video3.mp4'),
                ('Ngữ pháp cơ bản', '''
                    - Thì hiện tại đơn
                    - Thì quá khứ đơn
                    - Thì tương lai đơn
                    - Câu bị động
                ''', 2, False, 'https://example.com/video4.mp4'),
                ('Kỹ năng nghe nói', '''
                    - Luyện nghe cơ bản
                    - Phát âm chuẩn
                    - Giao tiếp thường ngày
                    - Thực hành hội thoại
                ''', 3, False, 'https://example.com/video5.mp4')
            ]
        },
        {
            'title': 'Kỹ Năng Thuyết Trình',
            'slug': 'ky-nang-thuyet-trinh',
            'category': CourseCategory.objects.get(name='Kỹ năng mềm'),
            'thumbnail': 'courses/thumbnails/presentation_skills.jpg',
            'description': '''
                Khóa học kỹ năng thuyết trình giúp bạn tự tin và chuyên nghiệp khi trình bày trước đám đông.
                
                Bạn sẽ học được:
                - Kỹ thuật thuyết trình hiệu quả
                - Cách chuẩn bị nội dung
                - Kỹ năng sử dụng ngôn ngữ cơ thể
                - Xử lý câu hỏi và phản hồi
                - Sử dụng công cụ hỗ trợ
                
                Đặc biệt:
                - Thực hành trực tiếp
                - Nhận phản hồi từ chuyên gia
                - Tài liệu tham khảo đầy đủ
            ''',
            'price': Decimal('0.00'),
            'duration': timedelta(hours=5),
            'lessons': [
                ('Chuẩn bị bài thuyết trình', '''
                    - Xác định mục tiêu
                    - Phân tích đối tượng
                    - Thu thập thông tin
                    - Cấu trúc nội dung
                ''', 1, True, 'https://example.com/video5.mp4'),
                ('Kỹ thuật trình bày', '''
                    - Ngôn ngữ cơ thể
                    - Giọng nói và tốc độ
                    - Sử dụng ví dụ
                    - Tương tác với khán giả
                ''', 2, False, 'https://example.com/video6.mp4'),
                ('Xử lý tình huống', '''
                    - Trả lời câu hỏi
                    - Xử lý phản hồi
                    - Đối phó với sự cố
                    - Kết thúc ấn tượng
                ''', 3, False, 'https://example.com/video7.mp4')
            ]
        }
    ]

    for course_item in course_data:
        course = Course.objects.create(
            title=course_item['title'],
            slug=course_item['slug'],
            category=course_item['category'],
        instructor=admin_user,
            thumbnail=course_item['thumbnail'],
            description=course_item['description'],
            price=course_item['price'],
            discount_price=course_item.get('discount_price'),
            duration=course_item['duration'],
        status='published',
        published_at=timezone.now() - timedelta(days=9),
        enrollment_count=50,
            is_free=(course_item['price'] == Decimal('0.00')),
        is_featured=True
    )
        
        for title, content, order, is_preview, video_url in course_item['lessons']:
            Lesson.objects.create(
                course=course,
                title=title,
                content=content,
                duration=timedelta(hours=1),
                order=order,
                is_preview=is_preview,
                video_url=video_url
            )
        print(f"Created course: {course.title}")

    print("\nDữ liệu giả đã được tạo thành công!")

if __name__ == "__main__":
    populate_data()