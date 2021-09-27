# Introdução
&emsp;&emsp;Nesse tópico abordaremos o algoritmo "Dividir para Conquistar", a solução para esse algoritmo consiste nos seguintes passos.
 
  * Passo 1: O problema dado é dividido em pequenos problemas.
  * Passo 2: Cada pequeno problema é resolvida separadamente.(Nesse segundo passo normalmente utilizamos chamadas recursivas que é  parte da conquista)
  * Passo 3: As soluções de problemas menores são combinadas para assim produzir uma solução mais robusta.
 
Abaixo podemos ver essa imagem ilustrativa do algoritmo.


<center>

<audio controls>
  <source src="https://github.com/projeto-de-algoritmos/D-C-Apre-DC/blob/gh-pages/assets/audios/fluxo.m4a?raw=true" type="audio/mpeg">
</audio>

</center>


<center>

![](https://raw.githubusercontent.com/projeto-de-algoritmos/D-C-Apre-DC/gh-pages/images/fluxo.png)

[Imagem 1: Fluxo de como funciona o algoritmo](https://raw.githubusercontent.com/projeto-de-algoritmos/D-C-Apre-DC/gh-pages/images/fluxo.png)

</center>


# Questão Problema

## Entendimento do problema e um pouco da historia.


&emsp;&emsp; A torre de Bramanismo, mais conhecida como torre de hanói, é um dos problemas clássicos da matemática, que é possível se aplicar o algoritmos de dividir para conquistar, esse problema foi inventado em 1883 pelo matemático francês Edouard Lucas. Esse problema tem uma inspiração direta com um lenda hindu que conta que os sacerdotes receberam três pinos e um conjunto de 64 discos de ouro, sendo cada disco um menor que o outro. O objetivo é transferir todos os 64 discos de um dos 3 pinos para o outro, e nunca poderá colocar um disco maior em cima de um disco menor. Segundo a lenda, depois que esses sacerdotes finalizarem esse grande desafio, o templo se desmoronaria e o mundo desapareceria. 

<center>

![](https://raw.githubusercontent.com/projeto-de-algoritmos/D-C-Apre-DC/gh-pages/images/Torre-de-hanoi.png)

[Imagem 2: Torre de hanoi](https://raw.githubusercontent.com/projeto-de-algoritmos/D-C-Apre-DC/gh-pages/images/Torre-de-hanoi.png)

</center>

## Conflito cognitivo

&emsp;&emsp; Uma das perguntas seria, "mais é bem simples resolver isso não?", aparentemente não parece ser algo difícil, mas vocês vão ver o quão complexo é essa resolução. Ok iremos usar um pouco da matemática para fazer algumas estimativas de beleza? Existe uma fórmula matemática que mostra a quantidade de movimentos mínimos para resolver esse problema, esse termo é bem conhecido na matemática, que seria (2^N)-1, vamos calcular que tempo que os sacerdotes demorariam para acabar esse desafio, ficaria o seguinte. 

Por exemplo:
* Para solucionar o jogo com 3 discos, são necessários 7 movimentos.

* Para solucionar o jogo com 4 discos, são necessários 15 movimentos.
* Para solucionar o jogo com 7 discos, são necessários 127 * movimentos.
* Para solucionar o jogo com 15 discos, são necessários 32.767 movimentos.
* Para solucionar o jogo com 64 discos, são necessários 18.446.744.073.709.551.615 movimentos.

(2^64)−1 =  18.446.744.073.709.551.615 de movimentos. Vamos supor que os sacerdotes façam um movimento por segundo, logo o tempo estimado seria de 584.942.417.355  anos para terminar! Claramente esse problema é mais complexo do que aparenta e se você para para pensa, no final tudo de trata de um PG(Progressão geometrica). Como  já  se  passaram  perto  de  12 bilhões  de anos  desde  o  início  do  universo, ainda  nos  resta  um  tempinho, da até para jogar umas partidas no chess.com de vez enqundo. 😂🤣😂🤣


## Resolução




