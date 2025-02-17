import pandas as pd
import os
from datetime import datetime  # นำเข้า datetime

# กำหนดชื่อไฟล์
file_path = "group-3pq1ex51ka.csv"  # แก้ไขเป็นชื่อไฟล์ของคุณ

# ตรวจสอบว่าไฟล์มีอยู่หรือไม่
if os.path.exists(file_path):
    try:
        # อ่านไฟล์ CSV
        data = pd.read_csv(file_path, delimiter=',')  # ใช้ Tab เป็นตัวคั่น

        # แปลงคอลัมน์เวลาส่งให้เป็น datetime
        data['SubmittedAt'] = pd.to_datetime(data['SubmittedAt'])

        # คำนวณเวลาที่เร็วที่สุดและช้าที่สุด
        fastest_time = data['SubmittedAt'].min()
        slowest_time = data['SubmittedAt'].max()

        # นับจำนวนตัว 'p' ในคอลัมน์ Result
        #count_p = data['Result'].str.count('p', case=False).sum()
        count_p = data['Result'].str.lower().str.count('p').sum()

        # เวลาที่กำหนดให้สำหรับเปรียบเทียบ
        #reference_time = datetime(2025, 2, 17, 12, 0, 0)  # เปลี่ยนเป็นเวลาที่ต้องการ
        reference_time = fastest_time
        data['TimeDifference'] = data['SubmittedAt'] - reference_time

        # แสดงผลข้อมูลที่อ่านได้และค่าที่คำนวณได้
        print(data)
        print(f"Fastest Submission: {fastest_time}")
        print(f"Slowest Submission: {slowest_time}")
        print(f"Count of 'p' in Result: {count_p}")
        print("Time differences compared to reference time:")
        print(data[['SubmittedAt', 'TimeDifference']])

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
else:
    print(f"ไม่พบไฟล์: {file_path}, กรุณาตรวจสอบตำแหน่งและชื่อไฟล์อีกครั้ง")

