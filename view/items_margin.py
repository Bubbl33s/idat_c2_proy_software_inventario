from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class TableItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Pintar el fondo
        painter.fillRect(option.rect, option.backgroundBrush)

        # Configurar la fuente del ítem
        painter.setFont(option.font)

        # Margen izquierdo
        offset = 10

        # Pintar el texto con margen
        text = index.data()
        alignment = option.displayAlignment
        rect = option.rect

        if alignment & Qt.AlignRight:
            # Si la alineación es a la derecha, no ajuste el margen izquierdo
            painter.drawText(rect, alignment, text)
        else:
            # Ajuste el rectángulo para el margen izquierdo si no está alineado a la derecha
            adjusted_rect = rect.adjusted(offset, 0, 0, 0)
            painter.drawText(adjusted_rect, alignment, text)
