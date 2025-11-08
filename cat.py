import car
from PIL import Image
import requests
import numpy as np
from io import BytesIO

# Download an image of a cat
url = "https://st4.depositphotos.com/11342552/41908/i/450/depositphotos_419081616-stock-photo-cute-little-red-cat-young.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert("RGB")

# Convert to NumPy array
cat_array = np.array(img)

print("Shape:", cat_array.shape)
print("Dtype:", cat_array.dtype)

# Display the image
car.plot(cat_array)
