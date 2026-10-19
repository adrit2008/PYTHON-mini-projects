import qrcode

url = input("Enter your URL to generate QR code: ")
file_path = "qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)

QRimage = qr.make_image()
QRimage.save("MY qrcode" + "/" + file_path)

print( "Your qr code has been generated and saved ")
