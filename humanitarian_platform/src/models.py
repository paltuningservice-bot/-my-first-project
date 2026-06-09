"""
📦 قاعدة البيانات - Database Models
نماذج البيانات لمنصة إدارة المشاريع الإنسانية
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from typing import List, Optional
import json
import uuid


def generate_id():
    """توليد معرف فريد"""
    return str(uuid.uuid4())[:8]


@dataclass
class Project:
    """نموذج المشروع"""
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: str = ""
    donor: str = ""  # الجهة المانحة
    budget: float = 0.0
    currency: str = "USD"
    start_date: str = ""
    end_date: str = ""
    status: str = "نشط"  # نشط، مكتمل، متوقف، ملغي
    location: str = ""  # الموقع الجغرافي
    target_beneficiaries: int = 0
    actual_beneficiaries: int = 0
    progress: float = 0.0  # نسبة الإنجاز
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    updated_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    created_by: str = ""
    milestones: List[dict] = field(default_factory=list)
    activities: List[str] = field(default_factory=list)  # قائمة معرفات الأنشطة
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Beneficiary:
    """نموذج المستفيد"""
    id: str = field(default_factory=generate_id)
    name: str = ""
    phone: str = ""
    gender: str = ""  # ذكر، أنثى
    age: int = 0
    category: str = ""  # الفئة المستهدفة
    area: str = ""  # المنطقة
    address: str = ""
    project_id: str = ""  # المشروع المسجل فيه
    registration_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    status: str = "نشط"
    notes: str = ""
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Activity:
    """نموذج النشاط"""
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: str = ""
    project_id: str = ""
    activity_type: str = ""  # نوع النشاط
    scheduled_date: str = ""
    completed_date: str = ""
    status: str = "مخطط"  # مخطط، جاري، مكتمل، متأخر
    location: str = ""
    target_count: int = 0
    actual_count: int = 0
    responsible: str = ""
    budget: float = 0.0
    indicators: List[dict] = field(default_factory=list)
    tasks: List[dict] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Indicator:
    """نموذج المؤشر"""
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: str = ""
    project_id: str = ""
    activity_id: str = ""
    indicator_type: str = ""  # إنتاجي، نتيجة، أثر
    baseline: float = 0.0  # القيمة الأساسية
    target: float = 0.0  # الهدف
    actual: float = 0.0  # الفعلي
    unit: str = ""  # الوحدة
    measurement_frequency: str = ""  # شهري، ربع سنوي، سنوي
    last_updated: str = ""
    
    def to_dict(self):
        return asdict(self)


@dataclass
class User:
    """نموذج المستخدم"""
    id: str = field(default_factory=generate_id)
    username: str = ""
    password: str = ""  # سيتم تشفيرها
    full_name: str = ""
    email: str = ""
    role: str = "مستخدم"  # مدير، مشرف، مستخدم
    permissions: List[str] = field(default_factory=list)
    status: str = "نشط"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    last_login: str = ""
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Document:
    """نموذج الوثيقة"""
    id: str = field(default_factory=generate_id)
    title: str = ""
    document_type: str = ""  # تقرير، عقد، صورة، ملف
    project_id: str = ""
    file_path: str = ""
    uploaded_by: str = ""
    upload_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    description: str = ""
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Financial:
    """نموذج البيانات المالية"""
    id: str = field(default_factory=generate_id)
    project_id: str = ""
    transaction_type: str = ""  # إيراد، مصروف
    amount: float = 0.0
    currency: str = "USD"
    description: str = ""
    date: str = ""
    receipt_number: str = ""
    recorded_by: str = ""
    attachment: str = ""
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Task:
    """نموذج المهمة"""
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: str = ""
    project_id: str = ""
    activity_id: str = ""
    assigned_to: str = ""
    status: str = "قيد الانتظار"  # قيد الانتظار، جاري، مكتمل
    priority: str = "متوسط"  # منخفض، متوسط، عالي، عاجل
    due_date: str = ""
    completed_date: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Notification:
    """نموذج التنبيه"""
    id: str = field(default_factory=generate_id)
    title: str = ""
    message: str = ""
    notification_type: str = ""  # تذكير، تنبيه، رسالة
    is_read: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))
    related_id: str = ""
    
    def to_dict(self):
        return asdict(self)


class Database:
    """فئة قاعدة البيانات"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.projects_file = f"{data_dir}/projects.json"
        self.beneficiaries_file = f"{data_dir}/beneficiaries.json"
        self.activities_file = f"{data_dir}/activities.json"
        self.indicators_file = f"{data_dir}/indicators.json"
        self.users_file = f"{data_dir}/users.json"
        self.documents_file = f"{data_dir}/documents.json"
        self.financial_file = f"{data_dir}/financial.json"
        self.tasks_file = f"{data_dir}/tasks.json"
        self.notifications_file = f"{data_dir}/notifications.json"
        self.settings_file = f"{data_dir}/settings.json"
        
    def _load_json(self, filepath, default=[]):
        """تحميل بيانات من ملف JSON"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return default
    
    def _save_json(self, filepath, data):
        """حفظ بيانات إلى ملف JSON"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    # المشاريع
    def get_projects(self):
        return self._load_json(self.projects_file)
    
    def save_project(self, project):
        projects = self.get_projects()
        projects.append(project.to_dict())
        self._save_json(self.projects_file, projects)
    
    def update_project(self, project_id, data):
        projects = self.get_projects()
        for i, p in enumerate(projects):
            if p['id'] == project_id:
                projects[i].update(data)
                projects[i]['updated_at'] = datetime.now().strftime("%Y-%m-%d")
                break
        self._save_json(self.projects_file, projects)
    
    def delete_project(self, project_id):
        projects = self.get_projects()
        projects = [p for p in projects if p['id'] != project_id]
        self._save_json(self.projects_file, projects)
    
    # المستفيدين
    def get_beneficiaries(self):
        return self._load_json(self.beneficiaries_file)
    
    def save_beneficiary(self, beneficiary):
        beneficiaries = self.get_beneficiaries()
        beneficiaries.append(beneficiary.to_dict())
        self._save_json(self.beneficiaries_file, beneficiaries)
    
    def update_beneficiary(self, beneficiary_id, data):
        beneficiaries = self.get_beneficiaries()
        for i, b in enumerate(beneficiaries):
            if b['id'] == beneficiary_id:
                beneficiaries[i].update(data)
                break
        self._save_json(self.beneficiaries_file, beneficiaries)
    
    def delete_beneficiary(self, beneficiary_id):
        beneficiaries = self.get_beneficiaries()
        beneficiaries = [b for b in beneficiaries if b['id'] != beneficiary_id]
        self._save_json(self.beneficiaries_file, beneficiaries)
    
    # الأنشطة
    def get_activities(self):
        return self._load_json(self.activities_file)
    
    def save_activity(self, activity):
        activities = self.get_activities()
        activities.append(activity.to_dict())
        self._save_json(self.activities_file, activities)
    
    def update_activity(self, activity_id, data):
        activities = self.get_activities()
        for i, a in enumerate(activities):
            if a['id'] == activity_id:
                activities[i].update(data)
                break
        self._save_json(self.activities_file, activities)
    
    # المستخدمون
    def get_users(self):
        return self._load_json(self.users_file)
    
    def save_user(self, user):
        users = self.get_users()
        users.append(user.to_dict())
        self._save_json(self.users_file, users)
    
    # المهام
    def get_tasks(self):
        return self._load_json(self.tasks_file)
    
    def save_task(self, task):
        tasks = self.get_tasks()
        tasks.append(task.to_dict())
        self._save_json(self.tasks_file, tasks)
    
    # الإعدادات
    def get_settings(self):
        return self._load_json(self.settings_file, {
            "language": "ar",
            "theme": "light",
            "currency": "USD",
            "organization_name": "منظمتك"
        })
    
    def save_settings(self, settings):
        self._save_json(self.settings_file, settings)
    
    # الإحصائيات
    def get_statistics(self):
        projects = self.get_projects()
        beneficiaries = self.get_beneficiaries()
        activities = self.get_activities()
        
        total_projects = len(projects)
        active_projects = len([p for p in projects if p.get('status') == 'نشط'])
        
        total_beneficiaries = len(beneficiaries)
        male_count = len([b for b in beneficiaries if b.get('gender') == 'ذكر'])
        female_count = len([b for b in beneficiaries if b.get('gender') == 'أنثى'])
        
        total_activities = len(activities)
        completed_activities = len([a for a in activities if a.get('status') == 'مكتمل'])
        
        # حساب متوسط الإنجاز
        total_progress = sum(p.get('progress', 0) for p in projects)
        avg_progress = total_progress / total_projects if total_projects > 0 else 0
        
        return {
            "total_projects": total_projects,
            "active_projects": active_projects,
            "total_beneficiaries": total_beneficiaries,
            "male_count": male_count,
            "female_count": female_count,
            "total_activities": total_activities,
            "completed_activities": completed_activities,
            "avg_progress": avg_progress
        }
    
    # النسخ الاحتياطي
    def create_backup(self, backup_dir="backups"):
        import shutil
        import os
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{backup_dir}/backup_{timestamp}"
        
        os.makedirs(backup_path, exist_ok=True)
        
        files = [
            self.projects_file,
            self.beneficiaries_file,
            self.activities_file,
            self.indicators_file,
            self.users_file,
            self.financial_file,
            self.tasks_file,
            self.settings_file
        ]
        
        for file in files:
            if os.path.exists(file):
                shutil.copy(file, backup_path)
        
        return backup_path