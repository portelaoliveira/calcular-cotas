from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from ..components.Button.Button import Button
from ..components.DropDown.dropdown import DropDown
from ..components.Input.input_file import InputFile
from ..components.Input.input_number import InputNumber
from ..components.Popup.popup import Popup
from ..controller.functions import gen_intermediate_cotas


class IntermediateQuotasViewer(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.setStyleSheet("background-color: #fff")

        self.create_layout()

    def create_layout(self):
        self.layout = QVBoxLayout()

        # create components
        self.in_file = InputFile(
            text_label="Selecionar arquivo .txt de entrada:",
            text_button="Abrir",
            is_folder=False,
            file_types=["txt"],
            parent=self,
        )

        self.out_file = InputFile(
            text_label="Selecionar pasta de saída:",
            text_button="Salvar",
            is_folder=True,
            is_save=True,
            parent=self,
        )

        self.interval = InputNumber(
            text_label="Espaçamento das cotas a serem calculadas:",
            number_type=int,
            default_value=20,
            max=1000,
            parent=self,
        )

        self.projection = DropDown(
            text_label="Projeção:",
            items=["Horizontal", "Topografia"],
            parent=self,
        )

        self.calculate_button = Button(
            "Calcular cotas intermediárias",
            callback=self.process_data,
            parent=self,
        )

        self.success_popup = Popup(
            title="Cálculo finalizado!",
            text="Imagem e tabela gerada com sucesso!",
            parent=self,
        )

        title = QLabel("Cotas intermediárias", parent=self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
                QLabel {
                color: #566164;
                font-size: 20px;
                font-weight: 700;
                }
            """)

        vertical_spacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horiontal_layout = QHBoxLayout()
        self.horiontal_layout.addWidget(self.interval, 1)
        self.horiontal_layout.addWidget(self.projection, 1)

        self.layout.addSpacerItem(vertical_spacer)
        self.layout.addWidget(title, alignment=Qt.AlignCenter)
        self.layout.addSpacerItem(vertical_spacer)
        self.layout.addWidget(self.in_file)
        self.layout.addWidget(self.out_file)
        self.layout.addLayout(self.horiontal_layout)
        self.layout.addSpacing(24)
        self.layout.addSpacerItem(vertical_spacer)
        self.layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)
        self.layout.addSpacerItem(vertical_spacer)

        self.setLayout(self.layout)

    def set_enabled_inputs(self, enabled):
        self.calculate_button.setEnabled(enabled)
        self.in_file.action_button.setEnabled(enabled)
        self.out_file.action_button.setEnabled(enabled)
        self.interval.number_input.setEnabled(enabled)

        if enabled:
            self.calculate_button.update_text("Calcular cotas intermediárias")
        else:
            self.calculate_button.update_text("Calculando...")

    def handle_errors(self):
        error = False
        if not self.in_file.file_path:
            self.in_file.set_error()
            error = True
        else:
            self.in_file.remove_error()

        if not self.out_file.file_path:
            self.out_file.set_error()
            error = True
        else:
            self.out_file.remove_error()

        if self.interval.get_value() is None:
            self.interval.set_error()
            error = True
        else:
            self.interval.remove_error()

        return not error

    def process_data(self):
        if self.handle_errors():
            self.set_enabled_inputs(False)

            gen_intermediate_cotas(
                file_name_txt=self.in_file.file_path,
                path_folder=self.out_file.file_path,
                spacing_cotas_in=self.interval.get_value(),
                option_in=self.projection.get_value(),
                on_success=self.on_success,
                on_error=self.on_error,
            )

    def on_success(self):
        self.set_enabled_inputs(True)
        self.success_popup.exec()

    def on_error(self, error: str):
        self.set_enabled_inputs(True)

        error_popup = Popup(
            title=(
                "Erro ao gerar a imagem e a tabela com as cotas"
                " intermediárias!"
            ),
            text=f"{error}",
            error=True,
            parent=self,
        )
        error_popup.exec()
