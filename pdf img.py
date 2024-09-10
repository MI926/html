# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('tantrarajtantra/ilovepdf_split-range/476449-Tantraraja Tantra (1926)_text-1-151.pdf')
print("1")
#images[1].save('tantraraj/page'+ str(1) +'.jpg', 'JPEG')
for i in range(len(images)):
  
      # Save pages as images in the pdf
    if i == 109:
        images[i].save('tantraraj/page'+ str(i) +'.jpg', 'JPEG')

images = convert_from_path('tantrarajtantra/ilovepdf_split-range/476449-Tantraraja Tantra (1926)_text-1-151.pdf') 
for i in range(len(images)):
  
      # Save pages as images in the pdf
    images[i].save('tantraraj/page'+ str(i+150) +'.jpg', 'JPEG')
