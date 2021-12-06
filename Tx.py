# image
from PIL import Image

im = Image.open('tcp.png')
img = im.load()

print('before')
print(img[500,600])
img[500,600] = (0,0,0)
print('after')
print(img[500,600])
# does this update? 
im.save('tcp_updated.png')  # Save the modified pixels as .png
