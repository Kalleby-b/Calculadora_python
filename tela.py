import customtkinter as ctk



def inserir(n):
    numero_entry = str(entrada.get())
    algarismo = str(n)
    numero_completo = numero_entry + algarismo
    entrada.delete(0, ctk.END)
    entrada.insert(0,numero_completo )


def resultado():
    equacao= entrada.get()
    try:
        resposta = eval(equacao)
        lblCalculo.configure(text = equacao)
        lblResultado.configure(text = resposta)
        entrada.delete(0, ctk.END)
        print (resposta)
    except:
        lblResultado.configure(text = "Erro")
        entrada.delete(0, ctk.END)
        lblResultado.configure(text = "")
        lblCalculo.configure(text= '')
def apaga():
    entrada.delete(0 ,ctk.END)
    lblResultado.configure(text = "")
    lblCalculo.configure(text= '')



janela = ctk.CTk()
janela._set_appearance_mode('dark')
janela.title('calculadora')
janela.geometry('400x500')
janela.resizable(width= False, height= False)

#Label da expressão
lblCalculo= ctk.CTkLabel(janela, text="", font= ('arial bold', 16))
lblCalculo.place(x = 10, y=35)

lblResultado = ctk.CTkLabel(janela, text="", font=('arial bold', 32))
lblResultado.place(x = 100, y=35)
#Botões 

botao1 = ctk.CTkButton(janela, text ="  1  ",width=100 , height=50, command= lambda: inserir(1) ).place(x = 10, y = 110)

botao2 = ctk.CTkButton(janela, text ="  2  ",width=100 , height=50, command= lambda: inserir(2)).place(x = 120, y = 110)

botao3 = ctk.CTkButton(janela, text ="  3  ",width=100 , height=50, command= lambda: inserir(3)).place(x = 230, y = 110)

botao4 = ctk.CTkButton(janela, text ="  4  ",width=100 , height=50, command= lambda: inserir(4)).place(x = 10, y = 170)

botao5 = ctk.CTkButton(janela, text ="  5  ",width=100 , height=50, command= lambda: inserir(5)).place(x = 120, y = 170)

botao6 = ctk.CTkButton(janela, text ="  6  ",width=100 , height=50, command= lambda: inserir(6)).place(x = 230, y = 170)

botao7 = ctk.CTkButton(janela, text ="  7  ",width=100 , height=50, command= lambda: inserir(7)).place(x = 10, y = 230)

botao8 = ctk.CTkButton(janela, text ="  8  ",width=100 , height=50, command= lambda: inserir(8)).place(x = 120, y = 230)

botao9 = ctk.CTkButton(janela, text ="  9  ",width=100 , height=50, command= lambda: inserir(9)).place(x = 230, y = 230)

botao0 = ctk.CTkButton(janela, text ="  0  ",width=100 , height=50, command= lambda: inserir(0)).place(x = 10, y = 290)

botaoresposta = ctk.CTkButton(janela, text ="  =  ",width=100 , height=50, command= resultado).place(x = 120, y = 290)

btnlimpa = ctk.CTkButton(janela, text ="  AC  ",width=50 , height=50, command= apaga).place(x = 230, y = 290)

btnponto = ctk.CTkButton(janela, text ="  .  ",width=40 , height=50, command= lambda: inserir('.')).place(x = 290, y = 290)

btnsoma = ctk.CTkButton(janela, text='+',width=50 , height=50, command= lambda: inserir('+'))
btnsoma.place(x = 340, y = 110)

btnsubtrair = ctk.CTkButton(janela, text='-',width=50 , height=50, command= lambda: inserir('-'))
btnsubtrair.place(x = 340, y = 170)

btnmultiplicar = ctk.CTkButton(janela, text='*',width=50 , height=50, command= lambda: inserir('*'))
btnmultiplicar.place(x = 340, y = 230)

btndividir = ctk.CTkButton(janela, text='/',width=50 , height=50, command= lambda: inserir('/'))
btndividir.place(x = 340, y =  290)
#Caixas de texto

entrada = ctk.CTkEntry(janela, width=300 ,placeholder_text='Digite o primeiro numero... ')
entrada.place(x = 10, y=10)


janela.mainloop()