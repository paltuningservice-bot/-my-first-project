"""
🚀 مشغل منصة إدارة المشاريع الإنسانية
Humanitarian Projects Management Platform Launcher
"""

import os
import sys

def main():
    """تشغيل المنصة"""
    print("=" * 50)
    print("🏠 منصة إدارة المشاريع الإنسانية")
    print("=" * 50)
    print("\n⏳ جاري تحميل المنصة...")
    
    try:
        # الانتقال إلى مجلد src
        src_dir = os.path.join(os.path.dirname(__file__), "src")
        os.chdir(src_dir)
        
        # تشغيل التطبيق الرئيسي
        from main_app import main
        print("✅ تم تحميل جميع المكونات بنجاح!")
        print("\n" + "=" * 50)
        main()
        
    except ImportError as e:
        print(f"\n❌ خطأ في الاستيراد: {e}")
        print("\n📋 تأكد من تثبيت المكتبات المطلوبة:")
        print("   pip install tkcalendar")
        input("\nاضغط Enter للإغلاق...")
        
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        input("\nاضغط Enter للإغلاق...")


if __name__ == "__main__":
    main()