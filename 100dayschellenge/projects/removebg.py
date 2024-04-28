from rembg import remove
from PIL import Image
input_path = '/home/mani/Desktop/mani-demo-new-1/100dayschellenge/wp5457083-780130089.jpg'
output_path = '/home/mani/Desktop/mani-demo-new-1/100dayschellenge/wp5457083-780130089.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)