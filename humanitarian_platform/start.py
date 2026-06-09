"""
🚀 مشغل منصة إدارة المشاريع الإنسانية
Humanitarian Projects Management Platform Launcher
"""

import os
import sys
import importlib.util

def main():
    """تشغيل المنصة"""
    print("=" * 50)
    print("🏠 منصة إدارة المشاريع الإنسانية")
    print("=" * 50)
    print("\n⏳ جاري تحميل المنصة...")
    
    try:
        # مسار مجلد src
        src_dir = os.path.join(os.path.dirname(__file__), "src")
        
        # إضافة مسار src إلى sys.path
        sys.path.insert(0, src_dir)
        
        # تحميل main_app مباشرة
        spec = importlib.util.spec_from_file_location(
            "main_app", 
            os.path.join(src_dir, "main_app.py")
        )
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        
        print("✅ تم تحميل جميع المكونات بنجاح!")
        print("\n" + "=" * 50)
        main_module.main()
        
    except ImportError as e:
        print(f"\n❌ خطأ في الاستيراد: {e}")
        print("\n📋 تأكد من تثبيت المكتبات المطلوبة:")
        print("   pip install tkcalendar")
        input("\nاضغط Enter للإغلاق...")
        
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        import traceback
        traceback.print_exc()
        input("\nاضغط Enter للإغلاق...")


if __name__ == "__main__":
    main()