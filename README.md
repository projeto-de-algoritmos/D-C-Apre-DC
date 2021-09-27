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

(2^64)−1 =  18.446.744.073.709.551.615 de movimentos. Vamos supor que os sacerdotes façam um movimento por segundo, logo o tempo estimado seria de 584.942.417.355  anos para terminar! Claramente esse problema é mais complexo do que aparenta e se você para para pensa, no final tudo de trata de um PG(Progressão geometrica). Como  já  se  passaram  perto  de  12 bilhões  de anos  desde  o  início  do  universo, ainda  nos  resta  um  tempinho, da até para jogar umas partidas de xadrez no [chess.com](chess.com) de vez enquando. 😂🤣😂🤣


## Resolução
 
&emsp;&emsp; A princípio já vem algumas perguntas automáticas, como podemos desenvolver uma solução para esse problema? e recursivamente pior ainda! Qual o caso base? Para a resposta dessa pergunta vamos usar o algoritmo de dividir para conquistar, vamos começar pensando em resolver o problema completo, ok, agora vamos quebrar o problemas em problemas menores que é mais facil de resolver, como exemplo iremos pegar um torre com 4 discos, então vamo começar a quebrar, resolver um torre de 4 pinos é trivial? no caso não ok, vamos quebrar para um torre com 3 discos, e agora? Ok, então quebramos para 2 discos e finalmente para uma, onde a resolução é trivial, que no caso a gente apenas movimenta o discos do pino de origem para o pino de destino, então agora só voltamos às chamadas anteriores, como agora fiz com um disco, também consigo fazer com 2 discos, na próxima consigo fazer com 3 e aí por diante, pode ter ficado um pouco confuso, mas vou deixar um colinha abaixo para entender melhor como que funciona o algoritmo.
 
* 1 passo: Mova a torre de (altura − 1) para o pino intermediário, usando o pino destino como intermediário.
 
* 2 passo: Mova o disco restante para o pino destino.
 
* 3 Mova a torre de altura−1 do pino intermediário para o pino destino usando o pino origem como intermediário.
 
Contanto que sempre obedeçamos a regra de que os discos maiores permanecem na parte inferior da pilha, podemos usar as três etapas acima recursivamente, tratando discos maiores como se eles nem estivessem lá. Para melhor entendimento temo uma solução pronta, para conseguir acessar siga o passo abaixo.
 
Acesse o [link](https://github.com/projeto-de-algoritmos/D-C-Apre-DC) e procure a sessão de uso/solução, siga o passo a passo e rode a solução proposta.
 
## Desafio
 
 
&emsp;&emsp; Para um melhor entendimento temos um desafio para vocês, com esses conhecimentos você já tem condições de resolver um desafio com 5 ou mais discos, e aí aceita o desafio? Para rodar o desafio siga os seguintes passos.
 
Acesse o [link](https://github.com/projeto-de-algoritmos/D-C-Apre-DC) e procure a sessão de uso/make play, siga o passo a passo e complete o desafio.

