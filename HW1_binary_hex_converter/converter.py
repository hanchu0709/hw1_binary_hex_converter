import tkinter as tk
from tkinter import messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("進位轉換器")
        self.root.geometry("400x250")

        # 標籤與變數
        tk.Label(root, text="Binary (2進位):").pack(pady=5)
        self.bin_entry = tk.Entry(root)
        self.bin_entry.pack()

        tk.Label(root, text="Decimal (10進位):").pack(pady=5)
        self.dec_entry = tk.Entry(root)
        self.dec_entry.pack()

        tk.Label(root, text="Hexadecimal (16進位):").pack(pady=5)
        self.hex_entry = tk.Entry(root)
        self.hex_entry.pack()

        # 按鈕
        self.convert_btn = tk.Button(root, text="開始轉換", command=self.process_conversion)
        self.convert_btn.pack(pady=20)

    # 自定義轉換邏輯
    def manual_to_decimal(self, s, base):
        digits = "0123456789ABCDEF"
        res = 0
        for char in s.upper():
            val = digits.find(char)
            if val == -1 or val >= base:
                raise ValueError
            res = res * base + val
        return res

    def manual_from_decimal(self, n, base):
        if n == 0: return "0"
        digits = "0123456789ABCDEF"
        res = ""
        while n > 0:
            res = digits[n % base] + res
            n //= base
        return res

    def process_conversion(self):
        try:
            # 判斷哪個欄位有輸入內容
            if self.bin_entry.get():
                dec = self.manual_to_decimal(self.bin_entry.get(), 2)
            elif self.dec_entry.get():
                dec = self.manual_to_decimal(self.dec_entry.get(), 10)
            elif self.hex_entry.get():
                dec = self.manual_to_decimal(self.hex_entry.get(), 16)
            else:
                return

            # 更新所有欄位 (支援超過 255 的數值)
            self.bin_entry.delete(0, tk.END)
            self.bin_entry.insert(0, self.manual_from_decimal(dec, 2))
            
            self.dec_entry.delete(0, tk.END)
            self.dec_entry.insert(0, str(dec))
            
            self.hex_entry.delete(0, tk.END)
            self.hex_entry.insert(0, self.manual_from_decimal(dec, 16))

        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數值格式")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()