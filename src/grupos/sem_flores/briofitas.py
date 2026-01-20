from src.base.planta_superclasse import PlantaAmazonia

class BriofitaAmazonia(PlantaAmazonia):
    def __init__(self, nome, especie):
        super().__init__(nome, especie, 'Briofitas', 'pequeno')
        self.flores = False
        self.caule = False
        self.umidade_ideal = 80

    def verificar_umidade(self, nivel):
        if nivel >= self.umidade_ideal:
            self.saude = True
        else:
            self.saude = False

#instancia criada a partir da subclasse anterior
musgo1 = BriofitaAmazonia('musgo do jardim', 'Musgo')