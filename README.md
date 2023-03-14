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
5. [Modelo Matemático](#modelo-matemático)
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

## Modelo Matemático
Para cifrar uma mensagem usando Enigma, a matriz de permutação de cada vetor é aplicada à mensagem em ordem. Isso é feito da seguinte maneira:

### Criptografia
Para a criptografia, utilizamos a função 'Enigma', a qual é usada para criptografar uma mensagem usando as matrizes de enigma e de permutação fornecidas.

A ideia principal da função é criar uma matriz one-hot a partir da mensagem de entrada, aplicar a matriz de permutação à primeira coluna e, para cada coluna subsequente, aplicar a matriz de enigma E à matriz resultante da multiplicação da matriz one-hot correspondente com todas as matrizes de enigma anteriores usando o operador @ de multiplicação de matriz.

A função começa convertendo a mensagem de entrada em uma matriz one-hot usando a função 'para_one_hot', que retorna uma matriz de tamanho (27, m), onde m é o número de caracteres na mensagem de entrada. A matriz resultante é transposta usando o método '.T.'.

Em seguida, a primeira coluna da matriz one-hot é embaralhada aplicando a matriz de permutação P à primeira coluna da matriz one-hot. A matriz de permutação é multiplicada com a primeira coluna da matriz one-hot usando o operador @ de multiplicação de matriz.

Para cada coluna subsequente da matriz one-hot, a função percorre as matrizes de enigma, aplicando uma matriz de enigma a cada coluna subsequente da matriz one-hot. A matriz de enigma é aplicada usando o operador @ de multiplicação de matriz. A função 'reduce' é usada para aplicar as matrizes de enigma em ordem, começando com a segunda coluna da matriz one-hot e terminando com a última coluna.

A função 'np.vstack' é usada para concatenar as colunas processadas da matriz one-hot em uma matriz resultante 'final'. A função 'np.vstack' adiciona uma nova linha a cada iteração do loop for, que é formada pela aplicação das matrizes de enigma às colunas da matriz one-hot.

O resultado final é uma matriz de tamanho (27, m), onde m é o número de caracteres na mensagem original, contendo a representação one-hot da mensagem cifrada. A matriz resultante é transposta e convertida de volta para uma string usando a função 'para_string', que retorna uma string correspondente à mensagem cifrada.

#### Matematicamente:
A função enigma pode ser expressa em equações matemáticas da seguinte forma:

- Seja msg uma string de tamanho m contendo a mensagem original. 
- Seja P uma matriz de permutação 27 x 27. 
- Seja E uma matriz de enigma 27 x 27. 
- Seja hotMessage uma matriz 27 x m representando a mensagem original na forma one-hot, onde cada coluna corresponde a um caractere da mensagem.

A matriz cifrada resultante final pode ser calculada da seguinte forma:

1. Transpor a matriz hotMessage para obter uma matriz m x 27.

    $hotMessage^T = [h_1, h_2, \cdots, h_m]$

2. Calcular o produto matricial P @ hotMessage[0] para obter a primeira coluna da matriz cifrada final.

    $final[:,0] = P \cdot hotMessage^T_{:,0}$

3. Para as colunas restantes de hotMessage, calcular o produto matricial E @ x em um loop usando a função reduce para obter cada coluna correspondente de final.

    $final[:,i] = \left(\prod_{j=0}^{i-1} E \right) \cdot P \cdot hotMessage^T_{:,i}$

4. Converter a matriz cifrada final em uma string usando a função para_string.

    $cifra = para_string(final^T)$

### Decriptografia
A decriptografia com Enigma segue uma lógica parecida com processo da criptografia. Sendo que essa é usada para descriptografar uma mensagem cifrada usando as matrizes de enigma e de permutação fornecidas. <br>
O objetivo da função é reverter a cifragem feita pela função enigma, que converteu a mensagem original em uma matriz one-hot, aplicou a matriz de permutação à primeira coluna e, para cada coluna subsequente, aplicou a matriz de enigma E à matriz resultante da multiplicação da matriz one-hot correspondente com todas as matrizes de enigma anteriores usando o operador @ de multiplicação de matriz.

A função começa convertendo a mensagem cifrada em uma matriz one-hot usando a função para_one_hot, que retorna uma matriz de tamanho (27, m), onde m é o número de caracteres na mensagem cifrada.

Em seguida, a primeira coluna da matriz one-hot é desembaralhada aplicando a matriz de permutação inversa np.linalg.inv(P) à primeira coluna da matriz one-hot. A matriz de permutação inversa é encontrada usando a função np.linalg.inv, que calcula a matriz inversa de uma matriz quadrada.

Para cada coluna subsequente da matriz one-hot, a função percorre as matrizes de enigma de trás para frente, aplicando a matriz inversa de cada uma delas à coluna correspondente da matriz one-hot. O resultado da aplicação da matriz inversa de cada matriz de enigma é usado como entrada para a matriz inversa da matriz de permutação np.linalg.inv(P). A função reduce é usada para aplicar as matrizes inversas em ordem reversa, começando com a última matriz de enigma e terminando na primeira.

O resultado final é uma matriz de tamanho (27, m), onde m é o número de caracteres na mensagem cifrada, contendo a representação one-hot da mensagem original. A mensagem original é obtida convertendo a matriz de volta para uma string usando a função para_string, que retorna uma string correspondente à mensagem original.

#### Matematicamente:

Ela recebe três parâmetros: uma string msg representando a mensagem cifrada, uma matriz de permutação P e uma matriz de enigma E.

A matriz decifrada resultante final pode ser calculada da seguinte forma:

Seja msg uma matriz 27 x m representando a mensagem cifrada na forma one-hot, onde cada coluna corresponde a um caractere da mensagem.

1. Para a primeira coluna de msg, calcular o produto matricial da matriz inversa de P com a primeira coluna de msg.

    $final[:,0] = P^{-1} \cdot msg^T_{:,0}$

2. Para as colunas restantes de msg, calcular o produto matricial da matriz inversa de E multiplicada por todas as colunas anteriores de msg (usando a função reduce) com a matriz inversa de P e adicionar a coluna correspondente a final.

    $final[:,i] = P^{-1} \cdot \left(\prod_{j=0}^{i-1} E^{-1} \right) \cdot msg^T_{:,i}$

3. Converter a matriz decifrada final em uma string usando a função para_string.

     $cifra = para_string(final^T)$

<b>Portanto, a equação matemática geral para a função de_enigma seria: </b>

Dada uma mensagem cifrada msg, uma matriz de permutação P e uma matriz de enigma E, a mensagem original pode ser obtida pela seguinte equação:

$final[:,0] = P^{-1} \cdot msg^T_{:,0}$

$final[:,i] = P^{-1} \cdot \left(\prod_{j=0}^{i-1} E^{-1} \right) \cdot msg^T_{:,i}$

$cifra = para_string(final^T)$

## Como rodar

Para rodar o demo da biblioteca Enigma, siga as instruções abaixo:

### Como instalar a biblioteca
1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Para instalar a biblioteca, execute o seguinte comando no terminal:
    ```bash
    pip install git+https://github.com/liviatanaka/criptografia_Enigma
    ```

### Como rodar a API
1. Certifique-se de que o Python 3 ou superior está instalado no seu computador.
2. Clone ou faça o download do repositório no seu computador.
    #### 2.1 Clonar o repositório:
    Primeiramente, é necessário que se clone o repositório do projeto. <br>
    <b> Obs.: </b> Se você não sabe como clonar um repositório, não tem problema! Basta seguir o link a seguir para resolver isso:                              "https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository"
3. Acesse a pasta raiz do projeto no terminal.
4. Instalar dependências:
    #### 4.1 Após ter o repositório em sua máquina, é necessário que se instale as dependências as quais o projeto utiliza para o seu funcionamento. Para isso, é necessário que, com o projeto aberto em seu editor de código (VS Code, Intelli J, etc.), seja criado um terminal e que esse esteja também esteja com o diretório do projeto aberto (utilizar comandos 'cd' - Windows ou 'ls' - Linux) para muder de diretório.
    #### 4.2 Certifique-se de que você tem o pip (gerenciador de pacotes Python) instalado. Caso contrário, você pode instalá-lo utilizando o comando sudo apt install python-pip (para sistemas baseados em Debian/Ubuntu) ou sudo yum install python-pip (para sistemas baseados em CentOS/Fedora).
    #### 4.3 Com o diretório do projeto no terminal, podemos baixar todas as dependências necessárias. Para isso, utilize o seguinte comando: <br>
    ``` 
    pip install -r requirements.txt 
    ```
      Esse comando instalará todas as dependências especificadas no arquivo "requirements.txt" automaticamente.
  
     #### 4.4 Aguarde até que todas as dependências sejam instaladas. Isso pode levar algum tempo, dependendo do número de pacotes listados e suas respectivas dependências.
     #### 4.5 Depois que todas as dependências forem instaladas com sucesso, você poderá executar o seu projeto Python normalmente, sem se preocupar com a falta de pacotes necessários.
 
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

## Rotas da API

`https://localhost:5000`

| Funcionalidade | URL path |
| --- | --- |
| Cifra| /enygma/encrypt/cifra |
| De_Cifra | /enygma/decrypt/de-cifra |
| Enigma | /enygma/encrypt/enigma |
| De_Enigma | /enygma/decrypt/de-enigma |
| Para_OneHot | /enygma/encrypt/onehot | 
| Para_String | /enygma/decrypt/string |
