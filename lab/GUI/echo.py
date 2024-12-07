import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # ดึงข้อมูลจากช่องป้อนข้อมูล
    data_type = qr_type.get()
    data_input = input_field.get()
    
    if not data_input.strip():
        messagebox.showerror("Error", "กรุณาป้อนข้อมูล!")
        return
    
    # สร้างข้อมูล QR Code
    if data_type == "WiFi":
        ssid = ssid_field.get().strip()
        password = password_field.get().strip()
        security = security_field.get().strip()
        qr_data = f"WIFI:S:{ssid};T:{security};P:{password};;"
    else:
        qr_data = data_input

    # สร้าง QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # แสดง QR Code บน GUI
    qr_img_tk = ImageTk.PhotoImage(qr_img.resize((200, 200)))
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

    # เก็บภาพ QR Code สำหรับบันทึก
    global qr_image
    qr_image = qr_img

def save_qr():
    if qr_image is None:
        messagebox.showwarning("Warning", "ยังไม่มี QR Code ที่สร้างไว้!")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
    )
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Success", f"บันทึกไฟล์ QR Code ที่: {file_path}")

def switch_type(*args):
    if qr_type.get() == "WiFi":
        wifi_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        url_frame.grid_remove()
    else:
        wifi_frame.grid_remove()
        url_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("QR Code Generator")

# ตัวเลือกประเภทข้อมูล
qr_type = tk.StringVar(value="URL")
tk.Label(root, text="เลือกประเภทข้อมูล:").grid(row=0, column=0, padx=10, pady=10)
type_menu = ttk.Combobox(root, textvariable=qr_type, values=["URL", "WiFi", "Text"], state="readonly")
type_menu.grid(row=0, column=1, padx=10, pady=10)
type_menu.bind("<<ComboboxSelected>>", switch_type)

# ช่องป้อนข้อมูลสำหรับ URL หรือข้อความ
url_frame = ttk.Frame(root)
tk.Label(url_frame, text="ป้อนข้อมูลหรือ URL:").grid(row=0, column=0, padx=10, pady=10)
input_field = tk.Entry(url_frame, width=30)
input_field.grid(row=0, column=1, padx=10, pady=10)

# ช่องป้อนข้อมูลสำหรับ WiFi
wifi_frame = ttk.Frame(root)
tk.Label(wifi_frame, text="SSID:").grid(row=0, column=0, padx=10, pady=5)
ssid_field = tk.Entry(wifi_frame, width=20)
ssid_field.grid(row=0, column=1, padx=10, pady=5)
tk.Label(wifi_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_field = tk.Entry(wifi_frame, width=20, show="*")
password_field.grid(row=1, column=1, padx=10, pady=5)
tk.Label(wifi_frame, text="Security (WPA/WEP):").grid(row=2, column=0, padx=10, pady=5)
security_field = tk.Entry(wifi_frame, width=20)
security_field.grid(row=2, column=1, padx=10, pady=5)

# แสดง Frame เริ่มต้น
url_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

# ปุ่มสร้างและบันทึก QR Code
ttk.Button(root, text="สร้าง QR Code", command=generate_qr).grid(row=3, column=0, padx=10, pady=10)
ttk.Button(root, text="บันทึก QR Code", command=save_qr).grid(row=3, column=1, padx=10, pady=10)

# แสดง QR Code ที่สร้างขึ้น
qr_label = tk.Label(root)
qr_label.grid(row=4, column=0, columnspan=2, pady=10)

# ตัวแปรเก็บ QR Code ที่สร้างขึ้น
qr_image = None

root.mainloop()
