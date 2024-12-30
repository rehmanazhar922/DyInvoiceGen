from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import cv2
import numpy as np

input_file = "facture_.png"
output_file = "facture.png"

img = Image.open(input_file)
draw = ImageDraw.Draw(img)

bg_color_invoice = img.getpixel((25, 75))
bg_color_date = img.getpixel((25, 125))

font_path = "C:/Windows/Fonts/Arial.ttf"
font_invoice = ImageFont.truetype(font_path, 12)
font_date = ImageFont.truetype(font_path, 14)

new_date = datetime.now().strftime("%d %B %Y")
base_invoice = "722051ca5d30960a0234b7aa26be7f37"
modified_invoice = "#" + base_invoice[:-4] + datetime.now().strftime('%H%M')

coordinates = {
    "invoice_number": (25, 80),
    "date": (25, 130)
}

draw.rectangle([(coordinates["invoice_number"][0]-1, coordinates["invoice_number"][1]-1), 
                (coordinates["invoice_number"][0] + 200, coordinates["invoice_number"][1] + 15)], fill=bg_color_invoice)
draw.rectangle([(coordinates["date"][0]-1, coordinates["date"][1]-1), 
                (coordinates["date"][0] + 150, coordinates["date"][1] + 17)], fill=bg_color_date)

gray_color = (90, 90, 90)
dark_color = (40, 40, 40)
draw.text(coordinates["invoice_number"], modified_invoice, fill=gray_color, font=font_invoice)
draw.text(coordinates["date"], new_date, fill=dark_color, font=font_date)

img_np = np.array(img)
img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

blurred_img = cv2.GaussianBlur(img_cv2, (3, 3), 0.5)

cv2.imwrite(output_file, blurred_img)
print(f"Updated invoice saved as {output_file}")
