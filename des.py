import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics

# Função para selecionar o arquivo CSV
def selecionar():
    caminho = filedialog.askopenfilename(
        title='Selecione o arquivo CSV',
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )
    return caminho

# Função para plotar gráfico de barras em uma nova janela
def data_plot():
    caminho = selecionar()
    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()

        # Criar nova janela para o gráfico de barras
        nova_janela = tk.Toplevel()
        nova_janela.title('Gráfico de Barras')
        
        # Criar uma figura para o gráfico
        fig = plt.Figure()
        grafico = fig.add_subplot(111)
        grafico.bar(vendedor, vendas)

        # Widget para exibir a figura na nova janela
        canvas = FigureCanvasTkAgg(fig, master=nova_janela)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Atualizar a interface gráfica
        nova_janela.mainloop()

# Função para plotar gráfico de dispersão em uma nova janela
def data_plot1():
    caminho = selecionar()
    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()

        # Criar nova janela para o gráfico de dispersão
        nova_janela = tk.Toplevel()
        nova_janela.title('Gráfico de Dispersão')
        
        # Criar uma figura para o gráfico
        fig = plt.Figure()
        grafico = fig.add_subplot(111)
        grafico.scatter(vendedor, vendas)

        # Widget para exibir a figura na nova janela
        canvas = FigureCanvasTkAgg(fig, master=nova_janela)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Atualizar a interface gráfica
        nova_janela.mainloop()

# Função para plotar gráfico de linha em uma nova janela
def data_plot2():
    caminho = selecionar()
    if caminho:
        dados = pd.read_csv(caminho)
        vendedor = dados['vendedor'].to_list()
        vendas = dados['vendas'].to_list()

        # Criar nova janela para o gráfico de linha
        nova_janela = tk.Toplevel()
        nova_janela.title('Gráfico de Linha')
        
        # Criar uma figura para o gráfico
        fig = plt.Figure()
        grafico = fig.add_subplot(111)
        grafico.plot(vendedor, vendas)

        # Widget para exibir a figura na nova janela
        canvas = FigureCanvasTkAgg(fig, master=nova_janela)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Atualizar a interface gráfica
        nova_janela.mainloop()

# Função para plotar gráfico de pizza em uma nova janela
def data_plot3():
    caminho = selecionar()
    if caminho:
        dados = pd.read_csv(caminho)
        vendas = dados['vendas'].to_list()
        labels = dados['vendedor'].to_list()

        # Criar nova janela para o gráfico de pizza
        nova_janela = tk.Toplevel()
        nova_janela.title('Gráfico de Pizza')
        
        # Criar uma figura para o gráfico
        fig = plt.Figure()
        grafico = fig.add_subplot(111)
        grafico.pie(vendas, labels=labels, autopct='%1.2f%%')

        # Widget para exibir a figura na nova janela
        canvas = FigureCanvasTkAgg(fig, master=nova_janela)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Atualizar a interface gráfica
        nova_janela.mainloop()

# Função para calcular estatísticas
def calcular_estatisticas():
    caminho = selecionar()
    if caminho:
        dados = pd.read_csv(caminho)
        vendas = dados['vendas'].to_list()

        # Calcular estatísticas
        media = statistics.mean(vendas)
        mediana = statistics.median(vendas)
        moda = statistics.mode(vendas)
        desvio_padrao = statistics.stdev(vendas)

        # Exibir resultados
        print(f"Média: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        print(f"Desvio Padrão: {desvio_padrao}")

# Interface gráfica com tkinter
janela = tk.Tk()

# Botões para os gráficos
btn1 = tk.Button(janela, text='Plot Bar', command=data_plot)
btn1.pack(pady=5)

btn2 = tk.Button(janela, text='Plot scatter', command=data_plot1)
btn2.pack(pady=5)

btn3 = tk.Button(janela, text='Plot Line', command=data_plot2)
btn3.pack(pady=5)

btn4 = tk.Button(janela, text='Plot Pie', command=data_plot3)
btn4.pack(pady=5)

# Botão para estatísticas
btn5 = tk.Button(janela, text='Estatística', command=calcular_estatisticas)
btn5.pack(pady=5)

janela.mainloop()