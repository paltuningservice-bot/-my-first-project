"""
🧮 الآلة الحاسبة - Simple Calculator
برنامج آلة حاسبة سهل الاستخدام
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ خطأ: القسمة على صفر!"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "❌ خطأ: لا يمكن أخذ الجذر التربيعي لعدد سالب!"
    return a ** 0.5

def percent(a, b):
    """نسبة b من a"""
    return (a * b) / 100


def calculator():
    """الآلة الحاسبة التفاعلية"""
    print("\n" + "="*50)
    print("🧮 الآلة الحاسبة")
    print("="*50)
    
    operations = {
        "1": ("جمع", add),
        "2": ("طرح", subtract),
        "3": ("ضرب", multiply),
        "4": ("قسمة", divide),
        "5": ("أس", power),
        "6": ("جذر تربيعي", sqrt),
        "7": ("نسبة مئوية", percent)
    }
    
    while True:
        print("\nاختر العملية:")
        print("1️⃣  جمع")
        print("2️⃣  طرح")
        print("3️⃣  ضرب")
        print("4️⃣  قسمة")
        print("5️⃣  أس (تربيع، تكعيب...)")
        print("6️⃣  جذر تربيعي")
        print("7️⃣  نسبة مئوية")
        print("8️⃣  الخروج")
        
        choice = input("\n👉 اختيارك: ")
        
        if choice == "8":
            print("\n👋 شكراً!")
            break
        
        if choice not in operations:
            print("❌ اختيار غير صحيح!")
            continue
        
        name, func = operations[choice]
        
        try:
            if choice == "6":  # sqrt
                a = float(input("العدد: "))
                result = func(a)
            elif choice == "7":  # percent
                a = float(input("العدد الكلي: "))
                b = float(input("النسبة %: "))
                result = func(a, b)
                print(f"\n📊 {b}% من {a} = {result}")
                continue
            else:
                a = float(input("العدد الأول: "))
                b = float(input("العدد الثاني: "))
                result = func(a, b)
            
            print(f"\n✅ النتيجة: {result}")
            
        except ValueError:
            print("❌ خطأ: أدخل رقماً صحيحاً!")


if __name__ == "__main__":
    calculator()