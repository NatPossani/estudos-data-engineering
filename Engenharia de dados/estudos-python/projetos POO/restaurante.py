class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #inicia o contrutor. o __init__ eh o nome reservado para o construtor. self eh o primeiro parametro, ele se refere a propria instancia do objeto que esta sendo criada. eh atraves do self que voce acessa os atributos e metodos esp[ecificos daquele ojeto]
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    #ao inves de ser self. pode ser this. ou qualquer outro nome criado, mas por convenção se usa self
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
                print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('praca', 'gourmet') # instancia/cria restaurante
#restaurante_praca.nome = 'Praca'
#restaurante_praca.categoria = 'gourmet'
restaurante_pizza = Restaurante('pizza', 'italiana')

# restaurantes = [restaurante_praca, restaurante_pizza] # lista de restaurantes

#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))

# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.listar_restaurantes()