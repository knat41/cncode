import requests
from bs4 import BeautifulSoup

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

# 🔹 ทดสอบฟังก์ชัน
url = 'https://elabsheet.org/elab/taskpads/workon/7hoqhluyq2/uqn2mfcu37/'
textarea_data = scrape_textareas(url)

# แสดงผลข้อมูลที่ดึงได้
for i, data in enumerate(textarea_data, start=1):
    print(f'Textarea #{i}:')
    print(data)
    print('-' * 40)

