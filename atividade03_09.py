import unittest

class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_consecutivos = 0
        self.direcao_anterior = None

    def mover(self, comandos):
        for comando in comandos:
            self.validar_comando(comando)
            self.executar_comando(comando)
            if abs(self.posicao) >= 50:
                break
        return self.posicao

    def validar_comando(self, comando):
        if comando not in ["ESQUERDA", "DIREITA"]:
            raise ValueError(f"Comando inválido: {comando}")

    def executar_comando(self, comando):
        if comando == "ESQUERDA":
            self.mover_para_esquerda()
        elif comando == "DIREITA":
            self.mover_para_direita()

    def mover_para_esquerda(self):
        if self.direcao_anterior == "ESQUERDA":
            self.movimentos_consecutivos += 1
        else:
            self.movimentos_consecutivos = 1
            self.direcao_anterior = "ESQUERDA"
        if self.movimentos_consecutivos > 20:
            raise ValueError("Excedido o limite de 20 movimentos consecutivos na mesma direção")
        self.posicao -= 1

    def mover_para_direita(self):
        if self.direcao_anterior == "DIREITA":
            self.movimentos_consecutivos += 1
        else:
            self.movimentos_consecutivos = 1
            self.direcao_anterior = "DIREITA"
        if self.movimentos_consecutivos > 20:
            raise ValueError("Excedido o limite de 20 movimentos consecutivos na mesma direção")
        self.posicao += 1

class TestTremAutonomo(unittest.TestCase):
    def setUp(self):
        self.trem = TremAutonomo()

    def test_comandos_simples(self):
        self.assertEqual(self.trem.mover(["DIREITA", "DIREITA"]), 2)
        self.assertEqual(self.trem.mover(["ESQUERDA"]), 1)
        self.assertEqual(self.trem.mover(["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]), 3)

    def test_comando_invalido(self):
        with self.assertRaises(ValueError):
            self.trem.mover(["ESQUERDA", "CIMA"])

    def test_lista_de_comandos_vazia(self):
        self.assertEqual(self.trem.mover([]), 0)

    def test_excesso_de_movimentos(self):
        comandos = ["DIREITA"] * 51
        with self.assertRaises(ValueError):
            self.trem.mover(comandos)

    def test_movimentos_consecutivos_mesma_direcao(self):
        comandos = ["DIREITA"] * 21
        with self.assertRaises(ValueError):
            self.trem.mover(comandos)

def rodar_programa():
    trem = TremAutonomo()
    
    comandos = input("Digite os comandos (separados por vírgula) [ESQUERDA, DIREITA]: ").strip().split(",")
    comandos = [comando.strip().upper() for comando in comandos]
    
    try:
        posicao_final = trem.mover(comandos)
        print(f"A posição final do trem é: {posicao_final}")
    except ValueError as e:
        print(f"Erro: {e}")

def rodar_testes():
    unittest.main(argv=[''], verbosity=2, exit=False)

def menu():
    while True:
        print("1. Rodar o programa do trem autônomo")
        print("2. Rodar os testes automáticos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            rodar_programa()
        elif escolha == '2':
            rodar_testes()
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
