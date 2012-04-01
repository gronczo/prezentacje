import gfx
from fabric.api import *
import os

def save_on_server(file, dir):
    file_path = dir + file.name
    print "-- helpers -- save_on_server() -- zapis pliku: " + file_path
    destinantion = open(file_path, 'wb+')
    for chunk in file.chunks():
        destinantion.write(chunk)
    destinantion.close()

    return file_path

def convert(file_path, presentation_id, dir):
    print "-- helpers -- convert() -- wywolanie metody"
    doc = gfx.open("pdf", file_path)

    slide_list = list()

    for i in range(doc.pages):
        img = gfx.ImageList()
        page = doc.getPage(i + 1)
        img.startpage(page.width, page.height)
        page.render(img)
        img.endpage()
        name = str(presentation_id) + "_" + str(i) + ".png"
        path = dir + str(presentation_id) + "_" + str(i) + ".png"
        img.save(path)
        slide_list.append(name)
        print "-- helpers -- convert -- zapis pliku: " + path

    return slide_list

def collect_static():
    cmd = 'python manage.py collectstatic -v0 --noinput'
    result = os.system(cmd)
    print "-- helpers -- colect_static() -- result: " + str(result)

