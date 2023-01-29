from PIL import Image #by DZgas 18.05.2022

# https://stackoverflow.com/questions/48248405/cannot-write-mode-rgba-as-jpeg
###стандартное уменьшение качества
# for U in range(2):
    # U+1
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1),Image.BICUBIC)
    # rgb_im.save('1.jpeg', format="JPEG", quality=30, optimize=False)
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1),Image.LANCZOS)
    # rgb_im.save('1.jpeg', format="JPEG", quality=50, optimize=False)
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1),Image.LANCZOS)
    # rgb_im.save('1.jpeg', format="JPEG", quality=20, optimize=False)
    # print(U)
# for U in range(2):
    # U+1
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])-1, (im.size[1])-1),Image.BICUBIC)
    # rgb_im.save('1.jpeg', format="JPEG", quality=41, optimize=False)
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])-1, (im.size[1])-1),Image.LANCZOS)
    # rgb_im.save('1.jpeg', format="JPEG", quality=56, optimize=False)
    # im = Image.open("1.jpeg")
    # rgb_im = im.resize(((im.size[0])-1, (im.size[1])-1),Image.LANCZOS)
    # rgb_im.save('1.jpeg', format="JPEG", quality=21, optimize=False)
    # print(U)


###эффект вт¤гивани¤
# for U in range(2):
   # U+1
   # im = Image.open("1.jpeg")
   # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1))
   # rgb_im.save('1.jpeg', format="JPEG", quality=60)
   # im = Image.open("1.jpeg")
   # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1))
   # rgb_im.save('1.jpeg', format="JPEG", quality=80)
   # im = Image.open("1.jpeg")
   # rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1))
   # rgb_im.save('1.jpeg', format="JPEG", quality=10)
   # print(U)


###эффект выт¤гивани¤
for U in range(2):
   U+1
   im = Image.open("1.jpeg")
   rgb_im = im.resize(((im.size[0])-2, (im.size[1])-2))
   rgb_im.save('1.jpeg', format="JPEG", quality=60)
   im = Image.open("1.jpeg")
   rgb_im = im.resize(((im.size[0])+1, (im.size[1])+1))
   rgb_im.save('1.jpeg', format="JPEG", quality=80)
   im = Image.open("1.jpeg")
   rgb_im = im.resize(((im.size[0])-1, (im.size[1])+1))
   rgb_im.save('1.jpeg', format="JPEG", quality=10)
   print(U)
