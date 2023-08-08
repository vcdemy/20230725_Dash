from dash import Dash, html
import matplotlib.pyplot as plt
import numpy as np
import base64

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y)
fig.savefig('test.png')

def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
      image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

print(b64_image('test.png'))

app = Dash(__name__)
app.layout = html.Img(src=b64_image('test.png'))

if __name__=="__main__":
   app.run(debug=True)

