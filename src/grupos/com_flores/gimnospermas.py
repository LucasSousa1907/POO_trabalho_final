from src.base.planta_superclasse import PlantaAmazonia

class GimnospermaAmazonia(PlantaAmazonia):
    def __init__(self, nome, especie, porte):
        super().__init__(nome, especie, 'Gimnospermas', porte)
        self.flores = True
        self.frutos = False

    def produzir_cone(self):
        print('A planta produziu estróbilos')

pinheiro1 = GimnospermaAmazonia('pinheiro da amazonia', 'Retrophyllum piresii   ', 'grande')