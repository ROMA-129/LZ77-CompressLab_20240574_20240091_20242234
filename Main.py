import ctypes
import tkinter as tk
from tkinter import filedialog, messagebox

from Compression import compress
from Decompression import decompress

# --- 🎯 حل مشكلة بكسلة الخطوط (High DPI Awareness) ---
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass
# ---------------------------------------------------


def encode_symbol(symbol):
    """تحويل الحروف الخاصة إلى صيغة آمنة للحفظ في الملف"""
    if symbol is None:
        return "NULL"
    elif symbol == "\n":
        return "\\n"
    elif symbol == "\r":
        return "\\r"
    elif symbol == "\t":
        return "\\t"
    elif symbol == ",":
        return "\\COMMA"
    return symbol


def decode_symbol(symbol_str):
    """استرجاع الحروف الخاصة عند قراءة الملف"""
    if symbol_str == "NULL":
        return None
    elif symbol_str == "\\n":
        return "\n"
    elif symbol_str == "\\r":
        return "\\r"
    elif symbol_str == "\\t":
        return "\t"
    elif symbol_str == "\\COMMA":
        return ","
    return symbol_str


def write_tags_file(file_path, tags):
    """حفظ الـ Tags في ملف txt"""
    with open(file_path, "w", encoding="utf-8") as file:
        for pos, length, next_sym in tags:
            sym_str = encode_symbol(next_sym)
            file.write(f"{pos},{length},{sym_str}\n")


def read_tags_file(file_path):
    """قراءة الـ Tags من ملف txt"""
    tags = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\r\n")
            if not line:
                continue
            parts = line.split(",", 2)
            if len(parts) == 3:
                pos = int(parts[0])
                length = int(parts[1])
                next_sym = decode_symbol(parts[2])
                tags.append((pos, length, next_sym))
    return tags


def process_compression():
    """عملية اختيار الملف وضغطه"""
    input_file = filedialog.askopenfilename(
        title="Select Input Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Compressed Tags As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if not output_file:
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        tags = compress(text)
        write_tags_file(output_file, tags)

        messagebox.showinfo(
            "Compression Complete",
            "Compression completed successfully!"
        )
    except Exception as e:
        messagebox.showerror(
            "Compression Error",
            f"An error occurred:\n\n{e}"
        )


def process_decompression():
    """عملية اختيار ملف الـ Tags وفك ضغطه"""
    input_file = filedialog.askopenfilename(
        title="Select Tags File",
        filetypes=[("Text Files", "*.txt")]
    )
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Decompressed Text As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if not output_file:
        return

    try:
        tags = read_tags_file(input_file)
        decompressed_text = decompress(tags)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decompressed_text)

        messagebox.showinfo(
            "Decompression Complete",
            "Decompression completed successfully!"
        )
    except Exception as e:
        messagebox.showerror(
            "Decompression Error",
            f"An error occurred:\n\n{e}"
        )


def show_about_dialog(parent):
    """دالة لفتح نافذة فرعية بالأسماء عند الضغط على زر About"""
    about_win = tk.Toplevel(parent)
    about_win.title("About & Team")
    about_win.geometry("400x260")
    about_win.resizable(False, False)
    
    bg_color = "#181825"
    about_win.configure(bg=bg_color)

    about_win.transient(parent)
    about_win.grab_set()

    title_label = tk.Label(
        about_win,
        text="PROJECT TEAM",
        font=("Segoe UI", 11, "bold"),
        bg=bg_color,
        fg="#89b4fa"
    )
    title_label.pack(pady=(20, 15))

    members = [
        ("Mariam Said Hanafy", "20240574"),
        ("Omnia Ramadan Abdelghany", "20240091"),
        ("Amr Tariq Hawash", "20242234")
    ]

    for name, student_id in members:
        row_frame = tk.Frame(about_win, bg=bg_color)
        row_frame.pack(fill="x", padx=25, pady=4)  # 👈 تم التعديل إلى padx

        name_label = tk.Label(
            row_frame,
            text=f"•  {name}",
            font=("Segoe UI", 10),
            bg=bg_color,
            fg="#cdd6f4",
            anchor="w"
        )
        name_label.pack(side="left")

        id_label = tk.Label(
            row_frame,
            text=student_id,
            font=("Consolas", 10, "bold"),
            bg=bg_color,
            fg="#a6adc8",
            anchor="e"
        )
        id_label.pack(side="right")

    close_btn = tk.Button(
        about_win,
        text="Close",
        font=("Segoe UI", 9, "bold"),
        bg="#313244",
        fg="#cdd6f4",
        activebackground="#45475a",
        activeforeground="#cdd6f4",
        relief="flat",
        cursor="hand2",
        command=about_win.destroy
    )
    close_btn.pack(pady=(20, 0), ipadx=15)


def main():
    root = tk.Tk()
    root.title("LZ77 Compression Engine")
    root.geometry("450x380")
    root.resizable(False, False)

    bg_color = "#1e1e2e"
    root.configure(bg=bg_color)

    # 1. إطار علوي يحتوي على زر (About / Team)
    top_bar = tk.Frame(root, bg=bg_color)
    top_bar.pack(fill="x", padx=15, pady=(10, 0))  # 👈 تم التعديل إلى padx

    about_btn = tk.Button(
        top_bar,
        text="ℹ About Team",
        font=("Segoe UI", 9, "bold"),
        bg="#313244",
        fg="#89b4fa",
        activebackground="#45475a",
        activeforeground="#b4befe",
        relief="flat",
        cursor="hand2",
        command=lambda: show_about_dialog(root)
    )
    about_btn.pack(side="right")

    # 2. العنوان الرئيسي
    title_label = tk.Label(
        root,
        text="LZ77 Compression Engine",
        font=("Segoe UI", 16, "bold"),
        bg=bg_color,
        fg="#cdd6f4"
    )
    title_label.pack(pady=(20, 20))

    # 3. زر الضغط
    compress_btn = tk.Button(
        root,
        text="Compress TXT File",
        font=("Segoe UI", 11, "bold"),
        width=25,
        height=2,
        bg="#89b4fa",
        fg="#11111b",
        activebackground="#b4befe",
        activeforeground="#11111b",
        relief="flat",
        cursor="hand2",
        command=process_compression
    )
    compress_btn.pack(pady=10)

    # 4. زر فك الضغط
    decompress_btn = tk.Button(
        root,
        text="Decompress Tags File",
        font=("Segoe UI", 11, "bold"),
        width=25,
        height=2,
        bg="#89b4fa",
        fg="#11111b",
        activebackground="#b4befe",
        activeforeground="#11111b",
        relief="flat",
        cursor="hand2",
        command=process_decompression
    )
    decompress_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()