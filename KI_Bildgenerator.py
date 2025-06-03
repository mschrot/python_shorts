# https://youtube.com/shorts/hinplDA-kUw?si=1jC_Zmsh76goGYTE

from g4f.client import Client
text_eingabe = input('Eingabe:')
app_client = Client()
my_model = app_client.images.generate(
    model='flux',
    prompt=text_eingabe,
    response_format='url'
)
image_url = my_model.data[0].url
print(f'Link zum Bild: \n{image_url}')
