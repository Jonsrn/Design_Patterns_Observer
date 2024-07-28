

class Observado:
    def __init__(self):
        self._observadores = []
        self._estado = 0

    def adicionar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._estado)

    def alterar_estado(self, novo_estado):
        self._estado = novo_estado
        self.notificar_observadores()

class Observador:
    def atualizar(self, estado):
        raise NotImplementedError("Subclasses devem implementar o método 'atualizar'")

class LabelObservador(Observador):
    def __init__(self, label):
        self.label = label

    def atualizar(self, estado):
        self.label.setText(f"Estado: {estado}")
