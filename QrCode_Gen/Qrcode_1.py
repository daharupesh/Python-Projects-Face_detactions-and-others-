import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_H, 
    box_size = 10,
    border=4,
    )
qr.add_data("Hello, My name is Rupesh Kumar Daha")
qr.make(fit= True)
img = qr.make_image(fillColor = "red", back_color ="red")
img.save("rupesh1.png")