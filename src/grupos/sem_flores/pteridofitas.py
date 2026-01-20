from src.base.planta_superclasse import PlantaAmazonia

class PteridofitaAmazonia(PlantaAmazonia):
    def __init__(self, nome, especie, porte):
        super().__init__(nome, especie, 'Pteridofitas', porte)
        self.flores = False
        self.caule = True
        self.umidade_ideal = 60

    def verificar_umidade(self, nivel):
        if nivel >= self.umidade_ideal:
            self.saude = True
        else:
            self.saude = False

samambaia1 = PteridofitaAmazonia('samambaia do jardim', 'samambaia', 'pequena')

# samambaia 1.identificar()
# print(musgo1.nome)
