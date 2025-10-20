import tkinter as tk 
from tkinter import messagebox  

# Variáveis globais para o jogo 
root = None  
tabuleiro = [['' for _ in range(3)] for _ in range(3)] 
jogador_atual = 'X'  # Começa com X
score_x = 0  # Pontos do X
score_o = 0  # Pontos do O
jogo_ativo = True  # Se o jogo está rolando
botoes = [[None for _ in range(3)] for _ in range(3)]  # Lista para os botões
label_x = None  # Label do placar X
label_o = None  # Label do placar O

# Função para criar toda a interface (chamada no início)
def criar_interface():
    global root, label_x, label_o 

    root = tk.Tk()
    root.title("Jogo da Velha !") 
    root.geometry("500x550")  
    root.resizable(False,False)
    root.configure(bg="#B0C4DE")  # Cor de fundo cinza claro
    
    #  Placar dos jogadores
    # Label para pontos do X
    label_x = tk.Label(root, text="X: 0", font=("Helvetica", 14), 
                       bg="#f0f0f0", fg="#000080")  # Azul harmonioso
    label_x.grid(row=0, column=0, padx=20, pady=10, sticky="w") 
    
    # Título no meio
    titulo = tk.Label(root, text="Jogo da Velha", font=("Mongolian Baiti", 16,), 
                      bg="#ADD8E6", fg="#333333")
    titulo.grid(row=0, column=1, pady=10)  
    
    # Label para pontos do O
    label_o = tk.Label(root, text="O: 0", font=("Helvetica", 14), 
                       bg="#f0f0f0", fg="#4a90e2")
    label_o.grid(row=0, column=2, padx=20, pady=10, sticky="e")  
    
    #Tabuleiro 3x3
    for i in range(3):  
        for j in range(3):  
   
            btn = tk.Button(root, text="", font=("Helvetica", 32), width=5, height=2,
                            bg="#ffffff", fg="#333333", 
                            command=lambda row=i, col=j: fazer_jogada(row, col)) 
            btn.grid(row=i+1, column=j, padx=2, pady=2)  
            botoes[i][j] = btn 
    
  
    # Botão Reiniciar Partida
    btn_reiniciar = tk.Button(root, text="Reiniciar Partida", font=("Helvetica", 12),
                              bg="#1E90FF", fg="white", width=15,
                              command=reiniciar_partida)  # Chama função
    btn_reiniciar.grid(row=4, column=0, pady=20, padx=10)
    
    # Botão Zerar Placar
    btn_zerar = tk.Button(root, text="Zerar Placar", font=("Helvetica", 12),
                          bg="#1E90FF", fg="white", width=15,
                          command=zerar_placar)
    btn_zerar.grid(row=4, column=1, pady=20, padx=10)
    
    # Botão Créditos
    btn_creditos = tk.Button(root, text="Créditos", font=("Helvetica", 12),
                             bg="#1E90FF", fg="white", width=15,
                             command=mostrar_creditos)
    btn_creditos.grid(row=4, column=2, pady=20, padx=10)
    
    # Atualiza o placar no início
    atualizar_placar()

def fazer_jogada(row, col):
    global jogador_atual, jogo_ativo 
    
    # Verifica se pode jogar
    if not jogo_ativo or tabuleiro[row][col] != '':
        return  # Sai se inválido
    
   
    tabuleiro[row][col] = jogador_atual
    botoes[row][col].config(text=jogador_atual) 
    
    # Verifica vitória
    if verificar_vitoria(jogador_atual):
        messagebox.showinfo("Vitória!", f"O jogador {jogador_atual} ganhou! 🎉")
        atualizar_placar_vitoria()
        jogo_ativo = False
        desabilitar_botoes()  
        return
    
    # Verifica empate
    if verificar_empate():
        messagebox.showinfo("Empate!", "Deu empate! Jogue de novo. ")
        jogo_ativo = False
        desabilitar_botoes()
        return
    
    # Troca jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Função para verificar vitória (simples, com ifs)
def verificar_vitoria(jogador):
    # Linhas
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    # Colunas
    for j in range(3):
        if tabuleiro[0][j] == jogador and tabuleiro[1][j] == jogador and tabuleiro[2][j] == jogador:
            return True
    # Diagonal principal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    # Diagonal secundária
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Função para verificar empate
def verificar_empate():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '':
                return False  # Tem espaço vazio
    return True  # Cheio

# Função para somar pontos na vitória
def atualizar_placar_vitoria():
    global score_x, score_o
    if jogador_atual == 'X':
        score_x += 1
    else:
        score_o += 1
    atualizar_placar()

# Função para atualizar os labels do placar
def atualizar_placar():
    global label_x, label_o
    label_x.config(text=f"X: {score_x}")
    label_o.config(text=f"O: {score_o}")

# Função para desabilitar botões (melhoria simples)
def desabilitar_botoes():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(state="disabled")

# Função para reiniciar a partida
def reiniciar_partida():
    global tabuleiro, jogador_atual, jogo_ativo
    # Limpa tabuleiro
    tabuleiro = [['' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    jogo_ativo = True
    
    # Limpa e reabilita botões
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")

#  zerar placar
def zerar_placar():
    global score_x, score_o
    score_x = 0
    score_o = 0
    atualizar_placar()
    reiniciar_partida()  

def mostrar_creditos():
    credits = """
    Jogo da Velha -
    
    Feito por: Anny Do nascimento Bento
    Turma: Densenvolvimento de Sistemas, sala 18
    Professor(a): Alexandre Tolentino
    
    Versão:0.1
    Data:  09/10/2025
    """
    messagebox.showinfo("Créditos do Projeto", credits)


if __name__ == "__main__":
    criar_interface()  # Cria tudo
    root.mainloop()  # Inicia o funcionamento