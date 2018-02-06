import time
from kütüphane import *
print("""
İşlemler;

1. Show Books

2. Search Book

3. Insert Book

4. Delete Book

5.Update Book

quit 'q'
***********************************""")

lib = libary()

while True:
    işlem = input("Process:")

    if (işlem == "q"):
        print("End")
        lib.cclose()
        break
    elif (işlem == "1"):
        lib.show()

    elif (işlem == "2"):
        isim = input("Name of Book:? ")
        print("Searching...")
        time.sleep(2)

        lib.detect(isim)
    elif (işlem == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        cat = input("Categories:")
        page = int(input("Page:"))

        newone = book(name,author,publisher,cat,page)
        #object
        print("Processing")
        time.sleep(2)

        lib.Insert(newone)
        print("done")


    elif (işlem == "4"):
        name=input("name:")

        ans = input("Are You Sure ? (Y/N)")
        if (ans == "Y"):
            print("Deleting...")
            time.sleep(2)
            lib.delbook(name)
            print("Book Eliminated....")


    elif (işlem == "5"):
        name=input("Name:")
        time.sleep(2)
        lib.updatebook(name)
        print("Completed....")

    else:
        print("nope")







