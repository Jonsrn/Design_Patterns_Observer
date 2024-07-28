
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from observador import Observado, LabelObservador

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        
        self.observado = Observado()

        main_layout = QVBoxLayout()

        font = QFont("Arial", 16)
        label_font = QFont("Arial", 20)

        self.label1 = QLabel("Estado: 0", self)
        self.label1.setFont(label_font)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel("Estado: 0", self)
        self.label2.setFont(label_font)
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("Estado: 0", self)
        self.label3.setFont(label_font)
        self.label3.setAlignment(Qt.AlignCenter)

        self.label_observador1 = LabelObservador(self.label1)
        self.label_observador2 = LabelObservador(self.label2)
        self.label_observador3 = LabelObservador(self.label3)

        box1_layout = QVBoxLayout()
        box1_layout.addWidget(self.label1)
        self.button_vincular1 = QPushButton("Vincular", self)
        self.button_vincular1.setFont(font)
        self.button_vincular1.clicked.connect(lambda: self.vincular_observador(self.label_observador1))
        self.button_desvincular1 = QPushButton("Desvincular", self)
        self.button_desvincular1.setFont(font)
        self.button_desvincular1.clicked.connect(lambda: self.desvincular_observador(self.label_observador1))
        box1_layout.addWidget(self.button_vincular1)
        box1_layout.addWidget(self.button_desvincular1)

        box2_layout = QVBoxLayout()
        box2_layout.addWidget(self.label2)
        self.button_vincular2 = QPushButton("Vincular", self)
        self.button_vincular2.setFont(font)
        self.button_vincular2.clicked.connect(lambda: self.vincular_observador(self.label_observador2))
        self.button_desvincular2 = QPushButton("Desvincular", self)
        self.button_desvincular2.setFont(font)
        self.button_desvincular2.clicked.connect(lambda: self.desvincular_observador(self.label_observador2))
        box2_layout.addWidget(self.button_vincular2)
        box2_layout.addWidget(self.button_desvincular2)

        box3_layout = QVBoxLayout()
        box3_layout.addWidget(self.label3)
        self.button_vincular3 = QPushButton("Vincular", self)
        self.button_vincular3.setFont(font)
        self.button_vincular3.clicked.connect(lambda: self.vincular_observador(self.label_observador3))
        self.button_desvincular3 = QPushButton("Desvincular", self)
        self.button_desvincular3.setFont(font)
        self.button_desvincular3.clicked.connect(lambda: self.desvincular_observador(self.label_observador3))
        box3_layout.addWidget(self.button_vincular3)
        box3_layout.addWidget(self.button_desvincular3)

        boxes_layout = QHBoxLayout()
        boxes_layout.addLayout(box1_layout)
        boxes_layout.addLayout(box2_layout)
        boxes_layout.addLayout(box3_layout)

        main_layout.addLayout(boxes_layout)

        self.button_increment = QPushButton("Incrementar", self)
        self.button_increment.setFont(font)
        self.button_increment.clicked.connect(self.incrementar_estado)
        main_layout.addWidget(self.button_increment)

        self.button_decrement = QPushButton("Decrementar", self)
        self.button_decrement.setFont(font)
        self.button_decrement.clicked.connect(self.decrementar_estado)
        main_layout.addWidget(self.button_decrement)

        self.setLayout(main_layout)
        self.setWindowTitle('Observer Pattern Example')
        self.show()

    def incrementar_estado(self):
        novo_estado = self.observado._estado + 1
        self.observado.alterar_estado(novo_estado)

    def decrementar_estado(self):
        novo_estado = self.observado._estado - 1
        self.observado.alterar_estado(novo_estado)

    def vincular_observador(self, observador):
        self.observado.adicionar_observador(observador)

    def desvincular_observador(self, observador):
        self.observado.remover_observador(observador)
