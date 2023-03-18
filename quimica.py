from molmass import Formula
from molmass import ELEMENTS, Element
from tkinter import *
from tkinter import ttk
from mendeleev import element




class chemical:

  def prosses(self):
    try:
      #___________________massa e composição_________________________
      self.mas_comp = self.caixa_mol.get()
      self.formula = Formula(self.mas_comp)
      self.my_var = self.formula.mass
      self.comp = self.formula.composition()
      self.atom = self.formula.atoms
      self.ap_mol.config(text=f'{self.my_var} g/mol')
      self.ap_comp.config(text=f'{self.comp} ')
      self.ap_atom.config(text=f'existe(m) {self.atom} átomo(s)')

    except Exception:
      self.ap_mol.config(text=f'ALGO FOI DIGITADO INCORRETAMENTE')
      self.ap_comp.config(text=f'VERIFIQUE O QUE FOI ESCRITO ')
      self.ap_atom.config(
        text=f'SOMETHING WAS ENTERED INCORRECTLY,\n CHECK WHAT WAS WRITTEN')

  #________________________Elementos_______________________________


#FRAME TELA1

  def elemento(self):  #FRAME TELA2
    try:
      self.t_elem = self.caixa_elem.get()
      self.p_elem = ELEMENTS[self.t_elem]  #MOLMASS
      self.p_elem_mendeleev = element(self.t_elem)  #MENDELEEV
      self.nome_e = self.p_elem.name
      self.simbolo = self.p_elem.symbol
      self.conf = self.p_elem.eleconfig
      self.e_conf = self.p_elem_mendeleev.oxistates  #mendeleev
      self.atomic = self.p_elem_mendeleev.atomic_weight  #mendeleev
      self.ap_elem.config(text=f'{self.nome_e}')
      self.ap_simb.config(text=f'{self.simbolo}')
      self.ap_conf.config(text=f'{self.conf}')
      self.ap_confe.config(text=f'{self.e_conf}')
      self.ap_atomic.config(text=f'{self.atomic}')
    except:
      self.ap_elem.config(text=f'ALGO FOI DIGITADO INCORRETAMENTE')
      self.ap_simb.config(text=f'VERIFIQUE O QUE FOI ESCRITO ')
      self.ap_conf.config(
        text=f'SOMETHING WAS ENTERED INCORRECTLY,\n CHECK WHAT WAS WRITTEN')
      self.ap_confe.config(text=f'Erro!')
      self.ap_atomic.config(text=f'Erro!')

  #___ ______________________________________________________________

  

  def __init__(self, master):

    self.tela_entrar = Tk()
    self.tela_entrar.geometry('300x450+300+100')
    self.tela_entrar.resizable(width=0, height=0)
    self.tela_entrar.title('DATA BASE')
    self.note = ttk.Notebook(self.tela_entrar)
    self.note.place(x=5, y=0, width=290, height=440)

    #frame COMPOSTO

    self.tela1 = Frame(self.tela_entrar,
                       bg='#D8E1FF',
                       borderwidth=2,
                       relief='sunken')
    self.note.add(self.tela1, text='COMPOSTO')
    self.tela2 = Frame(self.tela_entrar,
                       bg='#D8E1FF',
                       borderwidth=2,
                       relief='sunken')
    self.note.add(self.tela2, text='ELEMENTO')

   
    #____________inicio___________________

    #caixas entry
    self.nome_mol = Label(self.tela1,
                          text='INFORME O COMPOSTO: ',
                          bg='#D8E1FF')
    self.nome_mol.place(x=55, y=5)
    self.caixa_mol = Entry(self.tela1,
                           )  #caixa de massa molecular e composição
    self.caixa_mol.place(x=40, y=25, width=200)

    #________________________________
    #ligação com def

    self.mas_comp = ""

    self.element = ""

    #________________________________

    self.ap_mol = Label(self.tela1, text='Massa Molar g/mol ', bg='#D8E1EE')
    self.ap_mol.place(x=20, y=60)  #massa molar

    self.ap_comp = Label(self.tela1, text='Composição', bg='#D8E1EE')
    self.ap_comp.place(x=20, y=100)  #composição

    self.ap_atom = Label(self.tela1, text="Quant de Átomos", bg='#D8E1EE')
    self.ap_atom.place(x=20, y=190)  #átomos

    self.botao = Button(self.tela1, text="Processar", command=self.prosses)
    self.botao.place(x=60, y=350)

    #________________tela2________________
    self.nome_elem = Label(self.tela2,
                           text='INFORME O ELEMENTO: ',
                           bg='#D8E1FF')
    self.nome_elem.place(x=55, y=5)
    self.caixa_elem = Entry(self.tela2,
                            )  #caixa de massa molecular e composição
    self.caixa_elem.place(x=40, y=25, width=200)

    self.ap_elem = Label(self.tela2, text='NOME DO ELEMENTO ', bg='#D8E1EE')
    self.ap_elem.place(x=20, y=60)

    self.ap_simb = Label(self.tela2, text='SIMBOLO ', bg='#D8E1EE')
    self.ap_simb.place(x=20, y=120)

    self.ap_conf = Label(self.tela2, text='ELETRO CONFIGURAÇÃO ', bg='#D8E1EE')
    self.ap_conf.place(x=20, y=180)

    self.ap_confe = Label(self.tela2, text='ESTADO DE OXIDAÇÃO', bg='#D8E1EE')
    self.ap_confe.place(x=20, y=240)

    self.ap_atomic = Label(self.tela2, text='PESO ATÔMICO', bg='#D8E1EE')
    self.ap_atomic.place(x=20, y=300)

    self.botao = Button(self.tela2, text="Processar", command=self.elemento)
    self.botao.place(x=60, y=350)
    #____________________________________
    
    self.tela_entrar.mainloop()

root = Tk()
chemical(root)
