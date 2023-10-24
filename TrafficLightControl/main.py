# Controle de Semáforo

# O Departamento de Trânsito de uma cidade deseja implementar um sistema de controle de semáforo em um ponto crítico da cidade. 
# Este sistema de semáforo é composto por três cores: vermelho, amarelo e verde, representadas por valores binários 1 e 0. 
# Cada cor tem sua própria entrada binária para verificar seu status:

# Vermelho: 1 para ligado, 0 para desligado.
# Amarelo: 1 para ligado, 0 para desligado.
# Verde: 1 para ligado, 0 para desligado.

# O semáforo deve operar de acordo com as seguintes regras:
# ●    Se todas as entradas estiverem desligadas (0), deverá apresentar a mensagem: Semáforo desligado! E o Status: 0 0 0
 
# ●      Se apenas uma entrada estiver ligada (1), o semáforo deverá exibir qual cor está ligada: Vermelho ON! E o Status: 1 0 0
 
# ● Se mais de uma entrada estiver ligada ao mesmo tempo, deverá apresentar a mensagem: Entrada inválida!
# Dada as instruções, seu objetivo é escrever um programa em Python que, dado o status das três cores, determine qual cor deve 
# ser exibida no semáforo.