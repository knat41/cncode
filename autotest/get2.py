import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime  # นำเข้า datetime

# กำหนดชื่อไฟล์
file_path = "submission_data.csv"  # แก้ไขเป็นชื่อไฟล์ของคุณ

def scrape_textareas(url):
    """ ดึงข้อมูลจาก <textarea> ในเว็บที่กำหนด และคืนค่าเป็น list ของข้อความ """
    try:
        # ส่ง HTTP GET request ไปยัง URL
        response = requests.get(url)
        response.raise_for_status()  # ตรวจสอบข้อผิดพลาด HTTP

        # ใช้ BeautifulSoup วิเคราะห์ HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # ค้นหา <textarea> ทั้งหมดในหน้าเว็บ
        textareas = soup.find_all('textarea')

        # ดึงข้อมูลจากแต่ละ <textarea> และเก็บเป็นลิสต์
        return [textarea.get_text().strip() for textarea in textareas]

    except requests.exceptions.RequestException as e:
        print(f'เกิดข้อผิดพลาดในการดึงข้อมูล: {e}')
        return []

# ตรวจสอบว่าไฟล์มีอยู่หรือไม่
if os.path.exists(file_path):
    try:
        # อ่านไฟล์ CSV
        data = pd.read_csv(file_path, delimiter='\t')  # ใช้ Tab เป็นตัวคั่น

        # แปลงคอลัมน์เวลาส่งให้เป็น datetime
        data['SubmittedAt'] = pd.to_datetime(data['SubmittedAt'])

        # คำนวณเวลาที่เร็วที่สุดและช้าที่สุด
        fastest_time = data['SubmittedAt'].min()
        slowest_time = data['SubmittedAt'].max()

        # นับจำนวนตัว 'p' ในคอลัมน์ Result (แก้ไขการใช้ count())
        count_p = data['Result'].str.lower().str.count('p').sum()

        # เวลาที่กำหนดให้สำหรับเปรียบเทียบ
        reference_time = datetime(2025, 2, 17, 12, 0, 0)  # เปลี่ยนเป็นเวลาที่ต้องการ
        data['TimeDifference'] = data['SubmittedAt'] - reference_time

        # ดึงข้อมูลจากแต่ละลิงก์ในคอลัมน์ 'Link'
        data['ExtractedText'] = data['Link'].apply(scrape_textareas)

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
