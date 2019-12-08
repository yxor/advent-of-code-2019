
## part 1
with open("input.txt", "r") as f:
    inputs = f.read()

image_h = 6
image_w = 25
pixels = [inputs[i: i + image_w] for i in range(0, len(inputs), image_w)]
layers = [pixels[i: i + image_h] for i in range(0, len(pixels), image_h)]
least_0 = "".join(min(layers, key=lambda x: "".join(x).count('0')))

print(least_0.count('1') * least_0.count('2')) # 1474
