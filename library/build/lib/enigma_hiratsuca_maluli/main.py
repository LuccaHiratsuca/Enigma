# Uma função para_one_hot(msg : str) para codificar mensagens como uma matriz usando one-hot encoding
# Uma função para_string(M : np.array) para converter mensagens da representação one-hot encoding para uma string legível
# Uma função cifrar(msg : str, P : np.array) que aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
# Uma função de_cifrar(msg : str, P : np.array) que recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
# Uma função enigma(msg : str, P : np.array, E : np.array) que faz a cifra enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
# Uma função de_enigma(msg : str, P : np.array, E : np.array) que recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.


import numpy as np
from functools import reduce

def para_one_hot(msg: str) -> np.array:
    return np.array([[1 if {letra: indice for indice, letra in enumerate('abcdefghijklmnopqrstuvwxyz ')}[j] == i else 0 for i in range(27)] for j in msg.lower()]).T
    
def para_string(M: np.array) -> str:
    return ''.join({indice: letra for indice, letra in enumerate('abcdefghijklmnopqrstuvwxyz ')}[i] for i in np.argmax(M, axis=0))

def cifra(msg: str, M: np.array) -> str:
    return para_string(M @ para_one_hot(msg))

def de_cifra(msg: str, M: np.array) -> str:
   return para_string(np.linalg.inv(M) @ para_one_hot(msg))

def enigma(msg: str, P: np.array, E: np.array) -> str:
    try:
        hotMessage = para_one_hot(msg).T
        final = P @ hotMessage[0]
        for i in range(1,hotMessage.shape[0]):
            final = np.vstack((final, reduce(lambda x, _: E @ x, range(i), P @ hotMessage[i]).T))
        return para_string(final.T)
    except:
        return 'Erro: Matriz não invertível'

def de_enigma(msg: str, P: np.array, E: np.array) -> str:
    try:
        msg = para_one_hot(msg).T
        final = np.linalg.inv(P) @ msg[0]
        for i in range(1,msg.shape[0]):
            final = np.vstack((final, np.linalg.inv(P) @ reduce(lambda x, _: np.linalg.inv(E) @ x, range(i), msg[i])))
        return para_string(final.T)
    except:
        return 'Erro: Matriz não invertível'