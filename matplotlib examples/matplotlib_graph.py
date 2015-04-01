import matplotlib.pyplot as plt
from io import BytesIO
import PIL
import PIL.Image

from django.http import HttpResponse


def test_graph(request):
    x = [1,2,3,4,5,6]
    y = [5,6,7,2,9,7]
    
    plt.plot(x,y, linewidth = 2)    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('sample graph')
    plt.grid(True)
    
    buffer = io.BytesIO()

    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    
    graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, 'PNG')
    
    plt.close()
    
    response = HttpResponse(buffer.getvalue(), content_type = 'image/png')
    return response