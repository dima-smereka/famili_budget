import tkinter as tk
from tkinter import messagebox, filedialog
import json

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сімейний Бюджет")

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Місяць/рік
        tk.Label(self.main_frame, text="Місяць/Рік", font=('Helvetica', 14, 'bold')).grid(row=0, column=0, pady=10, sticky='w')
        tk.Label(self.main_frame, text="Місяць:").grid(row=1, column=0, sticky='w')
        self.month = tk.Entry(self.main_frame)
        self.month.grid(row=1, column=1, padx=10)

        tk.Label(self.main_frame, text="Рік:").grid(row=2, column=0, sticky='w')
        self.year = tk.Entry(self.main_frame)
        self.year.grid(row=2, column=1, padx=10)

        # Доходи
        tk.Label(self.main_frame, text="Доходи", font=('Helvetica', 14, 'bold')).grid(row=3, column=0, pady=10, sticky='w')
        tk.Label(self.main_frame, text="Зарплата чоловіка:").grid(row=4, column=0, sticky='w')
        self.salary_husband = tk.Entry(self.main_frame)
        self.salary_husband.grid(row=4, column=1, padx=10)

        tk.Label(self.main_frame, text="Зарплата дружини:").grid(row=5, column=0, sticky='w')
        self.salary_wife = tk.Entry(self.main_frame)
        self.salary_wife.grid(row=5, column=1, padx=10)

        tk.Label(self.main_frame, text="Допомога на дітей:").grid(row=6, column=0, sticky='w')
        self.child_support = tk.Entry(self.main_frame)
        self.child_support.grid(row=6, column=1, padx=10)

        # Витрати
        tk.Label(self.main_frame, text="Витрати", font=('Helvetica', 14, 'bold')).grid(row=7, column=0, pady=10, sticky='w')
        tk.Label(self.main_frame, text="Оренда квартири:").grid(row=8, column=0, sticky='w')
        self.rent = tk.Entry(self.main_frame)
        self.rent.grid(row=8, column=1, padx=10)

        tk.Label(self.main_frame, text="Оплата кредитів:").grid(row=9, column=0, sticky='w')
        self.loans = tk.Entry(self.main_frame)
        self.loans.grid(row=9, column=1, padx=10)

        tk.Label(self.main_frame, text="Оплата навчання дочки:").grid(row=10, column=0, sticky='w')
        self.education = tk.Entry(self.main_frame)
        self.education.grid(row=10, column=1, padx=10)

        tk.Label(self.main_frame, text="Витрати на їжу:").grid(row=11, column=0, sticky='w')
        self.food = tk.Entry(self.main_frame)
        self.food.grid(row=11, column=1, padx=10)

        tk.Label(self.main_frame, text="Оплата податків та мед. страхування:").grid(row=12, column=0, sticky='w')
        self.taxes_insurance = tk.Entry(self.main_frame)
        self.taxes_insurance.grid(row=12, column=1, padx=10)

        tk.Label(self.main_frame, text="Додаткові витрати:").grid(row=13, column=0, sticky='w')
        self.additional_expenses = tk.Entry(self.main_frame)
        self.additional_expenses.grid(row=13, column=1, padx=10)

        tk.Label(self.main_frame, text="Витрати на автомобіль:").grid(row=14, column=0, sticky='w')
        self.car_expenses = tk.Entry(self.main_frame)
        self.car_expenses.grid(row=14, column=1, padx=10)

        # Заощадження
        tk.Label(self.main_frame, text="Заощадження", font=('Helvetica', 14, 'bold')).grid(row=15, column=0, pady=10, sticky='w')
        tk.Label(self.main_frame, text="Планові заощадження:").grid(row=16, column=0, sticky='w')
        self.planned_savings = tk.Entry(self.main_frame)
        self.planned_savings.grid(row=16, column=1, padx=10)

        tk.Label(self.main_frame, text="Фактичні заощадження:").grid(row=17, column=0, sticky='w')
        self.savings_entry = tk.Entry(self.main_frame)
        self.savings_entry.grid(row=17, column=1, padx=10)

        # Buttons
        self.calculate_button = tk.Button(self.main_frame, text="Розрахувати", command=self.calculate)
        self.calculate_button.grid(row=18, column=0, pady=10)

        self.save_button = tk.Button(self.main_frame, text="Зберегти", command=self.save_data)
        self.save_button.grid(row=18, column=1, pady=10)

        self.load_button = tk.Button(self.main_frame, text="Завантажити", command=self.load_data)
        self.load_button.grid(row=18, column=2, pady=10)

        self.result_label = tk.Label(self.main_frame, text="")
        self.result_label.grid(row=19, column=0, columnspan=3, pady=10)

    def calculate(self):
        try:
            income = float(self.salary_husband.get() or 0) + float(self.salary_wife.get() or 0) + float(self.child_support.get() or 0)
            expenses = (float(self.rent.get() or 0) + float(self.loans.get() or 0) + float(self.education.get() or 0) +
                        float(self.food.get() or 0) + float(self.taxes_insurance.get() or 0) + float(self.additional_expenses.get() or 0) +
                        float(self.car_expenses.get() or 0))
            planned_savings = float(self.planned_savings.get() or 0)
            actual_savings = float(self.savings_entry.get() or 0)
            balance = income - (expenses + planned_savings)
            self.result_label.config(text=f"Залишок: {balance:.2f} грн")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа")

    def save_data(self):
        data = {
            "month": self.month.get(),
            "year": self.year.get(),
            "salary_husband": self.salary_husband.get(),
            "salary_wife": self.salary_wife.get(),
            "child_support": self.child_support.get(),
            "rent": self.rent.get(),
            "loans": self.loans.get(),
            "education": self.education.get(),
            "food": self.food.get(),
            "taxes_insurance": self.taxes_insurance.get(),
            "additional_expenses": self.additional_expenses.get(),
            "car_expenses": self.car_expenses.get(),
            "planned_savings": self.planned_savings.get(),
            "savings_entry": self.savings_entry.get()
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            messagebox.showinfo("Інформація", "Дані збережено успішно")

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.month.delete(0, tk.END)
                self.month.insert(0, data["month"])
                self.year.delete(0, tk.END)
                self.year.insert(0, data["year"])
                self.salary_husband.delete(0, tk.END)
                self.salary_husband.insert(0, data["salary_husband"])
                self.salary_wife.delete(0, tk.END)
                self.salary_wife.insert(0, data["salary_wife"])
                self.child_support.delete(0, tk.END)
                self.child_support.insert(0, data["child_support"])
                self.rent.delete(0, tk.END)
                self.rent.insert(0, data["rent"])
                self.loans.delete(0, tk.END)
                self.loans.insert(0, data["loans"])
                self.education.delete(0, tk.END)
                self.education.insert(0, data["education"])
                self.food.delete(0, tk.END)
                self.food.insert(0, data["food"])
                self.taxes_insurance.delete(0, tk.END)
                self.taxes_insurance.insert(0, data["taxes_insurance"])
                self.additional_expenses.delete(0, tk.END)
                self.additional_expenses.insert(0, data["additional_expenses"])
                self.car_expenses.delete(0, tk.END)
                self.car_expenses.insert(0, data["car_expenses"])
                self.planned_savings.delete(0, tk.END)
                self.planned_savings.insert(0, data["planned_savings"])
                self.savings_entry.delete(0, tk.END)
                self.savings_entry.insert(0, data["savings_entry"])
            messagebox.showinfo("Інформація", "Дані завантажено успішно")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
