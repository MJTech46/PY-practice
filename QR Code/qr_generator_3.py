import segno

# Data to be encoded
data = "https://www.example.com"

# Create QR code
qr = segno.make(data)

# Save the QR code as a PNG file
qr.save("qrcode_segno.png", scale=8)
