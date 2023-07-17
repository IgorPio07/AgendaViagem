from viagem.agenda import Agenda
from viagem.cadastro import Usuario

usuario = input('Informe seu nome para começarmos: ')


def main():
    usuario_1 = Agenda(usuario)
    usuario_1.adicionar_viagem()
    usuario_1.adicionar_viagem()
    usuario_1.display_agenda()


if __name__ == '__main__':
    main()