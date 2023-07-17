from viagem.cadastro import Usuario


class Agenda:

    def __init__(self, nome):
        self.__nome = nome
        self.__agenda = []

    def display_agenda(self):
        print(f'Agenda do usuário: {self.__nome}')
        for viagem in self.__agenda:
            viagem.display()

    def adicionar_viagem(self):
        init_args = Usuario.marcar_viagem()
        self.__agenda.append(Usuario(**init_args))
