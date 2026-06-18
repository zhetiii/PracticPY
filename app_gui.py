import tkinter as tk
from tkinter import ttk, messagebox
import db_manager

class MainWindow:
    def __init__(self, window_root):
        self.root = window_root
        self.root.title("Панель управления: Экспресс Курьер")
        self.root.geometry("650x450")
        
        db_manager.setup_database()

        # Таблица перемещена наверх
        table_columns = ("id_col", "customer_col", "date_col", "status_col", "total_col")
        self.data_grid = ttk.Treeview(window_root, columns=table_columns, show="headings")
        self.data_grid.heading("id_col", text="Рег. Номер")
        self.data_grid.heading("customer_col", text="Контрагент")
        self.data_grid.heading("date_col", text="Дата оформления")
        self.data_grid.heading("status_col", text="Текущий статус")
        self.data_grid.heading("total_col", text="Сумма (руб.)")
        self.data_grid.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Панель управления с кнопками перенесена вниз
        control_panel = tk.Frame(window_root)
        control_panel.pack(pady=10, fill=tk.X)
        
        tk.Button(control_panel, text="Синхронизировать", command=self.refresh_grid).pack(side=tk.LEFT, padx=10)
        tk.Button(control_panel, text="+ Новый клиент", command=self.create_mock_client).pack(side=tk.LEFT, padx=10)
        tk.Button(control_panel, text="+ Новый заказ", command=self.create_mock_order).pack(side=tk.LEFT, padx=10)
        tk.Button(control_panel, text="Сформировать отчет", command=self.display_stats).pack(side=tk.RIGHT, padx=10)

        self.refresh_grid()

    def refresh_grid(self):
        for entry in self.data_grid.get_children():
            self.data_grid.delete(entry)
        for record in db_manager.fetch_all_orders():
            self.data_grid.insert("", tk.END, values=record)

    def create_mock_client(self):
        db_manager.insert_new_customer("Петров Петр", "+79119876543", "Санкт-Петербург, ул. Ленина")
        messagebox.showinfo("Системное уведомление", "Карточка нового клиента создана.")

    def create_mock_order(self):
        db_manager.insert_new_order(1, "2026-06-18", "новый", 2450.0)
        self.refresh_grid()

    def display_stats(self):
        metrics = db_manager.calculate_status_stats()
        output_lines = [f"• {item[0]}: {item[1]} ед." for item in metrics]
        content = "\n".join(output_lines) if output_lines else "Данные отсутствуют."
        messagebox.showinfo("Аналитический отчет", content)

if __name__ == "__main__":
    window = tk.Tk()
    interface = MainWindow(window)
    window.mainloop()
