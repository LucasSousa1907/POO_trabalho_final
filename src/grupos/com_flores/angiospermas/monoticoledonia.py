from .angiospermas_base import AngiospermaAmazonia

class Monocotiledonia(AngiospermaAmazonia):
    def __init__(self, nome, especie, porte):
        super().__init__(nome, especie, porte)
        self.folhas = 'Folhas finas e compridas'
        self.tipo = 'monocotiledoneas'
    def identificar(self):
        print(f'Esta planta é um {self.nome}, da especie {self.especie}, pertencente ao grupo das {self.grupo} monocotiledonias\n ')