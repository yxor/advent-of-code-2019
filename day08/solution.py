
## part 1
with open("input.txt", "r") as f:
    inputs = f.read()

image_h = 6
image_w = 25
pixels = [inputs[i: i + image_w] for i in range(0, len(inputs), image_w)]
layers = [pixels[i: i + image_h] for i in range(0, len(pixels), image_h)]
least_0 = "".join(min(layers, key=lambda x: "".join(x).count('0')))

print(least_0.count('1') * least_0.count('2')) # 1474

## part 2

def decode_pixel(i, j, depth):
    if layers[depth][i][j] == '0' or layers[depth][i][j] == '1':
        return layers[depth][i][j]

    return decode_pixel(i, j, depth + 1)
message = []
for i in range(image_h):
    layer = []
    for j in range(image_w):
        layer.append(decode_pixel(i, j, 0))
    message.append(layer)

print("\n".join(["".join(pixel) for pixel in message])) # JCRCB

# visualising the image and saving it to a file
from PIL import Image

background = (0, 0, 0)

image = Image.new("RGB", (image_w, image_h), background)
pixels = image.load()

for i in range(image_h):
    for j in range(image_w):
        pixels[j, i] = (255, 255, 255) if message[i][j] == '1' else (0, 0, 0)

image.save("message.png")