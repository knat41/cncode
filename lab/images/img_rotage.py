from PIL import Image

# Open the image
image = Image.open('happy.png')

# Rotate the image by 45 degrees clockwise and fill the area outside of the image with white color
rotated_image = image.rotate(45, fillcolor='#FFF')

# Save the rotated image
rotated_image.save('rotated-output.jpg')