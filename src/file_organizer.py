"""
📁 منظم الملفات - File Organizer
برنامج لتنظيم الملفات في مجلدات حسب النوع
"""

import os
import shutil
from pathlib import Path


class FileOrganizer:
    """منظم الملفات - Organize your files automatically"""
    
    # أنواع الملفات وتصنيفاتها
    FILE_TYPES = {
        "صور": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "فيديو": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
        "صوت": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "مستندات": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "جداول": [".xlsx", ".xls", ".csv", ".ods"],
        "عروض": [".pptx", ".ppt", ".odp"],
        "أرشيف": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "برامج": [".exe", ".msi", ".dmg", ".app"],
        "كود": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"]
    }
    
    def __init__(self, source_folder):
        self.source_folder = Path(source_folder)
    
    def organize(self, create_subfolders=True):
        """تنظيم الملفات"""
        if not self.source_folder.exists():
            print(f"❌ المجلد غير موجود: {self.source_folder}")
            return
        
        print(f"\n📂 جاري تنظيم الملفات في: {self.source_folder}")
        print("="*50)
        
        for file in self.source_folder.iterdir():
            if file.is_file():
                ext = file.suffix.lower()
                category = self.get_category(ext)
                
                if category:
                    target_folder = self.source_folder / category
                    
                    if create_subfolders:
                        target_folder.mkdir(exist_ok=True)
                        new_path = target_folder / file.name
                    else:
                        new_path = self.source_folder / f"{category}_{file.name}"
                    
                    # نقل الملف
                    shutil.move(str(file), str(new_path))
                    print(f"  ✅ {file.name} → {category}/")
                else:
                    print(f"  ⚪ {file.name} → لم يتم تصنيفه")
        
        print("\n✅ تم الانتهاء من التنظيم!")
    
    def get_category(self, extension):
        """الحصول على فئة الملف"""
        for category, extensions in self.FILE_TYPES.items():
            if extension in extensions:
                return category
        return None
    
    def display_stats(self):
        """عرض إحصائيات المجلد"""
        stats = {}
        for file in self.source_folder.iterdir():
            if file.is_file():
                ext = file.suffix.lower()
                category = self.get_category(ext) or "أخرى"
                stats[category] = stats.get(category, 0) + 1
        
        print("\n📊 إحصائيات الملفات:")
        print("-"*30)
        for category, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {category}: {count} ملف")
        print(f"\n📁 المجموع: {sum(stats.values())} ملف")


def main():
    """الدالة الرئيسية"""
    print("\n" + "="*50)
    print("📁 منظم الملفات التلقائي")
    print("="*50)
    
    folder = input("\n📂 مسار المجلد للتنظيم: ").strip()
    
    if not folder:
        print("❌ يجب إدخال مسار المجلد")
        return
    
    organizer = FileOrganizer(folder)
    
    print("\nاختر:")
    print("1️⃣  تنظيم الملفات في مجلدات فرعية")
    print("2️⃣  إضافة بادئة للملفات (بدون مجلدات)")
    print("3️⃣  عرض الإحصائيات فقط")
    
    choice = input("\n👉 اختيارك: ")
    
    if choice == "1":
        organizer.organize(create_subfolders=True)
    elif choice == "2":
        organizer.organize(create_subfolders=False)
    elif choice == "3":
        organizer.display_stats()
    
    organizer.display_stats()


if __name__ == "__main__":
    main()