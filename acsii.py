from PIL import Image

video_length = 218

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

def scale(image, new_width, new_height):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    if new_height == 0:
        new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def pixel2ascii(image, range_width=3.69):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def asciify(path, new_width=100, new_height=30):
    image = Image.open(path)
    image = scale(image, new_width, new_height)
    image = image.convert('L')

    pixels_to_chars = pixel2ascii(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)


if __name__=='__main__':
    import os
    import time 
    import cv2
    vidcap = cv2.VideoCapture('badapple.mp4')
    time_count = 0
    frames = []
    while time_count <= video_length*1000:
        vidcap.set(0, time_count)
        success, image = vidcap.read()
        if success:
            cv2.imwrite('output.jpg', image)
        frames.append(asciify('output.jpg'))
        time_count = time_count + 100

    f = open('play.txt', 'w')
    f.write('SPLIT'.join(frames))
    f.close()