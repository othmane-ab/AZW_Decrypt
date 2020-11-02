from fpdf import FPDF
import glob

pdf = FPDF()
# imagelist is the list with all image filenames
imagefiles = glob.glob("Book/*.png")
imagelist = []
for i in range(1000):
    image_ = f"Book/book_{i}.png"
    if image_ in imagefiles:
        imagelist.append(image_)
for i in range(0,len(imagelist),2):
    pdf.add_page(orientation="P")
    image = imagelist[i]
    pdf.image(image, 0, 0, 200, 150)
    if i+1<len(imagelist):
        image_2 = imagelist[i+1] 
        pdf.image(image_2, 0, 150, 200, 150)
pdf.output("Book_Test.pdf", "F")
