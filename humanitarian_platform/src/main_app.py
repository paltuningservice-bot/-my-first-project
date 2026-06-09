"""
🏠 لوحة التحكم الرئيسية - Main Dashboard
منصة إدارة المشاريع الإنسانية
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import os
import json
from datetime import datetime

# استيراد النماذج
from models import Database, Project, Beneficiary, Activity, Indicator, Task, User, Document, Financial


class HumanitarianPlatform:
    """منصة إدارة المشاريع الإنسانية"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("منصة إدارة المشاريع الإنسانية")
        self.root.geometry("1400x800")
        self.root.state('zoomed')
        
        # تهيئة قاعدة البيانات
        self.db = Database(data_dir="data")
        self.current_language = "ar"
        
        # الألوان من التصميم
        self.colors = {
            "primary": "#1E6B54",
            "secondary": "#2FA36B",
            "accent1": "#F7C948",
            "accent2": "#F64E60",
            "white": "#FFFFFF",
            "dark": "#2D3436",
            "gray": "#636E72",
            "light_gray": "#DFE6E9",
            "success": "#00B894",
            "warning": "#FDCB6E",
            "danger": "#E17055"
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        """إعداد واجهة المستخدم"""
        # إطار رئيسي
        main_frame = tk.Frame(self.root, bg=self.colors["white"])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # القائمة الجانبية
        self.create_sidebar(main_frame)
        
        # القسم الرئيسي
        self.create_main_content(main_frame)
        
    def create_sidebar(self, parent):
        """إنشاء القائمة الجانبية"""
        # إطار القائمة الجانبية
        sidebar = tk.Frame(parent, bg=self.colors["primary"], width=250)
        sidebar.pack(side=tk.RIGHT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        # عنوان المنصة
        title_frame = tk.Frame(sidebar, bg=self.colors["primary"])
        title_frame.pack(fill=tk.X, pady=(20, 30))
        
        tk.Label(
            title_frame,
            text="🌟 منصة المشاريع",
            font=("Tajawal", 18, "bold"),
            fg=self.colors["white"],
            bg=self.colors["primary"]
        ).pack(pady=10)
        
        tk.Label(
            title_frame,
            text="الإنسانية",
            font=("Tajawal", 14),
            fg=self.colors["white"],
            bg=self.colors["primary"]
        ).pack()
        
        # القائمة
        menu_items = [
            ("🏠", "لوحة التحكم", self.show_dashboard),
            ("📁", "إدارة المشاريع", self.show_projects),
            ("👥", "إدارة المستفيدين", self.show_beneficiaries),
            ("📅", "الأنشطة والفعاليات", self.show_activities),
            ("📊", "المؤشرات والمتابعة", self.show_indicators),
            ("📋", "التقارير", self.show_reports),
            ("📄", "إدارة الوثائق", self.show_documents),
            ("🔗", "الإحالات والحالات", self.show_referrals),
            ("💰", "إدارة المالية", self.show_financial),
            ("👤", "المستخدمون", self.show_users),
            ("⚙️", "الإعدادات", self.show_settings)
        ]
        
        for icon, text, command in menu_items:
            btn = tk.Button(
                sidebar,
                text=f"  {icon}  {text}",
                font=("Tajawal", 12),
                fg=self.colors["white"],
                bg=self.colors["primary"],
                activebackground=self.colors["secondary"],
                activeforeground=self.colors["white"],
                relief=tk.FLAT,
                anchor=tk.RIGHT,
                padx=20,
                pady=12,
                command=command
            )
            btn.pack(fill=tk.X, padx=10, pady=2)
            
    def create_main_content(self, parent):
        """إنشاء المحتوى الرئيسي"""
        # إطار المحتوى
        self.content_frame = tk.Frame(parent, bg=self.colors["white"])
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # شريط البحث العلوي
        self.create_header()
        
        # منطقة المحتوى
        self.content_area = tk.Frame(self.content_frame, bg=self.colors["white"])
        self.content_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # إظهار لوحة التحكم
        self.show_dashboard()
        
    def create_header(self):
        """إنشاء شريط البحث العلوي"""
        header = tk.Frame(self.content_frame, bg=self.colors["white"], height=60)
        header.pack(fill=tk.X, padx=20, pady=(10, 0))
        header.pack_propagate(False)
        
        # شريط البحث
        search_frame = tk.Frame(header, bg=self.colors["light_gray"], bd=0)
        search_frame.pack(side=tk.RIGHT, pady=10)
        
        self.search_entry = tk.Entry(
            search_frame,
            font=("Tajawal", 12),
            width=40,
            bd=0,
            bg=self.colors["light_gray"],
            fg=self.colors["gray"]
        )
        self.search_entry.pack(side=tk.RIGHT, padx=10, pady=8)
        self.search_entry.insert(0, "🔍 ابحث في النظام...")
        
        # معلومات المستخدم
        user_frame = tk.Frame(header, bg=self.colors["white"])
        user_frame.pack(side=tk.LEFT, pady=10)
        
        tk.Label(
            user_frame,
            text="👤 مدير النظام",
            font=("Tajawal", 11),
            fg=self.colors["gray"]
        ).pack(side=tk.RIGHT, padx=10)
        
        tk.Label(
            user_frame,
            text="📅 " + datetime.now().strftime("%Y-%m-%d"),
            font=("Tajawal", 11),
            fg=self.colors["gray"]
        ).pack(side=tk.LEFT, padx=10)
        
    def clear_content(self):
        """مسح المحتوى الحالي"""
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
    def show_dashboard(self):
        """عرض لوحة التحكم"""
        self.clear_content()
        
        # العنوان
        title = tk.Label(
            self.content_area,
            text="📊 لوحة التحكم",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        )
        title.pack(anchor=tk.W, pady=(0, 20))
        
        # إحصائيات سريعة
        stats = self.db.get_statistics()
        
        stats_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # بطاقات الإحصائيات
        cards_data = [
            ("📁", "إجمالي المشاريع", stats["total_projects"], self.colors["primary"]),
            ("👥", "إجمالي المستفيدين", stats["total_beneficiaries"], self.colors["secondary"]),
            ("📅", "إجمالي الأنشطة", stats["total_activities"], self.colors["accent1"]),
            ("📈", "متوسط الإنجاز", f"{stats['avg_progress']:.1f}%", self.colors["accent2"])
        ]
        
        for icon, title, value, color in cards_data:
            card = tk.Frame(stats_frame, bg=color, bd=0, relief=tk.RIDGE)
            card.pack(side=tk.LEFT, padx=10, pady=5)
            
            tk.Label(
                card,
                text=f"{icon} {title}",
                font=("Tajawal", 12),
                fg=self.colors["white"],
                bg=color
            ).pack(padx=20, pady=(15, 5))
            
            tk.Label(
                card,
                text=str(value),
                font=("Tajawal", 28, "bold"),
                fg=self.colors["white"],
                bg=color
            ).pack(padx=20, pady=(0, 15))
        
        # جداول البيانات
        tables_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        tables_frame.pack(fill=tk.BOTH, expand=True)
        
        # جدول المشاريع
        projects_table = self.create_table(
            tables_frame,
            "📁 أحدث المشاريع",
            ["الاسم", "الجهة المانحة", "الميزانية", "الحالة", "تاريخ البداية"],
            self.db.get_projects()[:5]
        )
        projects_table.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # جدول المستفيدين
        beneficiaries_table = self.create_table(
            tables_frame,
            "👥 أحدث المستفيدين",
            ["الاسم", "رقم الهاتف", "الفئة", "المنطقة", "تاريخ التسجيل"],
            self.db.get_beneficiaries()[:5]
        )
        beneficiaries_table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    def create_table(self, parent, title, columns, data):
        """إنشاء جدول"""
        table_frame = tk.LabelFrame(
            parent,
            text=title,
            font=("Tajawal", 14, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"],
            padx=10,
            pady=10
        )
        
        # الجدول
        columns_count = len(columns)
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=5)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor=tk.CENTER)
        
        for row in data:
            values = []
            for key in columns:
                # استخراج البيانات حسب اسم العمود
                if "الاسم" in key:
                    values.append(row.get('name', ''))
                elif "الجهة" in key:
                    values.append(row.get('donor', ''))
                elif "الميزانية" in key:
                    values.append(f"{row.get('budget', 0):,.0f}")
                elif "الحالة" in key:
                    values.append(row.get('status', ''))
                elif "البداية" in key or "التسجيل" in key:
                    values.append(row.get('start_date', '') or row.get('registration_date', ''))
                elif "الهاتف" in key:
                    values.append(row.get('phone', ''))
                elif "الفئة" in key:
                    values.append(row.get('category', ''))
                elif "المنطقة" in key:
                    values.append(row.get('area', ''))
                else:
                    values.append('')
            tree.insert('', tk.END, values=values)
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # زر عرض الكل
        btn_frame = tk.Frame(table_frame, bg=self.colors["white"])
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(
            btn_frame,
            text="عرض الكل →",
            font=("Tajawal", 10),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=20,
            pady=5
        ).pack(side=tk.RIGHT)
        
        return table_frame
        
    def show_projects(self):
        """عرض إدارة المشاريع"""
        self.clear_content()
        
        # العنوان والأزرار
        title_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            title_frame,
            text="📁 إدارة المشاريع",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(side=tk.RIGHT)
        
        tk.Button(
            title_frame,
            text="➕ إضافة مشروع جديد",
            font=("Tajawal", 11),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=20,
            pady=8,
            command=self.add_project_dialog
        ).pack(side=tk.LEFT)
        
        # البحث والتصفية
        filter_frame = tk.Frame(self.content_area, bg=self.colors["light_gray"], padx=10, pady=10)
        filter_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(filter_frame, text="فلترة:", font=("Tajawal", 11), bg=self.colors["light_gray"]).pack(side=tk.RIGHT, padx=(0, 10))
        
        status_combo = ttk.Combobox(
            filter_frame,
            values=["الكل", "نشط", "مكتمل", "متوقف"],
            font=("Tajawal", 10),
            width=15
        )
        status_combo.current(0)
        status_combo.pack(side=tk.RIGHT, padx=10)
        
        # جدول المشاريع
        projects = self.db.get_projects()
        
        if not projects:
            tk.Label(
                self.content_area,
                text="📭 لا توجد مشاريع مسجلة",
                font=("Tajawal", 16),
                fg=self.colors["gray"],
                bg=self.colors["white"]
            ).pack(pady=50)
            return
            
        columns = ["الاسم", "الجهة المانحة", "الميزانية", "الحالة", "تاريخ البداية", "نسبة الإنجاز"]
        tree = ttk.Treeview(
            self.content_area,
            columns=columns,
            show='headings'
        )
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130, anchor=tk.CENTER)
        
        for project in projects:
            tree.insert('', tk.END, values=[
                project.get('name', ''),
                project.get('donor', ''),
                f"{project.get('budget', 0):,.0f}",
                project.get('status', ''),
                project.get('start_date', ''),
                f"{project.get('progress', 0):.1f}%"
            ])
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # أزرار الإجراءات
        actions_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        actions_frame.pack(fill=tk.X, pady=(20, 0))
        
        tk.Button(
            actions_frame,
            text="✏️ تعديل",
            font=("Tajawal", 10),
            bg=self.colors["secondary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=15,
            pady=5
        ).pack(side=tk.RIGHT, padx=5)
        
        tk.Button(
            actions_frame,
            text="🗑️ حذف",
            font=("Tajawal", 10),
            bg=self.colors["accent2"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=15,
            pady=5
        ).pack(side=tk.RIGHT, padx=5)
        
    def add_project_dialog(self):
        """نافذة إضافة مشروع جديد"""
        dialog = tk.Toplevel(self.root)
        dialog.title("إضافة مشروع جديد")
        dialog.geometry("600x700")
        dialog.resizable(False, False)
        
        # جعل النافذة مركزية
        dialog.transient(self.root)
        dialog.grab_set()
        
        # العنوان
        tk.Label(
            dialog,
            text="➕ إضافة مشروع جديد",
            font=("Tajawal", 18, "bold"),
            fg=self.colors["primary"]
        ).pack(pady=20)
        
        # حقول الإدخال
        fields = [
            ("اسم المشروع:", 0),
            ("الوصف:", 1),
            ("الجهة المانحة:", 2),
            ("الميزانية:", 3),
            ("الموقع:", 4),
            ("تاريخ البداية:", 5),
            ("تاريخ النهاية:", 6)
        ]
        
        entries = {}
        for label, row in fields:
            tk.Label(dialog, text=label, font=("Tajawal", 11)).pack(pady=(10, 0))
            entry = tk.Entry(dialog, font=("Tajawal", 11), width=50)
            entry.pack(pady=(5, 0))
            entries[label] = entry
        
        # الحالة
        tk.Label(dialog, text="الحالة:", font=("Tajawal", 11)).pack(pady=(10, 0))
        status_combo = ttk.Combobox(
            dialog,
            values=["نشط", "مكتمل", "متوقف", "ملغي"],
            font=("Tajawal", 11),
            width=47
        )
        status_combo.current(0)
        status_combo.pack(pady=(5, 0))
        
        # أزرار
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="حفظ",
            font=("Tajawal", 12),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=lambda: self.save_project(entries, status_combo.get(), dialog)
        ).pack(side=tk.RIGHT, padx=10)
        
        tk.Button(
            btn_frame,
            text="إلغاء",
            font=("Tajawal", 12),
            bg=self.colors["gray"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=dialog.destroy
        ).pack(side=tk.RIGHT, padx=10)
        
    def save_project(self, entries, status, dialog):
        """حفظ المشروع"""
        project = Project(
            name=entries["اسم المشروع:"].get(),
            description=entries["الوصف:"].get(),
            donor=entries["الجهة المانحة:"].get(),
            budget=float(entries["الميزانية:"].get() or 0),
            location=entries["الموقع:"].get(),
            start_date=entries["تاريخ البداية:"].get(),
            end_date=entries["تاريخ النهاية:"].get(),
            status=status
        )
        
        self.db.save_project(project)
        messagebox.showinfo("نجاح", "✅ تم حفظ المشروع بنجاح!")
        dialog.destroy()
        self.show_projects()
        
    def show_beneficiaries(self):
        """عرض إدارة المستفيدين"""
        self.clear_content()
        
        title_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            title_frame,
            text="👥 إدارة المستفيدين",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(side=tk.RIGHT)
        
        tk.Button(
            title_frame,
            text="➕ إضافة مستفيد جديد",
            font=("Tajawal", 11),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=20,
            pady=8,
            command=self.add_beneficiary_dialog
        ).pack(side=tk.LEFT)
        
        # إحصائيات المستفيدين
        stats = self.db.get_statistics()
        stats_frame = tk.Frame(self.content_area, bg=self.colors["light_gray"], padx=20, pady=15)
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            stats_frame,
            text=f"👨 عدد الذكور: {stats['male_count']}",
            font=("Tajawal", 12),
            bg=self.colors["light_gray"]
        ).pack(side=tk.RIGHT, padx=30)
        
        tk.Label(
            stats_frame,
            text=f"👩 عدد الإناث: {stats['female_count']}",
            font=("Tajawal", 12),
            bg=self.colors["light_gray"]
        ).pack(side=tk.RIGHT, padx=30)
        
        # جدول المستفيدين
        beneficiaries = self.db.get_beneficiaries()
        
        if not beneficiaries:
            tk.Label(
                self.content_area,
                text="📭 لا توجد مستفيدين مسجلين",
                font=("Tajawal", 16),
                fg=self.colors["gray"],
                bg=self.colors["white"]
            ).pack(pady=50)
            return
            
        columns = ["الاسم", "رقم الهاتف", "الجنس", "الفئة", "المنطقة", "تاريخ التسجيل"]
        tree = ttk.Treeview(
            self.content_area,
            columns=columns,
            show='headings'
        )
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor=tk.CENTER)
        
        for b in beneficiaries:
            tree.insert('', tk.END, values=[
                b.get('name', ''),
                b.get('phone', ''),
                b.get('gender', ''),
                b.get('category', ''),
                b.get('area', ''),
                b.get('registration_date', '')
            ])
        
        tree.pack(fill=tk.BOTH, expand=True)
        
    def add_beneficiary_dialog(self):
        """نافذة إضافة مستفيد جديد"""
        dialog = tk.Toplevel(self.root)
        dialog.title("إضافة مستفيد جديد")
        dialog.geometry("600x600")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="👥 إضافة مستفيد جديد",
            font=("Tajawal", 18, "bold"),
            fg=self.colors["primary"]
        ).pack(pady=20)
        
        fields = [
            ("الاسم الكامل:", 0),
            ("رقم الهاتف:", 1),
            ("العمر:", 2),
            ("المنطقة:", 3),
            ("العنوان:", 4)
        ]
        
        entries = {}
        for label, row in fields:
            tk.Label(dialog, text=label, font=("Tajawal", 11)).pack(pady=(10, 0))
            entry = tk.Entry(dialog, font=("Tajawal", 11), width=50)
            entry.pack(pady=(5, 0))
            entries[label] = entry
        
        tk.Label(dialog, text="الجنس:", font=("Tajawal", 11)).pack(pady=(10, 0))
        gender_combo = ttk.Combobox(
            dialog,
            values=["ذكر", "أنثى"],
            font=("Tajawal", 11),
            width=47
        )
        gender_combo.pack(pady=(5, 0))
        
        tk.Label(dialog, text="الفئة المستهدفة:", font=("Tajawal", 11)).pack(pady=(10, 0))
        category_entry = tk.Entry(dialog, font=("Tajawal", 11), width=50)
        category_entry.pack(pady=(5, 0))
        
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="حفظ",
            font=("Tajawal", 12),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=lambda: self.save_beneficiary(entries, gender_combo.get(), category_entry.get(), dialog)
        ).pack(side=tk.RIGHT, padx=10)
        
        tk.Button(
            btn_frame,
            text="إلغاء",
            font=("Tajawal", 12),
            bg=self.colors["gray"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=dialog.destroy
        ).pack(side=tk.RIGHT, padx=10)
        
    def save_beneficiary(self, entries, gender, category, dialog):
        """حفظ المستفيد"""
        beneficiary = Beneficiary(
            name=entries["الاسم الكامل:"].get(),
            phone=entries["رقم الهاتف:"].get(),
            age=int(entries["العمر:"].get() or 0),
            gender=gender,
            category=category,
            area=entries["المنطقة:"].get(),
            address=entries["العنوان:"].get()
        )
        
        self.db.save_beneficiary(beneficiary)
        messagebox.showinfo("نجاح", "✅ تم حفظ المستفيد بنجاح!")
        dialog.destroy()
        self.show_beneficiaries()
        
    def show_activities(self):
        """عرض إدارة الأنشطة"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="📅 إدارة الأنشطة والفعاليات",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Button(
            self.content_area,
            text="➕ إضافة نشاط جديد",
            font=("Tajawal", 11),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=20,
            pady=8,
            command=self.add_activity_dialog
        ).pack(anchor=tk.E, pady=(0, 20))
        
        activities = self.db.get_activities()
        
        if not activities:
            tk.Label(
                self.content_area,
                text="📭 لا توجد أنشطة مسجلة",
                font=("Tajawal", 16),
                fg=self.colors["gray"],
                bg=self.colors["white"]
            ).pack(pady=50)
            return
            
        columns = ["الاسم", "النوع", "المشروع", "التاريخ", "الحالة", "الموقع"]
        tree = ttk.Treeview(
            self.content_area,
            columns=columns,
            show='headings'
        )
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130, anchor=tk.CENTER)
        
        for a in activities:
            tree.insert('', tk.END, values=[
                a.get('name', ''),
                a.get('activity_type', ''),
                a.get('project_id', ''),
                a.get('scheduled_date', ''),
                a.get('status', ''),
                a.get('location', '')
            ])
        
        tree.pack(fill=tk.BOTH, expand=True)
        
    def add_activity_dialog(self):
        """نافذة إضافة نشاط جديد"""
        dialog = tk.Toplevel(self.root)
        dialog.title("إضافة نشاط جديد")
        dialog.geometry("600x550")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="📅 إضافة نشاط جديد",
            font=("Tajawal", 18, "bold"),
            fg=self.colors["primary"]
        ).pack(pady=20)
        
        fields = [
            ("اسم النشاط:", 0),
            ("الوصف:", 1),
            ("الموقع:", 2),
            ("التاريخ المجدول:", 3),
            ("الهدف:", 4)
        ]
        
        entries = {}
        for label, row in fields:
            tk.Label(dialog, text=label, font=("Tajawal", 11)).pack(pady=(10, 0))
            entry = tk.Entry(dialog, font=("Tajawal", 11), width=50)
            entry.pack(pady=(5, 0))
            entries[label] = entry
        
        tk.Label(dialog, text="نوع النشاط:", font=("Tajawal", 11)).pack(pady=(10, 0))
        type_combo = ttk.Combobox(
            dialog,
            values=["تدريب", "ورشة عمل", "متابعة", "تقييم", "فعالية"],
            font=("Tajawal", 11),
            width=47
        )
        type_combo.pack(pady=(5, 0))
        
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="حفظ",
            font=("Tajawal", 12),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=lambda: self.save_activity(entries, type_combo.get(), dialog)
        ).pack(side=tk.RIGHT, padx=10)
        
        tk.Button(
            btn_frame,
            text="إلغاء",
            font=("Tajawal", 12),
            bg=self.colors["gray"],
            fg=self.colors["white"],
            padx=30,
            pady=5,
            command=dialog.destroy
        ).pack(side=tk.RIGHT, padx=10)
        
    def save_activity(self, entries, activity_type, dialog):
        """حفظ النشاط"""
        activity = Activity(
            name=entries["اسم النشاط:"].get(),
            description=entries["الوصف:"].get(),
            activity_type=activity_type,
            location=entries["الموقع:"].get(),
            scheduled_date=entries["التاريخ المجدول:"].get(),
            target_count=int(entries["الهدف:"].get() or 0),
            status="مخطط"
        )
        
        self.db.save_activity(activity)
        messagebox.showinfo("نجاح", "✅ تم حفظ النشاط بنجاح!")
        dialog.destroy()
        self.show_activities()
        
    def show_indicators(self):
        """عرض المؤشرات والمتابعة"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="📊 المؤشرات والمتابعة",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Label(
            self.content_area,
            text="📈 وحدة تتبع المؤشرات والنتائج قيد التطوير...",
            font=("Tajawal", 14),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=50)
        
    def show_reports(self):
        """عرض التقارير"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="📋 التقارير",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        # أزرار التقارير
        reports_frame = tk.Frame(self.content_area, bg=self.colors["white"])
        reports_frame.pack(fill=tk.BOTH, expand=True)
        
        reports = [
            ("📊", "تقرير تقدم المشاريع", self.colors["primary"]),
            ("💰", "التقرير المالي", self.colors["secondary"]),
            ("📈", "تقرير تقييم الأداء", self.colors["accent1"]),
            ("👥", "تقرير المستفيدين", self.colors["accent2"]),
            ("📅", "تقرير الأنشطة المنفذة", self.colors["primary"]),
            ("🎯", "تقرير الإنجازات", self.colors["secondary"])
        ]
        
        for icon, title, color in reports:
            btn = tk.Frame(reports_frame, bg=color, bd=0, cursor="hand2")
            btn.pack(pady=10, padx=20, fill=tk.X)
            
            tk.Label(
                btn,
                text=f"{icon} {title}",
                font=("Tajawal", 14),
                fg=self.colors["white"],
                bg=color,
                padx=20,
                pady=15
            ).pack(fill=tk.X)
            
    def show_documents(self):
        """عرض إدارة الوثائق"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="📄 إدارة الوثائق",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Label(
            self.content_area,
            text="📁 وحدة إدارة الوثائق قيد التطوير...",
            font=("Tajawal", 14),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=50)
        
    def show_referrals(self):
        """عرض الإحالات والحالات"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="🔗 الإحالات والحالات",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Label(
            self.content_area,
            text="🔗 وحدة الإحالات والحالات قيد التطوير...",
            font=("Tajawal", 14),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=50)
        
    def show_financial(self):
        """عرض إدارة المالية"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="💰 إدارة المالية",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Label(
            self.content_area,
            text="💰 وحدة إدارة المالية قيد التطوير...",
            font=("Tajawal", 14),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=50)
        
    def show_users(self):
        """عرض إدارة المستخدمين"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="👤 المستخدمون والصلاحيات",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        tk.Button(
            self.content_area,
            text="➕ إضافة مستخدم جديد",
            font=("Tajawal", 11),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(anchor=tk.E, pady=(0, 20))
        
        tk.Label(
            self.content_area,
            text="👤 إدارة المستخدمين والصلاحيات قيد التطوير...",
            font=("Tajawal", 14),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=50)
        
    def show_settings(self):
        """عرض الإعدادات"""
        self.clear_content()
        
        tk.Label(
            self.content_area,
            text="⚙️ الإعدادات",
            font=("Tajawal", 24, "bold"),
            fg=self.colors["dark"],
            bg=self.colors["white"]
        ).pack(anchor=tk.W, pady=(0, 20))
        
        # إعدادات اللغة
        lang_frame = tk.LabelFrame(
            self.content_area,
            text="🌐 إعدادات اللغة",
            font=("Tajawal", 14),
            fg=self.colors["dark"],
            bg=self.colors["white"],
            padx=20,
            pady=15
        )
        lang_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(lang_frame, text="اللغة:", font=("Tajawal", 12), bg=self.colors["white"]).pack(side=tk.RIGHT, padx=(0, 10))
        
        lang_combo = ttk.Combobox(
            lang_frame,
            values=["العربية", "English"],
            font=("Tajawal", 12),
            width=20
        )
        lang_combo.current(0)
        lang_combo.pack(side=tk.RIGHT)
        
        # إعدادات النسخ الاحتياطي
        backup_frame = tk.LabelFrame(
            self.content_area,
            text="💾 النسخ الاحتياطي",
            font=("Tajawal", 14),
            fg=self.colors["dark"],
            bg=self.colors["white"],
            padx=20,
            pady=15
        )
        backup_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            backup_frame,
            text="إنشاء نسخة احتياطية من جميع البيانات:",
            font=("Tajawal", 12),
            bg=self.colors["white"]
        ).pack(side=tk.RIGHT, padx=(0, 10))
        
        tk.Button(
            backup_frame,
            text="💾 إنشاء نسخة احتياطية",
            font=("Tajawal", 11),
            bg=self.colors["primary"],
            fg=self.colors["white"],
            relief=tk.FLAT,
            padx=15,
            pady=5,
            command=self.create_backup
        ).pack(side=tk.LEFT)
        
    def create_backup(self):
        """إنشاء نسخة احتياطية"""
        try:
            backup_path = self.db.create_backup()
            messagebox.showinfo("نجاح", f"✅ تم إنشاء النسخة الاحتياطية في:\n{backup_path}")
        except Exception as e:
            messagebox.showerror("خطأ", f"❌ حدث خطأ: {str(e)}")


def main():
    """الدالة الرئيسية"""
    root = tk.Tk()
    app = HumanitarianPlatform(root)
    root.mainloop()


if __name__ == "__main__":
    main()