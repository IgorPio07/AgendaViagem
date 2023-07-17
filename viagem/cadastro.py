lista_destinos = ['Portugal', 'Inglaterra', 'Chile', 'EUA', 'Egito']


class Usuario:

    def __init__(self, destino):
        self.__destino = destino

    def display(self):
        print('=========')
        print(f'Viagem marcada para {lista_destinos[self.__destino]}')

    @staticmethod
    def marcar_viagem():
        print('[0] -> Portugal')
        print('[1] -> Inglaterra')
        print('[2] -> Chile')
        print('[3] -> EUA')
        print('[4] -> Egito')
        return dict(destino=int(input('Selecione a opção do destino')))



