from PIL import Image, ImageFont, ImageDraw
from django.utils.six import BytesIO
from versatileimagefield.datastructures import FilteredImage
from versatileimagefield.registry import versatileimagefield_registry


class WatermarkImage(FilteredImage):

    def process_image(self, image, image_format, save_kwargs={}):
        image = image.convert('RGBA')

        txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("arial.ttf", 200)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((400, 400), "Hello", font=fnt, fill=(255, 255, 255, 128))

        imagefile = BytesIO()
        inv_image = Image.alpha_composite(image, txt)
        inv_image.save(
            imagefile,
            **save_kwargs
        )
        print(imagefile)
        return imagefile


versatileimagefield_registry.register_filter('water', WatermarkImage)
