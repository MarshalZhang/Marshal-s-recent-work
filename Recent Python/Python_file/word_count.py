def count_word(filename):
    try:
        with open(filename) as f_obj:
            contents= f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words=contents.split()
        print("The file "+ filename +" has about"+ str(len(words))+"words")
    
filenames=["toefl.txt", "Marshal.txt","level.txt"]
for i in filenames:
    count_word(i)

def count(filename,searchword):
    n=0
    try:
        with open(filename,"r") as f_obj:
            contents= f_obj.read()
    except FileNotFoundError:
        print("This file does not exist")
    else:
        words=contents.lower().split()
        for i in words:
            if i ==str(searchword):
                n+=1
        print("the number of '"+searchword,"' in your file is", n)
        
count("toefl.txt","the")       
