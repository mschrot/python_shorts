# https://youtube.com/shorts/KnmwX_vqyvI?si=W41xpTyjD7b8haMN

import qrcode  # Import qrcode modull


qr_inhalt = 't.me/mschrot'    # Variable inhalt wird in QR-Code gespeichert
img = qrcode.make(qr_inhalt)  # Erstellt das QR-Code-Bild-Objekt   
img.save('qrcode.png')        # Speichert die Bilddatei mit dem Namen 'qrcode.png'
