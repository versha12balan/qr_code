import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5

)
data="https://www.google.com/search?q=google&oq=google&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTITCAEQLhiDARjHARixAxjRAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDIGCAQQRRg8MgYIBRBFGDwyBggGEAUYQDIGCAcQRRg80gEINTMxMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('text.png')

