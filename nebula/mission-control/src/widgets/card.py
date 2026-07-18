from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class Card(QFrame):
    def __init__(self, title, description):
        super().__init__()

        self.title = title

        self.setObjectName("card")
        self.setCursor(QCursor(Qt.PointingHandCursor))

        layout = QVBoxLayout()

        titleLabel = QLabel(title)
        titleLabel.setObjectName("cardTitle")

        descLabel = QLabel(description)
        descLabel.setObjectName("cardDesc")

        layout.addWidget(titleLabel)
        layout.addWidget(descLabel)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        print(f"{self.title} clicked!")
        super().mousePressEvent(event)
