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
print(square.get_height())
square.__height = 3 # raises AttributeError
print(square.set_height(6))
print(square.get_height())