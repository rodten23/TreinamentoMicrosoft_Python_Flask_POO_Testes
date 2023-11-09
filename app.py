# Baseado no treinamento "Criar aplicativos do mundo real com o Python" do Microsoft Learn (https://learn.microsoft.com/pt-br/training/paths/python-language/)

class Carro:   # A classe é o "modelo" para construção do objeto, com suas principais características.
    def __init__(self):   # __init__() é o método construtor da classe.
        # O parâmetro self refere-se à instância do objeto. Qualquer atribuição a essa palavra-chave significa que o atributo termina na instância do objeto. Se você não adicionar um atributo a self, ele será tratado como uma variável temporária que não existirá depois que a execução de __init__() for concluída.
        self.cor = 'Azul Marinho'   # self.Atributo (variável "cor") acaba (faz parte) no objeto e pode ser "invocada".
        marca = 'Nissan'   #sem o self, variável só existe para "trabalhar dentro da classe", mas não pode ser invocada no objeto instanciado. Se invocado, resultaria em um erro, 'marca' não existe no objeto.


carro = Carro()   # Para instanciar (criar o objeto em si) a partir da classe (que é o modelo), basta chamar seu nome com (). E, neste exemplo, este objeto foi atribuido a uma variável.

print(carro.cor)   # Atributo "cor" está presente no objeto instanciado e pode ser invocado.
#print(carro.marca)   # Variável "marca" está presente apenas na classe e causará erro ser for invocada (AttributeError: 'Carro' object has no attribute 'marca')

class Livro:
    def __init__(self, avaliacao):
        self.titulo = 'O Tao da Física'
        self.autor = 'Fritjof Capra'
        self.editora = 'Cultrix'
        self.avaliacao = avaliacao

livro = Livro('excelente')
print('Título: ' + livro.titulo, '\nAutor: ' + livro.autor, '\nEditora: ' + livro.editora, '\nAvaliação: ' + livro.avaliacao)
