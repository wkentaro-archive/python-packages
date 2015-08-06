from vispy import scene
from vispy import app
from vispy import io
import numpy as np

canvas = scene.SceneCanvas(keys='interactive')
canvas.size = 600, 600
canvas.show()

# Set up a viewbox to display the image with interactive pan/zoom
view = canvas.central_widget.add_view()
view.camera.invert_y = False

# Load lena
img_data = io.imread('lena.png')
image = scene.visuals.Image(img_data, parent=view.scene)

# Set the view bounds to show the entire image with some padding
view.camera.rect = (-10, -10, image.size[0]+20, image.size[1]+20)

import sys
if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
