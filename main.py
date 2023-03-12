# Uma função para_one_hot(msg : str) para codificar mensagens como uma matriz usando one-hot encoding
# Uma função para_string(M : np.array) para converter mensagens da representação one-hot encoding para uma string legível
# Uma função cifrar(msg : str, P : np.array) que aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
# Uma função de_cifrar(msg : str, P : np.array) que recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
# Uma função enigma(msg : str, P : np.array, E : np.array) que faz a cifra enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
# Uma função de_enigma(msg : str, P : np.array, E : np.array) que recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.


import numpy as np

# def para_one_hot(msg: str) -> np.array:
#     alfabeto = "abcdefghijklmnopqrstuvwxyz"
#     size_msg = len(msg)
#     matriz = np.zeros((size_msg, 26))
#     for i in range(size_msg):
#         for j in range(26):
#             if msg[i] == alfabeto[j]:
#                 matriz[i][j] = 1
#     return matriz.T

def para_one_hot(msg: str) -> np.array:
   return np.array([[1 if msg[i] == ('abcdefghijklmnopqrstuvwxyz')[j] else 0 for j in range(26)] for i in range(len(msg))]).T

def para_string(M: np.array) -> str:
   return ''.join([('abcdefghijklmnopqrstuvwxyz')[np.where(M[:,i] == 1)[0][0]] for i in range(M.shape[1])])

def de_cifra(msg: str, M: np.array) -> str:
   return para_string(np.linalg.inv(M) @ para_one_hot(msg))