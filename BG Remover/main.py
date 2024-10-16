from rembg import remove 
from PIL import Image 

input_path =  './img1.jpg' 
output_path = './out.png' 
  
# Processing the image 
input = Image.open(input_path) 
  
# Removing the background from the given Image 
output = remove(input) 
  
#Saving the image in the given path 
output.save(output_path) 
