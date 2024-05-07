image = input("enter the name of the image file: ")
content = input("enter message to be encrypted: ")
oImage = 'encrypt.png'

from stegano import lsb 

# encryption
lsb.hide(image,message=content).save(oImage)

# decryption
message = lsb.reveal(oImage)
print("encrypted message: "+message)

'''
from stegano import exifHeader as efi

# encryption
efi.hide(image, oImage, content)
# decryption
message = efi.reveal(oImage)
print("encrypted message: ")
print(message)
'''
