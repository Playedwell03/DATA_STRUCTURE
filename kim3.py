import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ------------------ 기능 함수 ------------------
def process1():
    try:
        f = float(e1.get())
        c = (f - 32) * 5/9
        e2.delete(0, tk.END)
        e2.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "숫자를 입력하세요!")

def process2():
    try:
        c = float(e2.get())
        f = c * 9/5 + 32
        e1.delete(0, tk.END)
        e1.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "숫자를 입력하세요!")

# ------------------ 메인 윈도우 ------------------
window = tk.Tk()
window.title("화씨 <-> 섭씨 변환")

# 라벨과 Entry
l1 = tk.Label(window, text="화씨", font=("Helvetica", 16, "italic"))
l1.grid(row=0, column=0, padx=5, pady=5)
e1 = tk.Entry(window, bg="yellow", fg="black")
e1.grid(row=0, column=1, padx=5, pady=5)

l2 = tk.Label(window, text="섭씨", font=("Helvetica", 16, "italic"))
l2.grid(row=1, column=0, padx=5, pady=5)
e2 = tk.Entry(window, bg="yellow", fg="black")
e2.grid(row=1, column=1, padx=5, pady=5)

# ------------------ 버튼 스타일 ------------------
style = ttk.Style()
style.configure("Blue.TButton", background="lightblue", foreground="black")
style.map("Blue.TButton",
          background=[("active", "deepskyblue")],
          foreground=[("active", "white")])

style.configure("Green.TButton", background="lightgreen", foreground="black")
style.map("Green.TButton",
          background=[("active", "green")],
          foreground=[("active", "white")])

# 버튼
b1 = ttk.Button(window, text="화씨 -> 섭씨", command=process1, style="Blue.TButton")
b2 = ttk.Button(window, text="섭씨 -> 화씨", command=process2, style="Green.TButton")
b1.grid(row=2, column=0, padx=5, pady=10)
b2.grid(row=2, column=1, padx=5, pady=10)

# ------------------ 메인 루프 ------------------
window.mainloop()