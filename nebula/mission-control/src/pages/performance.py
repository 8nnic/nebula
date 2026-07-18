from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class PerformancePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Desktop")
        description = QLabel("Panels, layouts and workspace settings.")

        layout.addWidget(title)
        layout.addWidget(description)

        self.setLayout(layout)
