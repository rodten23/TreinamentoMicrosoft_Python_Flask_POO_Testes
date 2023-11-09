class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.escolha = ''

    def escolher(self):
        self.escolha = input('{nome}, selecione pedra, papel, tesoura, lagarto ou Spock: '.format(nome = self.nome))
        print('{nome} selecionou {escolha}'.format(nome = self.nome, escolha = self.escolha))

    def escolhaEmNumerico(self):
        switcher = {
            'pedra': 0,
            'papel': 1,
            'tesoura': 2,
            'lagarto': 3,
            'spock': 4
        }
        return switcher[self.escolha]
    
    def atribuirPontos(self):
        self.pontos += 1

class Rodada:
    def __init__(self,j1, j2):
        self.regras = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]

        j1.escolher()
        j2.escolher()

        resultado = self.compararEscolhas(j1,j2)
        print('Resultado da rodada é {resultado}'.format(resultado = self.resultadoComoString(resultado)))

        if resultado > 0:
            j1.atribuirPontos()
        elif resultado < 0:
            j2.atribuirPontos()


    def compararEscolhas(self, j1, j2):
        return self.regras[j1.escolhaEmNumerico()][j2.escolhaEmNumerico()]
    
    def resultadoComoString(self, resultado):
        res = {
            0: 'empate',
            1: 'venceu',
            -1: 'perdeu'
        }
        return res[resultado]
    
    def atribuirPontos(self):
        print('Feito!')

class Jogo:
    def __init__(self):
        self.fimJogo = False
        self.jogador = Jogador('Rodrigo')
        self.segundoJogador = Jogador('Leonardo')

    def iniciar(self):
        while not self.fimJogo:
            Rodada(self.jogador, self.segundoJogador)
            self.checarCondicaoFinal()

    def checarCondicaoFinal(self):
        perguntar = input('Continuar jogo? s/n: ')
        if perguntar == 's':
            Rodada(self.jogador, self.segundoJogador)
            self.checarCondicaoFinal()
        else:
            print('Jogo encerrado! {j1nome} ficou com {j1pontos} e {j2nome} terminou com {j2pontos}.'.format(j1nome = self.jogador.nome, j1pontos = self.jogador.pontos, j2nome = self.segundoJogador.nome, j2pontos = self.segundoJogador.pontos))
            self.determinarVencedor()
            self.fimJogo = True

    def determinarVencedor(self):
        resultadoString = 'É um empate!'
        if self.jogador.pontos > self.segundoJogador.pontos:
            resultadoString = '{nome} é o Vencedor!'.format(nome=self.jogador.nome)
        elif self.jogador.pontos < self.segundoJogador.pontos:
            resultadoString = '{nome} é o Vencedor!'.format(nome=self.segundoJogador.nome)
        print(resultadoString)

jogo = Jogo()
jogo.iniciar()