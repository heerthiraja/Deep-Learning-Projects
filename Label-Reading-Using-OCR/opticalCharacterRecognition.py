#pillow image read library
try:
    from PIL import Image
except ImportError:
    import Image
#if image not open with pillow. it opens from image. thats the code.

      
#OCR
import pytesseract

#Exe. File 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('2.jpg')
print(info)
file = open("result.txt","w")
file.write(info)
file.close()
print("Written Successful")
