# pip install qrcode
import qrcode                 # Import qrcode-Modul


qr_inhalt = 't.me/mschrot'    # Variable --> definiere den Inhalt des QR-Codes
img = qrcode.make(qr_inhalt)  # Erzeuge den QR-Code
img.save('qrcode.png')        # Save --> QR-Code.png
