# Descrição do problema

***Pedra***, ***papel*** e ***tesoura*** é um jogo com dois ***participantes***. O jogo tem ***rodadas***. Em cada rodada, um participante escolhe um símbolo de pedra, papel ou tesoura, e o outro participante faz o mesmo. O vencedor da rodada é determinado pela comparação dos símbolos escolhidos. As regras do jogo estabelecem que ***pedra ganha de tesoura***, ***tesoura vence (corta) papel*** e ***papel vence (embrulha) pedra***. O vencedor da rodada recebe um ***ponto***. O jogo continua pela ***quantidade de rodadas*** que os participantes combinarem. O vencedor é o participante com o ***maior número de pontos***.

| Fase | Ator | Comportamento | Dados |
| -------- | -------- | -------- | -------- |
| Entrada | Jogador | Escolhe símbolo | Símbolo salvo como **escolha** em Jogador (choice) |
| Processando | GameRound | Compara a escolha tendo em mente as regras do jogo | **Resultado** inspecionado |
| Processando | GameRound | Recebe pontos com base no valor do resultado | **Pontos** adicionados ao Jogador(point) vencedor |
| Processando | Game | Verificar resposta continuar | A resposta é true, continuar; caso contrário, sair |
| Saída | Game | Nova crédito de rodada do jogo ou fim do jogo |  |

| Comportamento | Método | Ator |
|---|---|---|
| Escolhe um símbolo | escolher() | Jogador |
| Compara opções | compararEscolha() | Rodada |
| Recebe pontos | atribuirPontos() | Rodada |
| Verificar resposta continuar | checarCondicaoFinal() | Jogo |
| Crédito final do jogo | determinarVencedor() | Jogo |


| Escolha | Pedra | Papel | Tesoura |
|---|---|---|---|
| Pedra | 0 | -1 | 1 |
| Papel | 1 | 0 | -1 |
| Tesoura | -1 | 1 | 0 |
