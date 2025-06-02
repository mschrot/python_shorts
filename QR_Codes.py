# https://youtube.com/shorts/KnmwX_vqyvI?si=W41xpTyjD7b8haMN

import qrcode


qr_inhalt = 't.me/mschrot'
img = qrcode.make(qr_inhalt)
img.save('qrcode.png')
