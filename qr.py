import segno
a= input("Enter the text you want to change in the URL")
qrcode = segno.make_qr(a)
qrcode.save("new.png",scale=10,border=10)