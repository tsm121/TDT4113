from PIL import ImageFilter
from PIL import Image
from PIL import ImageEnhance
from imager2 import Imager


class Img(Imager):

    def __init__(self, path):
        super().__init__(path)

        #Imager.display(im)
        #im = Imager.scale(self, 0.5,0.5)
        #im2 = Imager.map_color_wta(im,False,0.2)
        #Imager.display(im2)

        #im3 = Imager.gen_grayscale(im)
        #Imager.display(im3)
        #im = Imager.morph4(self,self)
        #Imager.display(im)

class Test:

    def __init__(self, im1_path, im2_path):
        #Image objects
        self.im1 = Img(im1_path)
        self.im2 = Img(im2_path)

        #Imager objects
        self.im1_img = Image.open(im1_path)
        self.im2_img = Image.open(im2_path)

        #self.tunnel()
        #self.scale_colors()

        #self.emboss()
        #self.brightness()
        #self.morph1()
        #self.collage()

    def fix_size(self):

        xSize = 250
        ySize = 250
        self.im1 = self.im1.resize(xSize, ySize)
        self.im2 = self.im2.resize(xSize, ySize)

    def morph4(self):
        self.fix_size()
        im3 = self.im1.morph4(self.im2)
        im3.display()

    def morph1(self):
        self.fix_size()
        im3 = self.im1.morph(self.im2)
        im3.display()

    def gray(self):
        im3 = self.im1.gen_grayscale()
        im3.display()

    def scale_colors(self):
        im3 = self.im2.scale_colors(False, 5)
        im3.display()

    def collage(self):
        im3 = self.im1.concat_horiz(self.im2)
        im3 = im3.concat_horiz(self.im2)
        im3 = im3.concat_horiz(self.im1)
        im3.display()

    def tunnel(self):

        im3 = self.im1.tunnel(10, 0.85)
        im3.display()

    def emboss(self):
        im_filter = self.im1_img.filter(ImageFilter.EMBOSS)
        im_filter.show()

    def brightness(self):
        img_enh = ImageEnhance.Brightness(self.im1_img)

        for x in range(2,4):
            y = x / 2
            img_enh.enhance(y).show()



im1_path = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 5/images/robot.jpeg"
im2_path = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 5/images/einstein.jpeg"


test_obj = Test(im1_path, im2_path)
