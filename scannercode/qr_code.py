import qrcode as qr
img = qr.make("https://www.linkedin.com/in/anjalikashyap997/")
img.save("my_linkedIn.png")