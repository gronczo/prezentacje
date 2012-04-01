import gfx

# zapis pliku na serwerze
def save_file(uploaded_file):
    print "-- helpers -- save_file() -- method call"
    upload_dir = "pdf_files/" # katalog do ktorego zapisujemy
    print "-- helpers -- save_file() -- uploaded file name: " + uploaded_file.name
    path = upload_dir + uploaded_file.name
    print "-- helpers -- save_file() -- write to: " + path
    destination = open(path, 'wb+')
    for chunk in uploaded_file.chunks():
        destination.write(chunk)
    destination.close()
    print "-- helpers -- safe_file() -- save completed "
    return path

# przerabia plik pdf na obrazy png
def convert(pdf_path, name):
    print "-- helpers -- convert() -- method call"
    upload_dir = "slide_files/"
    print "-- helpers -- convert() -- upload_dir: " + upload_dir

    file_list = list()

    try:
        doc = gfx.open("pdf", pdf_path)
        print "-- helpers -- convert() -- pages: " + str(doc.pages)

        for i in range(doc.pages):
            print "-- helpers -- convert() -- processing page number: " + str(i)
            img = gfx.ImageList()
            # img.setparameter("antialize", "1")
            page = doc.getPage(i+1)
            img.startpage(page.width, page.height) # okreslenie rozmiaru obrazu
            page.render(img)
            img.endpage()
            file_name = name + str(i) + ".png"
            print "-- helpers -- conver() -- file save to: " + file_name
            full_path = upload_dir + file_name
            img.save(full_path) # zapisanie obrazu
            file_list.append(file_name)
    except Exception as ex:
        print "Blad podczas konwertowania pdf do png"
        print "Klasa: convert, metoda: converter"
        print ex.message

    print "-- helpers -- convert() -- convert completed"
    return file_list

# wywolanie metody do konwersji
#convert(PDF_PATH, OUT_DIR, IMAGE_NAME)
