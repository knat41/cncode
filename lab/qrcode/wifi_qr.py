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
