import tkinter as tk
from tkinter import ttk

# دالة لحساب نتيجة العملية الحسابية
def calculate():
    try:
        expression = entry.get()  # جلب النص من مربع الإدخال
        result = eval(expression)  # WARNING: استخدام eval() خطر مع مدخلات غير موثوقة
        entry.delete(0, tk.END)  # مسح مربع الإدخال
        entry.insert(0, str(result))  # عرض النتيجة
    except (SyntaxError, NameError, TypeError, ZeroDivisionError): # معالجة الأخطاء
        entry.delete(0, tk.END)
        entry.insert(0, "Error") # عرض "Error" في حالة وجود خطأ

# دالة لإضافة الأرقام والعمليات إلى مربع الإدخال
def button_click(char):
    current = entry.get() # جلب النص الحالي في مربع الإدخال
    entry.delete(0, tk.END) # مسح مربع الإدخال
    entry.insert(0, current + str(char)) # إضافة الرقم أو العملية الجديدة

# دالة لمسح مربع الإدخال
def clear():
    entry.delete(0, tk.END)

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("Simple Calculator") # وضع عنوان للنافذة

# إنشاء مربع الإدخال
entry = ttk.Entry(root, width=25, font=("Arial", 16), justify="right") # تحديد حجم الخط ومحاذاة النص لليمين
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # وضع مربع الإدخال في النافذة باستخدام نظام grid

# تعريف أزرار الآلة الحاسبة
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

# إنشاء الأزرار ووضعها في النافذة
for button_text in buttons:
    if button_text == "=":
        ttk.Button(root, text=button_text, command=calculate, width=8).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        ttk.Button(root, text=button_text, command=lambda char=button_text: button_click(char), width=8).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# إنشاء زر المسح
clear_button = ttk.Button(root, text="C", command=clear, width=8)
clear_button.grid(row=5, column=0, padx=5, pady=5)


root.mainloop() # تشغيل البرنامج
