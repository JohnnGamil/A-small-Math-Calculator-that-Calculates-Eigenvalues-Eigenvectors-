from tkinter import *
import numpy as np
from tkinter import messagebox

np.set_printoptions(suppress=True)

window = Tk()
window.title("Matrix")
window.geometry("800x500+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)

wrapper1 = LabelFrame(window, text="WELCOME!")
wrapper1.pack(fill="both", expand="yes", padx=30, pady=5)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []


# callback function to get your StringVars
def get_mat():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())

    print(matrix)
    a = np.array(matrix, dtype=float)
    eigenvals, eigenvecs = np.linalg.eig(a)
    messagebox.showinfo("showinfo",f"Eigen Values: {eigenvals}\n\nEigen Vectors: {eigenvecs}")
    print(eigenvals)
    print(eigenvecs)

    

Label(wrapper1, text="Enter A Matrix For 'Eigenvalues & Eigenvectors' :", font=('arial', 10, 'bold'),
      bg="bisque2").place(x=20, y=20)


def press():
    top1 = Toplevel()
    top1.title('The TEAM')
    top1.geometry("800x700")
    top1.configure(bg='AntiqueWhite1')
    wrapper4 = LabelFrame(top1, text="WELCOME!")
    wrapper4.pack(fill="both", expand="yes", padx=30, pady=5)
    num0 = Label(wrapper4, text="Dr.Eng.Mostafa Reda ", font=("Helvetica", 30))
    num11 = Label(wrapper4, text="TEAM: ", font=("Helvetica", 25))
    num1 = Label(wrapper4, text="  Abdulrahman khaled      20190803 ", font=("Helvetica", 25))
    num2 = Label(wrapper4, text="  Zeyad Mostafa               20200208 ", font=("Helvetica", 25))
    num3 = Label(wrapper4, text="  Mira Ihab                       20201234 ", font=("Helvetica", 25))
    num4 = Label(wrapper4, text="  Rana mohamed             20200182 ", font=("Helvetica", 25))
    num5 = Label(wrapper4, text="Mazen Ahmed                 20200407 ", font=("Helvetica", 25))
    num6 = Label(wrapper4, text="  George Hana                 20200130 ", font=("Helvetica", 25))
    num7 = Label(wrapper4, text="  Yara Muhammad saad  20200629 ", font=("Helvetica", 25))
    num8 = Label(wrapper4, text="  Mohamed Hassan         20200441 ", font=("Helvetica", 25))
    num9 = Label(wrapper4, text="  John Fady                     20200133 ", font=("Helvetica", 25))
    num10 = Label(wrapper4, text="   Aly Eyad                       20200331 ", font=("Helvetica", 25))


    num0.grid(row=0, column=1)
    num11.grid(row=1, column=1)
    num1.grid(row=2, column=1)
    num2.grid(row=3, column=1)
    num3.grid(row=4, column=1)
    num4.grid(row=5, column=1)
    num5.grid(row=6, column=1)
    num6.grid(row=7, column=1)
    num7.grid(row=8, column=1)
    num8.grid(row=9, column=1)
    num9.grid(row=10, column=1)
    num10.grid(row=11, column=1)



x2 = 0
y2 = 0
rows, cols = (3, 3)
for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(StringVar())
        entries[i].append(Entry(wrapper1, textvariable=text_var[i][j], width=3))
        entries[i][j].place(x=60 + x2, y=50 + y2)
        x2 += 30

    y2 += 30
    x2 = 0

button = Button(wrapper1, text="Submit", bg='bisque3', width=15, command=get_mat)
button.place(x=160, y=140)

button = Button(wrapper1, text="INFO", bg='bisque3', width=15, command=press)
button.place(x=200, y=400)

window.mainloop()