class Pessoa:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __repr__(self):
        return f"Pessoa(message={self.nome}, number={self.numero})"
