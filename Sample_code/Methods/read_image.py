import base64

with open("D:/image path/CB-005_253.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print encoded_string