# Batalha Naval é um clássico jogo de estratégia para dois jogadores. Cada jogador posiciona 
# seus navios num grid 10 x 10, e cada rodada do jogo consiste em adivinhar as posições dos navios do adversário. 
# Existem muitas variações das regras, mas tais regras são irrelevantes para esse problema. Estamos interessados 
# num problema mais básico: Dada a lista dos navios e suas posições, você deve determinar se o posicionamento inicial é válido.
# As linhas e colunas do tabuleiro são numeradas de 1 a 10, e os navios são posicionados na horizontal ou na 
# vertical, ocupando uma sequência contígua de quadrados do tabuleiro. Para esse problema, um posicionamento é válido se:
#     · nenhuma posição é ocupada por mais de um navio;
#     · e todos os navios estão inteiramente contidos no tabuleiro.