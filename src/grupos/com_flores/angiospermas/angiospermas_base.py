from src.base.planta_superclasse import PlantaAmazonia

class AngiospermaAmazonia(PlantaAmazonia):
    def __init__(self, nome, especie, porte):
        super().__init__(nome, especie, 'Angiospermas', porte)
        self.flores = True
        self.frutos = True

    def produzir_fruto(self):
        print('A planta produziu frutos')
