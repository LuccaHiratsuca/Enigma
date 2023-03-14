# Projeto Enigma

APS 2 - Algebra Linear e Teoria da Informação - 2023.1

# 1.Integrantes:
* [Felipe Maluli de Carvalho Dias](https://github.com/FeMCDias)
* [Lucca Hiratsuca Costa](https://github.com/LuccaHiratsuca)

# Indice
1. [Introdução](#introdução)
2. [Descrição do Projeto](#descrição-do-projeto)
3. [Implementação](#implementação)
4. [Funções implementadas na biblioteca](#funções-implementadas-na-biblioteca)
5. [Equações implementadas](#equações-implementadas)
6. [Como rodar](#como-rodar)
7. [Como instalar a biblioteca](#como-instalar-a-biblioteca)
8. [Como rodar a API](#como-rodar-a-api)
9. [Demonstração da biblioteca](#demonstração-da-biblioteca)
10. [Rotas da API](#rotas-da-api)


## Introdução
A biblioteca em Python que estamos apresentando permite a criptografia e descriptografia de mensagens utilizando o algoritmo Enigma. Seu principal objetivo é atender à demanda da APS 2 da disciplina de Álgebra Linear e Teoria da Informação do curso de Ciência da Computação do Insper, ministrada pelo professor Tiago Fernandes Tavares.

A criptografia é um processo importante para garantir a segurança da informação e proteger a privacidade dos dados. O algoritmo Enigma, que foi utilizado pela Alemanha durante a Segunda Guerra Mundial para criptografar mensagens militares, é um exemplo clássico de criptografia. A biblioteca em Python que desenvolvemos é baseada nesse algoritmo e oferece uma maneira eficiente de criptografar e descriptografar mensagens.

Além de ser uma solução prática para a APS 2 da disciplina de Álgebra Linear e Teoria da Informação, a biblioteca em Python que desenvolvemos pode ser utilizada por qualquer pessoa ou organização que deseje criptografar suas comunicações de forma segura e confiável. Ela é fácil de usar e pode ser integrada em qualquer projeto em Python.

Por fim, é importante destacar que a segurança da criptografia não depende apenas do algoritmo utilizado, mas também da forma como ele é implementado e utilizado. Por isso, é importante tomar medidas adicionais para proteger a privacidade dos dados, como usar chaves seguras e implementar protocolos de segurança adequados.

## Descrição do Projeto
O algoritmo Enigma é um método de criptografia que utiliza uma cifra de substituição polialfabética. Essa cifra é construída a partir de uma série de rotores, que são discos com contatos elétricos que permitem codificar letras em uma mensagem. Cada rotor é uma permutação dos caracteres do alfabeto e, quando combinados em uma ordem específica, formam a cifra Enigma.

A complexidade da cifra Enigma se deve ao fato de que os rotores são rotativos e possuem um deslocamento aleatório, o que significa que a permutação dos caracteres muda a cada letra codificada. Além disso, os rotores são conectados de tal forma que cada letra da mensagem passa através deles de uma maneira não linear e altamente complexa. Essa complexidade é amplificada ainda mais pelo uso de um painel de plugues que altera ainda mais a configuração dos rotores.

A matemática por trás do algoritmo Enigma é extremamente complexa, e sua criptografia e descriptografia são baseadas em um conjunto de equações altamente não lineares. Essas equações são difíceis de serem resolvidas por meios convencionais, o que torna a cifra Enigma altamente segura. No entanto, durante a Segunda Guerra Mundial, a equipe de criptoanalistas liderada por Alan Turing conseguiu quebrar a cifra Enigma, o que foi fundamental para o esforço de guerra dos Aliados.

Em resumo, a cifra Enigma é um dos exemplos mais famosos de criptografia, e seu uso durante a Segunda Guerra Mundial ressalta a importância da segurança da informação e do desenvolvimento contínuo de técnicas avançadas de criptografia.

## Implementação
A biblioteca que estamos apresentando é uma implementação da cifra Enigma que utiliza matrizes de permutação para representar os rotores. A cifra é construída aplicando a matriz de permutação correspondente a cada rotor em ordem, o que permite codificar as letras da mensagem de forma segura e confiável.

Além disso, a biblioteca inclui funções para codificar mensagens como matrizes usando one-hot encoding, o que facilita o processamento da mensagem durante o processo de criptografia. Esse método de codificação converte cada letra em uma matriz com uma única posição definida como 1, e todas as outras posições definidas como 0. Esse formato é conveniente para o processamento da mensagem através dos rotores da cifra Enigma.

A biblioteca também inclui funções para converter as matrizes de volta em mensagens legíveis, o que permite a descriptografia da mensagem após a criptografia. Essas funções permitem que a mensagem original seja recuperada de forma fácil e eficiente.

Em resumo, a biblioteca que desenvolvemos é uma implementação eficiente da cifra Enigma, que utiliza matrizes de permutação para representar os rotores. Além disso, a inclusão de funções para codificar e decodificar mensagens como matrizes simplifica o processo de criptografia e descriptografia. Essa biblioteca pode ser utilizada por estudantes de criptografia, pesquisadores e desenvolvedores interessados em implementar a cifra Enigma em seus projetos.
## Funções implementadas na biblioteca:
* `para_one_hot(msg)`: Função para codificar mensagens como uma matriz usando one-hot encoding
* `para_string(M)`: Função para converter mensagens da representação one-hot encoding para uma string legível
* `cifrar(msg, P)`: Função que aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
* `de_cifrar(msg, P)`: Função que recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
* `enigma(msg, P, E)`: Função que faz a cifra enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
* `de_enigma(msg, P, E)`: Função que recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.

## Equações implementadas
Para cifrar uma mensagem usando Enigma, a matriz de permutação de cada rotor é aplicada à mensagem em ordem. Isso é feito da seguinte maneira:

### Criptografia
A criptografia com Enigma envolve uma série de operações realizadas em uma mensagem de texto, incluindo permutações e substituições de letras. A implementação deste repositório utiliza duas matrizes de permutação, P e E, para realizar a cifra Enigma.

A função enigma recebe como entrada uma mensagem de texto, a matriz P e a matriz E, e retorna a mensagem cifrada. Para cada letra da mensagem, a função realiza as seguintes operações:

1. Transforma a mensagem em uma matriz one-hot encoding.

    ```bash
        matriz_msg = para_one_hot(msg)
    ```

2. Multiplica a coluna da respectiva letra na matriz da mensagem pela matriz da permutação P.

    ```bash
        letra_cifrada = P @ coluna_letra
    ```

3. Concatena a matriz resultante à matriz final da mensagem cifrada.

    ```bash
        matriz_enigma = np.concatenate((matriz_enigma, letra_cifrada), axis=1)
    ```
4. Multiplica a matriz de permutação P pela matriz E.

    ```bash
        P = E @ P
    ```

Ao final das operações, a função retorna a mensagem cifrada em texto.

### Decriptografia
A decriptografia com Enigma segue o mesmo processo da criptografia, porém com a ordem das matrizes de permutação invertida. A função de_enigma recebe como entrada uma mensagem cifrada, a matriz P e a matriz E, e retorna a mensagem original. Para cada letra da mensagem cifrada, a função realiza as seguintes operações:

1. Transforma a letra cifrada em uma matriz one-hot encoding.
2. Multiplica a matriz da letra pela matriz inversa de P.
3. Concatena a matriz resultante à matriz final da mensagem 4.original.
4. Multiplica a matriz de permutação P pela matriz E.

Ao final das operações, a função retorna a mensagem original em texto.

### Funções auxiliares

As funções auxiliares para a biblioteca de criptografia enigma incluem `limpa_mensagem`, que transforma uma mensagem em minúsculas, remove acentos e substitui caracteres especiais por "_", e `cria_matriz`, que recebe uma chave, realiza uma rotação e cria uma matriz de codificação usando o novo alfabeto.

## Como rodar

Para rodar o demo da biblioteca Enigma, siga as instruções abaixo:

## Como instalar a biblioteca
1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Para instalar a biblioteca, execute o seguinte comando no terminal:
    ```bash
    pip install git+https://github.com/liviatanaka/criptografia_Enigma
    ```

## Como rodar a API
1. Certifique-se de que o Python 3 ou superior está instalado no seu computador.
2. Clone ou faça o download do repositório no seu computador.
3. Acesse a pasta raiz do projeto no terminal.
4. Instale as dependências da biblioteca com o comando:
    ```bash
    pip install -r requirements.txt
    ```
5. Execute o seguinte comando para rodar o demo:
    ```bash
    python app.py
    ```
Isso iniciará o servidor Flask e o demo estará disponível no endereço http://localhost:5000.
Para demonstração rápida, consulte o arquivo [teste_api.ipynb](teste_api.ipynb).

## Demonstração da biblioteca
Para aprender a usar a biblioteca enigmalille, consulte o arquivo [teste_biblioteca.ipynb](teste_biblioteca.ipynb). Nele, você encontrará exemplos de como cifrar e decifrar diferentes tipos de mensagens usando as funções disponíveis, incluindo:

* Mensagens comuns
* Mensagens contendo caracteres que não pertencem ao alfabeto
* Mensagens vazias

## 10. Rotas da API

`https://localhost:5000`

| Funcionalidade | URL path |
| --- | --- |
| Cifra| /enygma/encrypt/cifra |
| De_Cifra | /enygma/decrypt/de-cifra |
| Enigma | /enygma/encrypt/enigma |
| De_Enigma | /enygma/decrypt/de-enigma |
| Para_OneHot | /enygma/encrypt/onehot | 
| Para_String | /enygma/decrypt/string |
