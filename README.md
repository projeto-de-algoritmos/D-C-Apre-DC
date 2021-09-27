# Introdução
&emsp;&emsp;Nesse topico abordaremos o algoritmo "Dividir para Conquitar", a solução para esse algoritimo consiste nos seguintes passos.

   * Passo 1: O problema dado é dividido em pequenos problemas.
   * Passo 2: Cada pequeno problema é resolvida separadamente.(Nesse segundo passo normalmente ultizamos chamadas recussivas que é  parte da conquita)
   * Passo 3: As soluções do problemas menores são combinadas para assim produzir uma solução mais robusta.

Abaixo podemos ver essa imagem inlustrativa do algoritmo.

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


&emsp;&emsp; A torre de Bramanismo, mais conhecida como torre de hanoi é um dos problemas classicos da matematico, que é possivel se aplicar o algoritimos de dividir para conquitar, esse problema foi inventado em 1883 pelo matemático franceês Edouard Lucas. Esse problema tem uma inspiração direta com um lenda hindu que conta que os sacerdotes receberam três pinos e um conjunto de 64discos de ouro, sendo cada disco um menor que o outro. O objetivo é transferir todos os 64 discos de um dos 3 pinos para o outro, e nunca poderá colocar um disco maior em cima de um disco menor. Segundo a lenda depois que esses sacerdotes finalizarem esse grande desafio, o templo se desmonaria e o mundo desapareceria.

## Conflito cognitivo

&emsp;&emsp; Uma das perguntas seria, "mais é bem simples resolver isso não?", aparentemente não parece ser algo dificil, mas vocês vão ver o quão complexo é essa resolução. Ok iremos usar um pouco da matematica para fazer algumas estimativas beleza? Existe uma formula matematica que mostra a quantidade de movimentos minimos para resolver esse problema, esse termo é bem conhecido na matematica, que seria (2^N)-1, vamos calcular que tempo que os sacerdotes demoraria para acabar esse desafio, ficaria o seguinte. (2^64)−1 = 18,446,744,073,709,551,615 de movimentos. Vamos supor que os sacerdotes façam um movimento por segundo, logo o tempo estimado seria de 584.942.417.355  anos para terminar! Claramente esse problema é mais complexo do que aparenta.


## Resolução




