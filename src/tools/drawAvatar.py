import math
from PIL import Image, ImageChops, ImageDraw
import io

def drawAvatar(r_color: tuple = (255, 0, 0), g_color: tuple = (0, 255, 0), b_color: tuple = (0, 0, 255)):
    width, height = 300, 300
    img = Image.new("RGB", (width, height), (0, 0, 0))

    red_layer = Image.new("RGB", (width, height), (0, 0, 0))
    green_layer = Image.new("RGB", (width, height), (0, 0, 0))
    blue_layer = Image.new("RGB", (width, height), (0, 0, 0))

    radius = 70
    center_x, center_y = width // 2, height // 2
    distance = 45 

    top_x = center_x
    top_y = center_y + int(distance * math.sin(math.radians(-90)))

    right_x = center_x + int(distance * math.cos(math.radians(30)))
    right_y = center_y + int(distance * math.sin(math.radians(30)))

    left_x = center_x + int(distance * math.cos(math.radians(150)))
    left_y = center_y + int(distance * math.sin(math.radians(150)))

    draw_r = ImageDraw.Draw(red_layer)
    draw_r.ellipse(
        [
            (top_x - radius, top_y - radius),
            (top_x + radius, top_y + radius),
        ],
        fill=r_color,
    )

    draw_g = ImageDraw.Draw(green_layer)
    draw_g.ellipse(
        [
            (right_x - radius, right_y - radius),
            (right_x + radius, right_y + radius),
        ],
        fill=g_color,
    )

    draw_b = ImageDraw.Draw(blue_layer)
    draw_b.ellipse(
        [
            (left_x - radius, left_y - radius),
            (left_x + radius, left_y + radius),
        ],
        fill=b_color,
    )

    result = ImageChops.add(red_layer, green_layer)
    result = ImageChops.add(result, blue_layer)

    data = io.BytesIO()
    result.save(data, "png")
    data.seek(0)

    return data