import ocrspace

api = ocrspace.API()

with open('file.txt', 'w') as f:
    f.write(api.ocr_file('image.png'))

