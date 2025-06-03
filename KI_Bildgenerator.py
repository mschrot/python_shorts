# https://youtube.com/shorts/hinplDA-kUw?si=1jC_Zmsh76goGYTE

'''
g4f/                ← Paket
├── __init__.py
├── client.py       ← Modul
├── provider/
│   └── ...         ← weiteres Paket
└── utils.py        ← weiteres Modul

'''

#  pip install g4f

from g4f.client import Client
# aus paket_g4f.modul_client importiere --> class Client



text_eingabe = input('Eingabe:') # Eingabefeld --> Speichert die Eingabe in der Variable
app_client = Client()      # erstelle appClienten aus class Client() für kommunikation mit Modull-g4f


my_model = app_client.images.generate(
    model='flux',          # AI-Modell
    prompt=text_eingabe,   # Benutzer eingabe
    response_format='url'  # Format --> zum Bild-URL
)


# Bild-URL erzeugen
image_url = my_model.data[0].url

# Bild-URL ausgeben
print(f'Link zum Bild: \n{image_url}')
