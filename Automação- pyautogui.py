# Biblioteca 

import pyautogui
import time

# Temporizador de tempo ( Pausa)  
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link da Escola 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Aguardar por 3 segundos blaya.mendonca@gmail.com  sua senha
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email com latitude e longitude 
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("blaya.mendonca@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
# entrar 
pyautogui.click(x=955, y=638) # clique no botao de login
# Aguardar 3 segundos 
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

# Puxando e lendo a Tabela csv 
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto usando for Loop 
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela e a coluna que queremos preencher 
    codigo = tabela.loc[linha, "codigo"]
    # preencher e escrever no campo 
    pyautogui.write(str(codigo))
    # passar para a proxima etapa e apertar 
    pyautogui.press("tab")
    # preencher e escrever os campo buscando a colunas e dando tab
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    # Se não encontrar 
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # Fazer rolagem  de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
