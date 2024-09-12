class Restaurante:
    restaurantes = []
    def __init__(this,nome, categoria):
        this. nome = nome.title(),
        this.categoria = categoria.upper(),
        this._ativo = False
        Restaurante.restaurantes.append(this)
    
    @classmethod
    def listar_resturantes(cls):
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alterar_estado(self):
        self._ativo = not self._ativo
        
novo_restaurante= Restaurante('bao','Lanche')
novo_restaurante.alterar_estado()
Restaurante.listar_resturantes()


# print(vars(novo_restaurante))