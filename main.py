import pandas as pd
import random
import math
import requests
from tkinter import *

def Inicio():
    cidades = vcidades.get()
    global df

    if cidades == 'Montes Claros':
        df = pd.read_excel('Montes_Claros.xlsx', engine='openpyxl')
    if cidades == 'Monte Azul':
        df = pd.read_excel('Monte_Azul.xlsx', engine='openpyxl')
    if cidades == 'Guanambi':
        df = pd.read_excel('Guanambi.xlsx', engine='openpyxl')

    global BuscarProduto
    global BuscarLoja
    global Cordx_loja
    global Cordy_loja
    global Cordx_cliente
    global Cordy_cliente


    BuscarProduto = df.Produto
    BuscarLoja = df.Loja

    Cordx_loja = df.Cordx
    Cordy_loja = df.Cordy

    Cordx_cliente = random.randint(-500, 501)
    Cordy_cliente = random.randint(-500, 501)


def Buscar():

    Inicio()
    lista_resultado.delete(0,END)
    busca = Bnome.get()
    contador = 0
    linha = 0
    terminar = 0

    qtd_linhas = df['Loja'].count()

    while (1):
        resultado_produto = BuscarProduto[linha]
        resultado_loja = BuscarLoja[linha]
        produto = busca.lower() in resultado_produto
        loja = busca.upper() in resultado_loja
        if produto or loja:
            Dx = Cordx_loja[linha]
            Dy = Cordy_loja[linha]
            Distancia = math.sqrt(((Dx - Cordx_cliente) ** 2) + ((Dy - Cordy_cliente) ** 2))
            lista_resultado.insert(END, '{:<15} {:<30}  R${:<10} à {:.0f}m de você'.format(df['Loja'][linha], df['Produto'][linha], df['Preço'] [linha], Distancia))
            print('{:<15} {:<30}  R${:<10} à {:.2f}m de você'.format(df['Loja'][linha], df['Produto'][linha], df['Preço'][linha], Distancia))
        else:
            contador = contador + 1
        linha = linha + 1

        if contador == qtd_linhas:
            lista_resultado.insert(END, 'produto não encontrado')
        if linha == qtd_linhas:
            break


app = Tk()
app.title('Onde q tem?')
app.geometry('500x400')

imagem_icone = PhotoImage(file= 'imagens/iconlogo.png')

texto_logo = Label(app, image= imagem_icone)
texto_logo.place(x = 155, y = 0, width = 180, height = 95,)

lista_cidades = ['Montes Claros','Monte Azul','Guanambi']
vcidades = StringVar()
vcidades.set(lista_cidades[0])
op_cidades = OptionMenu(app, vcidades, *lista_cidades)
op_cidades.place(x = 170, y = 95, width = 150, height = 30)

texto_orientação = Label(app, text= 'O que deseja procurar?')
texto_orientação.place(x = 170, y = 125, width = 150, height = 20)

Bnome = Entry(app)
Bnome.place(x = 90, y = 150, width = 300, height = 20)

imagem_lupa = PhotoImage(file= 'imagens/lupa.png')
botão_produto = Button(app, image= imagem_lupa, command= Buscar)
botão_produto.place(x = 230, y = 180, width = 32, height = 25)


lista_resultado = Listbox(app)
lista_resultado.place(x=50, y = 210, width = 400, height = 180)

app.mainloop()