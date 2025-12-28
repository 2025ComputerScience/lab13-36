!sudo apt update
!sudo apt install tesseract-ocr tesseract-ocr-chi-tra

!pip install pytesseract


from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# 開啟圖片
import pytesseract
from PIL import Image
import cv2

# 開啟圖片
image = Image.open("Q3.png")

text = pytesseract.image_to_string(image, lang='chi_tra+eng', config='--psm 6')

print("OCR 辨識結果:")
print("-" * 40)
print(text)

