"""
El programa mostrará una ventana donde el usuario podrá:
-Seleccionar un tipo de mascota (por ejemplo, perro, gato, pájaro, etc.)
-Ingresar la edad de la mascota usando un SpinBox.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QMessageBox

class VentanaDatosMascota(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Datos de la Mascota")
        self.setGeometry(100, 100, 300, 200)
        
        # Crear los widgets
        self.label_tipo = QLabel("Seleccione el tipo de mascota:", self)
        self.combo_tipo = QComboBox(self)
        self.combo_tipo.addItems(["Perro", "Gato", "Pájaro", "Pez", "Hamster"])

        self.label_edad = QLabel("Ingrese la edad de la mascota:", self)
        self.spin_edad = QSpinBox(self)
        self.spin_edad.setRange(0, 20)  # Edad entre 0 y 20 años

        self.boton_leer = QPushButton("Leer Datos", self)
        self.boton_leer.clicked.connect(self.leer_datos)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_tipo)
        layout.addWidget(self.combo_tipo)
        layout.addWidget(self.label_edad)
        layout.addWidget(self.spin_edad)
        layout.addWidget(self.boton_leer)

        self.setLayout(layout)

    # Función para leer los datos ingresados
    def leer_datos(self):
        tipo_mascota = self.combo_tipo.currentText()
        edad_mascota = self.spin_edad.value()
        
        # Mostrar los datos en un cuadro de mensaje
        QMessageBox.information(self, "Datos de la Mascota", f"Tipo de Mascota: {tipo_mascota}\nEdad: {edad_mascota} años")

# Función principal para iniciar la aplicación
def iniciar_app():
    app = QApplication(sys.argv)
    ventana = VentanaDatosMascota()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    iniciar_app()
