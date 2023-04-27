import PIL.Image
import fitz
import io

pdf = fitz.open("./merged.pdf")
count = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img.save(open(f"./output/image{count}.{extension}", "wb"))
        count += 1