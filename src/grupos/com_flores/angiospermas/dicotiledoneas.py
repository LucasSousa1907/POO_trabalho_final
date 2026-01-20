from .angiospermas_base import AngiospermaAmazonia

class Dicotiledonea(AngiospermaAmazonia):
    def __init__(self, nome, especie, porte):
        super().__init__(nome, especie, porte)
        self.folhas = 'Folhas largas e espalhadas'
        self.tipo = 'dicotiledonias'
    def identificar(self):
        print(f'Esta planta é um {self.nome}, da especie {self.especie}, pertencente ao grupo das {self.grupo} dicotiledoneas\n ')