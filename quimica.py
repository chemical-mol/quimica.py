from molmass import Formula
from molmass import ELEMENTS, Element
from tkinter import *
from tkinter import ttk


class chemical:

  def prosses(self):
    #___________________massa e composição_________________________
    self.mas_comp = self.caixa_mol.get()
    self.formula = Formula(self.mas_comp)
    self.my_var = self.formula.mass
    self.comp = self.formula.composition()
    self.ap_mol.config(text=f'{self.my_var} g/mol')
    self.ap_comp.config(text=f'{self.comp} ')
    print(self.my_var)

  #________________________Elementos_______________________________

  def elemento(self):
    self.element = self.caixa_elem.get()
    pass

  #_________________________________________________________________

  def __init__(self, master):

    self.tela_entrar = Tk()
    self.tela_entrar.geometry('300x450+300+100')
    self.tela_entrar.resizable(width=0, height=0)
    self.tela_entrar.title('DATA BASE')
    self.note = ttk.Notebook(self.tela_entrar)
    self.note.place(x=5, y=0, width=290, height=440)

    #frame MOLECULA

    self.tela1 = Frame(self.tela_entrar,
                       bg='#D8E1FF',
                       borderwidth=2,
                       relief='sunken')
    self.note.add(self.tela1, text='MOLÉCULA')

    #____________inicio___________________

    #____________parte do pross__________
    self.nome_mol = Label(self.tela1,
                          text='INFORME A MOLÉCULA: ',
                          bg='#D8E1FF')
    self.nome_mol.place(x=55, y=5)
    self.caixa_mol = Entry(self.tela1,
                           )  #caixa de massa molecular e composição
    self.caixa_mol.place(x=40, y=25, width=200)

    self.caixa_elem = Entry(self.tela1, )  #caixa para Elementos
    self.caixa_elem.place(x=40, y=200, width=200)

    #________________________________
    #ligação com def
    self.my_var = StringVar()
    self.mas_comp = ""
    self.element = ""
    #________________________________

    self.ap_mol = Label(self.tela1, text='Massa Molar g/mol ', bg='#D8E1EE')
    self.ap_mol.place(x=60, y=60)  #massa molar

    self.ap_comp = Label(self.tela1, text='Composição', bg='#D8E1EE')
    self.ap_comp.place(x=40, y=100)  #composição

    self.botao = Button(self.tela1, text="massa", command=self.prosses)
    self.botao.place(x=60, y=350)

    #self.botao = Button(self.tela1, text="elemento", command=self.elemento)
    #self.botao.place(x=120, y=350)

    self.tela_entrar.mainloop()


root = Tk()
chemical(root)
