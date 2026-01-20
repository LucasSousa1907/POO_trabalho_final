class PlantaAmazonia:
    def __init__(self, nome, especie, grupo, porte):
        self.nome = nome
        self.reino = 'Plantae'
        self.especie = especie
        self.grupo = grupo
        self.saude = True
        self.porte = porte

    def crescer (self, cm):
        self.altura += cm
        print(f'{self.nome} aumentou {cm}cm!')

    def status(self):
        print(f'{self.nome} | Altura: {self.altura}cm | Saudável: {self.saude}')

    def identificar(self):
        print(f'Esta planta é um {self.nome}, da especie {self.especie}, pertencente ao grupo das {self.grupo}\n')
