import qrcode as qr
#In the URL Section "A" you can put any link and you are able to generate QR Code Easily. 
A=input("Enter the URL :")
img=qr.make(A)
img.save("Generated_Qr3.jpg")
#After running the code with Python Debugger.The QR Code will generate where you saved the file.