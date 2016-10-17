# tweets/views.py
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
# for image and graphics only
from PIL import Image
import random
from PIL import ImageDraw


class AboutView(TemplateView):
    template_name = "tweets/test.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context = {'last_name': 'Julius',
                   'first_name': 'Cesar',
                   'birth_year': '--98'}
        return context


class TimeView(TemplateView):
    template_name = "tweets/time.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context = {'now': datetime.datetime.now()}
        return context


def daytime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'tweets/time.html', context)

"""
def daytime(request):
    now = datetime.datetime.now()
    html = "Now it is  {:s}".format(str(now))
    return HttpResponse(html)
"""


def index(request):
    return HttpResponse("Hello world, you are at MyTweets")


def about(request):
    context = {'last_name': 'Augustus',
               'first_name': 'Emperor',
               'birth_year': '-88'}
    return render(request, 'tweets/test.html', context)


def month(request, numberstr):
    try:
        nr = int(numberstr)
    except ValueError:
        raise Http404()
    if nr < 1 or nr > 12:
        raise Http404
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
    month = months[nr-1]
    html = "The month {} is the {}".format(nr, month)
    return HttpResponse(html)


def day(request, numberstr):
    try:
        nr = int(numberstr)
    except ValueError:
        raise Http404()
    if nr < 1 or nr > 7:
        raise Http404
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    context = {'day_name': days[nr-1], 'day_number': nr, 'days': days}
    return render(request, 'tweets/day.html', context)


def image(request):
    # effbot.org/zone/django-pil.htm
    # http://djangobook.com/generating-non-html-content/
    INK = "red", "blue", "green", "yellow"
    # ... create/load image here ...
    image = Image.new("RGB", (400, 300), random.choice(INK))
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response


def graphics(request):
    # PIL.ImageDraw.Draw.rectangle(xy, fill=None, outline=None)
    INK = "red", "blue", "green", "yellow", "cyan", "lightpink", "lightgray"
    image = Image.new("RGB", (800, 600), "lightblue")
    draw = ImageDraw.Draw(image)
    # ... draw graphics here ...
    for i in range(20):
        x0 = random.randint(0, image.size[0])
        y0 = random.randint(0, image.size[1])
        x1 = random.randint(0, image.size[0])
        y1 = random.randint(0, image.size[1])
        draw.rectangle([x0, y0, x1, y1], fill=random.choice(INK), outline="black")
        # http://pillow.readthedocs.io/en/3.3.x/reference/ImageDraw.html
        # http://quickies.seriot.ch/?id=256
    del draw
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response


def pil_image(request):
    # https://bradmontgomery.net/blog/django-generating-an-image-with-pil/
    size = (100, 50)             # size of the image to create
    im = Image.new('RGB', size)  # create the image
    draw = ImageDraw.Draw(im)    # create a drawing object that is
    # used to draw on the new image
    red = (255, 0, 0)            # color of our text
    text_pos = (10, 10)          # top-left position of our text
    text = "Hello World!"        # text to draw
    # Now, we'll do the drawing:
    draw.text(text_pos, text, fill=red)

    del draw        # I'm done drawing so I don't need this anymore

    # We need an HttpResponse object with the correct mimetype
    response = HttpResponse(content_type="image/png")
    # now, we tell the image to save as a PNG to the
    # provided file-like object
    im.save(response, 'PNG')
    return response  # and we're done!
