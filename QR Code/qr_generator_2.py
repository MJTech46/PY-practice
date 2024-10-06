import pyqrcode
import png

# Data to be encoded
data = "https://www.example.com"

# Create QR code
qr = pyqrcode.create(data)

# Save the QR code as a PNG file
qr.png("qrcode_pyqrcode.png", scale=8)
