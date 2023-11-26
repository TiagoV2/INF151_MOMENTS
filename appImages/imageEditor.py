from PIL import Image

def resize_image(input_path, output_path, size=(48, 48)):
    image = Image.open(input_path)
    resized_image = image.resize(size, Image.Resampling.LANCZOS)
    resized_image.save(output_path)

if __name__ == "__main__":
    resize_image("name.png", "profile.png")

