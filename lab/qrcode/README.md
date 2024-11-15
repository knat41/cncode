# QR Code
## ใช้อะไรบ้าง
```
pip install qrcode
```
หรือ เพราะต้องใช้ pillow https://pypi.python.org/pypi/Pillow
```
pip install "qrcode[pil]"
```
## ตัวอย่าง
```python
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
```

ใส่ logo
```python
from PIL import Image
import qrcode

pixels = 256
wifi_logo = Image.open('cn_logo.jpg')

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(wifi_logo.size[0]))
hsize = int((float(wifi_logo.size[1])*float(wpercent)))
wifi_logo = wifi_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=1,
)
ssid =  'Chonkanya'
password = ''
security = '' # (one of WPA or WEP)

wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"

qr.add_data(wifi_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
pos = ((img.size[0] - wifi_logo.size[0]) // 2, (img.size[1] - wifi_logo.size[1]) // 2)
img.paste(wifi_logo, pos)

QR_image = img.resize((pixels, pixels), Image.NEAREST) 
    
QR_image.save("wfile20.png")
```
## น่าอ่านดู
* https://medium.com/@marc.bolle/generating-qr-codes-using-python-libraries-542b047890af
* https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d
* https://github.com/vinodvidhole/wifi-qr-code/blob/main/wifi-qr-code.ipynb
* https://thepythoncode.com/article/generate-read-qr-code-python
