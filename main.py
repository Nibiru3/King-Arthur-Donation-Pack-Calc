import tkinter as tk

def calculate_cost():
    try:
        pulls = int(pulls_entry.get()) if pulls_entry.get() else 0
        crystals = int(crystals_entry.get()) if crystals_entry.get() else 0
        stamina = int(stamina_entry.get()) if stamina_entry.get() else 0
        leg = int(leg_entry.get()) if leg_entry.get() else 0
        
        cost = (pulls * 1) + (crystals * 0.00067) + (stamina * 0.00335) + (leg * 60)
        result_label.config(text=f"Итоговая стоимость: ${cost:.2f}")
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректные значения.")

root = tk.Tk()
root.title("King Arthur Legend's Rise Cost Calculator")
root.geometry("400x300")

# Ввод полей
tk.Label(root, text="Количество призывов:").pack()
pulls_entry = tk.Entry(root)
pulls_entry.pack()

tk.Label(root, text="Количество кристаллов:").pack()
crystals_entry = tk.Entry(root)
crystals_entry.pack()

tk.Label(root, text="Количество стамины:").pack()
stamina_entry = tk.Entry(root)
stamina_entry.pack()

tk.Label(root, text="Количество лег:").pack()
leg_entry = tk.Entry(root)
leg_entry.pack()

# Кнопка расчёта
tk.Button(root, text="Посчитать стоимость", command=calculate_cost).pack()

# Поле вывода результата
result_label = tk.Label(root, text="Итоговая стоимость: $0.00")
result_label.pack()

root.mainloop()
