import math
from tkinter import *

def shifrlashMatn(matn, kalit):
    shifr = ""
    
    k_indx = 0
    matn_len = float(len(matn))
    matn_lst = list(matn)
    kalit_lst = sorted(list(kalit))
    ustun = len(kalit)
    qator = int(math.ceil(matn_len / ustun))
    fill_null = int((qator * ustun) - matn_len)
    matn_lst.extend('_' * fill_null)
 
    matritsa = [matn_lst[i: i + ustun] 
                for i in range(0, len(matn_lst), ustun)]

    for _ in range(ustun):
        curr_idx = kalit.index(kalit_lst[k_indx])
        shifr += ''.join([qator[curr_idx] 
                        for qator in matritsa])
        k_indx += 1

    royxat = ""
    for element in shifr:
        if element == '1':
            royxat += 'б'
        elif element == '2':
            royxat += 'и'
        elif element == '3':
            royxat += 'у'
        elif element == '4':
            royxat += 'т'
        elif element == '5':
            royxat += 'в'
        elif element == '6':
            royxat += 'о'
        elif element == '7':
            royxat += 'й'
        elif element == '8':
            royxat += 'с'
        elif element == '9':
            royxat += 'ч'
        else:
            royxat += element
    return royxat

def de_shifrlash(shifr, kalit):
    matn = ""
    k_indx = 0
    matn_indx = 0
    matn_len = float(len(shifr))
    matn_lst = list(shifr)
    ustun = len(kalit)
    qator = int(math.ceil(matn_len / ustun))
    kalit_lst = sorted(list(kalit))
    dec_shifr = []
    
    for _ in range(qator):
        dec_shifr += [[None] * ustun]

    for _ in range(ustun):
        curr_idx = kalit.index(kalit_lst[k_indx])

        for j in range(qator):
            dec_shifr[j][curr_idx] = matn_lst[matn_indx]
            matn_indx += 1
        k_indx += 1

    try:
        matn = ''.join(sum(dec_shifr, []))
    except TypeError:
        raise TypeError("Bu shifrni dastur ocha olmaydi",
                        "boshqa so'zni kiritib ko'ring.")

    null_count = matn.count('_')

    if null_count > 0:
        matn = matn[: -null_count]

    royxat = ""
    for element in matn:
        if element == 'б':
            royxat += '1'
        elif element == 'и':
            royxat += '2'
        elif element == 'у':
            royxat += '3'
        elif element == 'т':
            royxat += '4'
        elif element == 'в':
            royxat += '5'
        elif element == 'о':
            royxat += '6'
        elif element == 'й':
            royxat += '7'
        elif element == 'с':
            royxat += '8'
        elif element == 'ч':
            royxat += '9'
        else:
            royxat += element
    return royxat

def on_shifrlash_click():
    kalit = kalit_entry.get()
    matn = matn_entry.get()
    shifr = shifrlashMatn(matn, kalit)
    result_label.config(text=f"Shifrlangan matn:")
    result_entry.delete(0, END)
    result_entry.insert(0, shifr)

def on_de_shifrlash_click():
    kalit = kalit_entry.get()
    shifr = matn_entry.get()
    de_shifr_matn = de_shifrlash(shifr, kalit)
    result_label.config(text=f"De-Shifrlangan matn:")
    result_entry.delete(0, END)
    result_entry.insert(0, de_shifr_matn)

root = Tk()
root.title("jii shifrlash Ilhom Jabborov")
root.geometry("600x250")
root.resizable(False, False)


kalit_label = Label(root, text="Kalit so'zni kiriting:")
kalit_entry = Entry(root)

button1 = Button(root, text="Shifrlash", command=on_shifrlash_click)
button2 = Button(root, text="De-Shifrlash", command=on_de_shifrlash_click)

matn_label = Label(root, text="Matnni kiriting:")
matn_entry = Entry(root)

result_label = Label(root, text="Natija:")
result_label.config(font=("Helvetica", 12))

result_entry = Entry(root)


kalit_label.grid(row=0, column=0, padx=10, pady=10)
kalit_entry.grid(row=0, column=1, padx=10, pady=10)
matn_label.grid(row=1, column=0, padx=10, pady=10)
matn_entry.grid(row=1, column=1, padx=10, pady=10)
button1.grid(row=2, column=0, padx=10, pady=10)
button2.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=0, padx=10, pady=10)
result_entry.grid(row=3, column=1, padx=10, pady=10)


for i in range(2):
    root.columnconfigure(i, weight=1)
    



root.mainloop()


