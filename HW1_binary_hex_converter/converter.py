import tkinter as tk               # 匯入tkinter模組，簡寫tk
from tkinter import messagebox     # 從tkinter匯入messagebox，用於彈出錯誤視窗

class ConverterApp:                    # 定義ConverterApp的類別
    def __init__(self, root):          # 類別初始化，root代表主視窗
        self.root = root               # 將傳入的root存入實際變數中
        self.root.title("進位轉換器")   # 設定視窗標題
        self.root.geometry("400x250")  # 設定視窗尺寸：寬400像素、高250像素

        # 標籤與變數
        tk.Label(root, text="Binary (2進位):").pack(pady=5)       # 顯示「Binary (2進位)」的文字標籤
        self.bin_entry = tk.Entry(root)                           # 建立供使用者輸入2進位數值的輸入框
        self.bin_entry.pack()                                     # 將2進位輸入框放進視窗，垂直間距：5

        tk.Label(root, text="Decimal (10進位):").pack(pady=5)     # 顯示「Decimal (10進位)」的文字標籤
        self.dec_entry = tk.Entry(root)                           # 建立供使用者輸入10進位數值的輸入框
        self.dec_entry.pack()                                     # 將10進位輸入框放進視窗，垂直間距：5

        tk.Label(root, text="Hexadecimal (16進位):").pack(pady=5) # 顯示「Hexadecimal (16進位)」
        self.hex_entry = tk.Entry(root)                           # 建立供使用者輸入16進位數值的輸入框
        self.hex_entry.pack()                                     # 將16進位輸入框放進視窗，垂直間距：5

        # 按鈕
        self.convert_btn = tk.Button(root, text="開始轉換", command=self.process_conversion)  # 建立「開始轉換」的按鈕，點擊
        self.convert_btn.pack(pady=20)                                                       # 將按鈕放進視窗，垂直間距：20

    # 三種進位間的手動轉換
    def manual_to_decimal(self, s, base):         # 定義manual_to_decimal：將任意字串轉換成10進位數字，(因為是在Converter.App中定義，所以一定要加self,輸入字串,進位基準，if2進位，base=2)
        digits = "0123456789ABCDEF"               # digits:可能出現的字元
        res = 0                                   # 初始結果為0
        for char in s.upper():                    # 將輸入字串轉為大寫並取出字元
            val = digits.find(char)               # val:找尋在digits中，找出對應數值
            if val <= -1 or val >= base:          # 當val值小於等於-1(找不到字元)或大於等於base值
                raise ValueError                  # 回報錯誤訊息
            res = res * base + val                # 進位計算:結果*基準+當前數值(二進位轉十進位ex:101，則s=101、base=2 1.res=1 2.res=1*2+0=2 3.res=2*2+1=5)
        return res                                # 輸出結果

    def manual_from_decimal(self, n, base):       # 定義manual_from_decimal：將10進位數字轉換成目標進位字元
        if n == 0: return "0"                     # 如果輸入n=0，回傳結果字串0
        digits = "0123456789ABCDEF"               # digits:可能出現的字元
        res = ""                                  # 初始化結果字串
        while n > 0:                              # 當n>0時，持續迴圈
            res = digits[n % base] + res          # 短除法(十進位轉十六進位ex:100，則n=100、base=16 1.100/16=6...4 res=4 2.6/16=0...6 res=64[驗算:6*16^1+4*16^0=100])
            n //= base                            # (十進位轉二進位ex：10，則n=10 1.10/2=5...0 res=0 2.5/2=2...1 res=10 3.2/2=1...0 res=010 4.1/2=0...1 res=1010[驗算:1*2^3+0*2^0+1*2^1+0*2^0=10])
        return res                                # 輸出結果

    def process_conversion(self):
        try:
            # 判斷哪個欄位有輸入內容，將其轉換成10進位(dec)
            if self.bin_entry.get():                                    # 如果2進位輸入欄位有抓取到數字
                dec = self.manual_to_decimal(self.bin_entry.get(), 2)   # 將manual_to_decimal設定為(我們所抓取到的數字,base=2)
            elif self.dec_entry.get():                                  # 如果10進位輸入欄位有抓取到數字
                dec = self.manual_to_decimal(self.dec_entry.get(), 10)  # 將manual_to_decimal設定為(我們所抓取到的數字,base=10)
            elif self.hex_entry.get():                                  # 如果16進位輸入欄位有抓取到數字
                dec = self.manual_to_decimal(self.hex_entry.get(), 16)  # 將manual_to_decimal設定為(我們所抓取到的數字,base=16)
            else:
                return                                                  # 否則就都不執行

            # 清除欄位舊有內容，顯示計算結果
            self.bin_entry.delete(0, tk.END)
            self.bin_entry.insert(0, self.manual_from_decimal(dec, 2))
            
            self.dec_entry.delete(0, tk.END)
            self.dec_entry.insert(0, str(dec))
            
            self.hex_entry.delete(0, tk.END)
            self.hex_entry.insert(0, self.manual_from_decimal(dec, 16))

        # 若出現ValueError，顯示標題:錯誤的「請輸入有效數值格式」的警告視窗
        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效數值格式")

# AI 建議生成並保留的一段程式
if __name__ == "__main__":    # 如果此腳本是主程式直接執行
    root = tk.Tk()            # 初始化tkinter，建立主視窗物件
    app = ConverterApp(root)  # 建立ConverterApp，並將主視窗傳進去
    root.mainloop()           # 開始執行視窗迴圈，讓視窗保持開啟並監聽操作