"""
🌟 مدير المشاريع - Project Manager
برنامج لإدارة المشاريع التقنية والإنسانية
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ProjectManager:
    """مدير المشاريع - Manage projects easily"""
    
    def __init__(self, data_file="projects_data.json"):
        self.data_file = data_file
        self.projects = self.load_projects()
    
    def load_projects(self):
        """تحميل المشاريع من الملف"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def save_projects(self):
        """حفظ المشاريع إلى الملف"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.projects, f, ensure_ascii=False, indent=2)
    
    def add_project(self, name, description, category, status="قيد التنفيذ"):
        """إضافة مشروع جديد"""
        project = {
            "id": len(self.projects) + 1,
            "name": name,
            "description": description,
            "category": category,
            "status": status,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "tasks": []
        }
        self.projects.append(project)
        self.save_projects()
        return project
    
    def add_task(self, project_id, task_name):
        """إضافة مهمة لمشروع"""
        for project in self.projects:
            if project["id"] == project_id:
                task = {
                    "id": len(project["tasks"]) + 1,
                    "name": task_name,
                    "completed": False,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                project["tasks"].append(task)
                self.save_projects()
                return task
        return None
    
    def complete_task(self, project_id, task_id):
        """إكمال مهمة"""
        for project in self.projects:
            if project["id"] == project_id:
                for task in project["tasks"]:
                    if task["id"] == task_id:
                        task["completed"] = True
                        self.save_projects()
                        return task
        return None
    
    def get_projects_by_category(self, category):
        """جلب المشاريع حسب الفئة"""
        return [p for p in self.projects if p["category"] == category]
    
    def display_all_projects(self):
        """عرض جميع المشاريع"""
        if not self.projects:
            print("\n📭 لا توجد مشاريع بعد!\n")
            return
        
        print("\n" + "="*60)
        print("📋 المشاريع المسجلة")
        print("="*60)
        
        for project in self.projects:
            completed_tasks = sum(1 for t in project["tasks"] if t["completed"])
            total_tasks = len(project["tasks"])
            progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
            
            print(f"\n🆔 #{project['id']} | {project['name']}")
            print(f"   📝 {project['description']}")
            print(f"   🏷️  الفئة: {project['category']}")
            print(f"   📊 الحالة: {project['status']}")
            print(f"   📈 التقدم: {progress:.0f}% ({completed_tasks}/{total_tasks} مهمة)")
            print("-"*60)


def main():
    """الدالة الرئيسية للبرنامج"""
    manager = ProjectManager()
    
    print("\n" + "="*60)
    print("🌟 مدير المشاريع التقنية والإنسانية 🌟")
    print("="*60)
    
    while True:
        print("\nاختر العملية:")
        print("1️⃣  إضافة مشروع جديد")
        print("2️⃣  إضافة مهمة لمشروع")
        print("3️⃣  إكمال مهمة")
        print("4️⃣  عرض جميع المشاريع")
        print("5️⃣  عرض المشاريع حسب الفئة")
        print("6️⃣  الخروج")
        
        choice = input("\n👉 اختيارك: ")
        
        if choice == "1":
            print("\n--- إضافة مشروع جديد ---")
            name = input("اسم المشروع: ")
            description = input("الوصف: ")
            print("الفئات المتاحة: تقنية، إنساني، تعليمي، صحي، آخر")
            category = input("الفئة: ")
            status = input("الحالة (افتراضي: قيد التنفيذ): ") or "قيد التنفيذ"
            manager.add_project(name, description, category, status)
            print("✅ تم إضافة المشروع بنجاح!")
            
        elif choice == "2":
            manager.display_all_projects()
            try:
                project_id = int(input("رقم المشروع: "))
                task_name = input("اسم المهمة: ")
                manager.add_task(project_id, task_name)
                print("✅ تم إضافة المهمة بنجاح!")
            except:
                print("❌ خطأ في البيانات")
                
        elif choice == "3":
            manager.display_all_projects()
            try:
                project_id = int(input("رقم المشروع: "))
                task_id = int(input("رقم المهمة: "))
                manager.complete_task(project_id, task_id)
                print("✅ تم إكمال المهمة!")
            except:
                print("❌ خطأ في البيانات")
                
        elif choice == "4":
            manager.display_all_projects()
            
        elif choice == "5":
            print("الفئات: تقنية، إنساني، تعليمي، صحي، آخر")
            category = input("الفئة: ")
            projects = manager.get_projects_by_category(category)
            print(f"\n📂 مشاريع الفئة '{category}': {len(projects)}")
            for p in projects:
                print(f"  - {p['name']}")
                
        elif choice == "6":
            print("\n👋 شكراً لاستخدام البرنامج!")
            break


if __name__ == "__main__":
    main()