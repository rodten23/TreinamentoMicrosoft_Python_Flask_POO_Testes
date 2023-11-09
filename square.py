# SEM modificadores de acesso
class Square_A:
    def __init__(self):
         self.height = 2   # Sem _ os dados estão livres para o mundo externo da classe.
         self.width = 2
    def set_side(self, new_side):
         self.height = new_side
         self.width = new_side

square = Square_A()
square.height = 3 # not a square anymore

# COM modificadores de acesso
class Square_B:
    def __init__(self):
          self._height = 2   # Com 1 _ à esquerda, indicamos que são dados que não devem ser alterados pelo mundo exterior (dados protegidos).
          self._width = 2
    def set_side(self, new_side):
          self._height = new_side
          self._width = new_side

square = Square_B()
square._height = 3 # not a square anymore


class Square_C:
    def __init__(self):
          self.__height = 2   # Com 2 _ à esquerda, indicamos que são dados são privados.
          self.__width = 2
    def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side

square = Square_C()
square.__height = 3 # raises AttributeError

# Mesmo assim, isso não é uma segurança "perfeita". Usando o código abaixo, ainda conseguimos acessar os dados, pois com _ ou __ apenas alteramos os nomes dos dados.
square = Square_C()
square._Square__height = 3 # is allowed

# Segundo a Microsoft "Muitas outras linguagens que implementam a proteção de dados resolvem esse problema de maneira diferente. O Python é exclusivo, pois a proteção de dados é mais semelhante a níveis de sugestão em vez de ser estritamente implementada."


# COM Getters (acessadores) e Setters (modificadores)
class Square_D:
    def __init__(self):
        self.__height = 2
        self.__width = 2
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side
    def get_height(self):   # Os métodos Getters tornam os dados do objetos acessíveis ao mundo exterior.
        return self.__height
    def set_height(self, h):   # Já os métodos Setters permitem alterar os dados do objetos diretamente.
        if h >= 0:
            self.__height = h
        else:
            raise Exception("value needs to be 0 or larger")

square = Square_D()
square.__height = 3 # raises AttributeError

# COM Decorador

'''Usar decoradores para getters e setters
Os decoradores são uma entidade importante em Python. Eles fazem parte de uma entidade maior chamada metaprogramação. Os decoradores são funções que usam sua função como uma entrada. A ideia é codificar a funcionalidade reutilizável como funções decoradoras e, em seguida, decorar outras funções com ela. A finalidade é dar à sua função um recurso que ela não tinha antes. Um decorador pode, por exemplo, adicionar campos ao seu objeto, medir o tempo necessário para invocar uma função e fazer muito mais.

No contexto da OOP e getters e setters, um decorador específico @property pode ajudar você a remover um código clichê quando adiciona getters e setters. O decorador @property faz o seguinte para você:

Cria um campo de suporte: quando você decora uma função com o decorador @property, ele cria um campo de suporte específico. Você poderá substituir esse comportamento se desejar, mas é bom ter um comportamento padrão.
Identifica um setter: um método setter pode alterar o campo de suporte.
Identifica um getter: essa função deve retornar o campo de suporte.
Identifica uma função de exclusão: essa função pode excluir o campo.
Vamos ver esse decorador em ação:'''

class Square:
    def __init__(self, w, h):
        self.__height = h
        self.__width = w
  
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")
        
'''No código anterior, a função height() é decorada pelo decorador @property. Essa ação de decoração cria o campo privado __height. O campo __height não está definido no construtor __init__() porque o decorador já faz isso. Há também outra decoração acontecendo, ou seja, @height.setter. Essa decoração aponta para um método height() semelhante ao setter. O novo método height recebe outro parâmetro value como o segundo parâmetro.

A capacidade de manipular a altura separada da largura ainda causará um problema. Você precisará entender o que a classe faz antes de você considerar a possibilidade de permitir getters e setters, pois você está introduzindo o risco.'''