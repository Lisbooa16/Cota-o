from Cotação.func import Cotacao
from tkinter import *
from tkinter import ttk
import tkinter as tk

cotacao = Cotacao('Euro')

class exemplo:
    def __init__(self, tk):
        self.frame1 = Frame(tk)
        self.frame2 = Frame(tk)


        self.frame1.pack()
        self.frame2.pack()

        self.val = Text(self.frame2, height=1, width=22)
        self.val.pack()
        moeda = str(self.val.get(1.0, "end-1c"))
        print(moeda)
        self.cotacao = Cotacao(moeda)


        self.valor = self.cotacao.cotacao()

        self.aviso = Label(self.frame2, text=f'{self.valor}')
        self.aviso.pack()

        self.es_C1 = IntVar() #self.es_NomeVariável = IntVar(), explico o que é IntVar() lá embaixo.
        self.C1 = Button(tk, text = "Atualizar",  height=2,
                 width = 15, command=self.marcada)
        self.C1.pack()


    def marcada(self):
        cotacao = Cotacao(str(self.val.get(1.0, "end-1c")).replace(" ","-"))
        self.aviso['text'] = cotacao.cotacao()

ex = Tk()
ex.geometry('275x100')
ex.title("cotação moeda")
# ex.iconphoto(True, tk.PhotoImage(file=r'C:\Users\guilherme.lisboa\Downloads\1175277.png'))
exemplo(ex)
ex.mainloop()

