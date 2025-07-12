import sys
import os
import piexif
from PIL import Image, ExifTags
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView, QLineEdit, QDialog, QDialogButtonBox
)
from PyQt5.QtGui import QPixmap, QClipboard
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import webbrowser
import json
import pillow_heif
pillow_heif.register_heif_opener()
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QLibraryInfo

class MetadataViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyMetadater")
        icon_path = os.path.join(os.path.abspath("."), "cyberius.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        self.setGeometry(200, 100, 1000, 720)
        self.setStyleSheet("background-color: #2d3037; color: #939194;")
        self.setAcceptDrops(True)  # Habilita arrastrar y soltar

        self.tray_icon = QSystemTrayIcon(QIcon("cyberius.ico"), self)
        self.tray_icon.setToolTip("CyMetadater")

        tray_menu = QMenu()

        restore_action = QAction("Mostrar ventana", self)
        restore_action.triggered.connect(self.show_normal_from_tray)
        tray_menu.addAction(restore_action)

        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.image_path = None
        self.image_list = []
        self.current_index = -1
        self.exif_data = {}
        self.exif_raw = {}

        self.init_ui()
    
    def minimize_to_tray(self):
        self.hide()
        self.tray_icon.show()
        self.tray_icon.showMessage("CyMetadater", "La aplicación sigue activa en segundo plano.", QSystemTrayIcon.Information, 3000)

    def show_normal_from_tray(self):
        self.show()
        self.tray_icon.hide()

    def init_ui(self):
        import datetime
        layout = QVBoxLayout()

        self.header_label = QLabel("Ninguna imagen seleccionada")
        self.header_label.setStyleSheet("background-color: #4f5354; color: #83f1e8; font-size: 16px; padding: 8px;")
        self.header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.header_label)

        self.image_label = QLabel("Arrastra una/as imagen aquí")
        self.image_label.setFixedHeight(400)
        self.image_label.setStyleSheet("border: 2px solid #939194; margin-bottom: 10px;")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        btn_layout = QHBoxLayout()

        self.load_btn = QPushButton("Cargar Imagen Manualmente")
        self.load_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.load_btn.clicked.connect(self.load_image)
        btn_layout.addWidget(self.load_btn)

        self.reload_btn = QPushButton("Quitar datos del Viewer")
        self.reload_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.reload_btn.clicked.connect(self.reset_view)
        btn_layout.addWidget(self.reload_btn)

        self.clean_btn = QPushButton("Limpiar EXIF")
        self.clean_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.clean_btn.clicked.connect(self.clean_exif)
        btn_layout.addWidget(self.clean_btn)

        self.gps_btn = QPushButton("Sin datos GPS")
        self.gps_btn.setEnabled(False)
        self.gps_btn.setStyleSheet("background-color: #4f5354; color: #666666; padding: 8px;")
        self.gps_btn.clicked.connect(self.show_gps_location)
        btn_layout.addWidget(self.gps_btn)

        layout.addLayout(btn_layout)

        self.export_btn = QPushButton("Exportar metadatos")
        self.export_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.export_btn.clicked.connect(self.export_metadata)
        layout.addWidget(self.export_btn)

        self.minimize_btn = QPushButton("Minimizar a segundo plano")
        self.minimize_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.minimize_btn.clicked.connect(self.minimize_to_tray)
        layout.addWidget(self.minimize_btn)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Buscar metadato...")
        self.search_box.textChanged.connect(self.filter_metadata)
        self.search_box.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 6px;")
        layout.addWidget(self.search_box)

        nav_layout = QHBoxLayout()
        self.prev_btn = QPushButton("← Anterior")
        self.prev_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.prev_btn.clicked.connect(self.load_prev_image)

        self.next_btn = QPushButton("Siguiente →")
        self.next_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        self.next_btn.clicked.connect(self.load_next_image)

        self.image_counter = QLabel("")
        self.image_counter.setAlignment(Qt.AlignCenter)
        self.image_counter.setStyleSheet("color: #83f1e8; font-size: 12px; padding: 4px;")

        nav_layout.addWidget(self.prev_btn)
        nav_layout.addWidget(self.image_counter)
        nav_layout.addWidget(self.next_btn)
        layout.addLayout(nav_layout)


        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Campo", "Valor"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setStyleSheet("color: #83f1e8;")
        self.table.setStyleSheet("background-color: #4f5354; color: #83f1e8;")
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.AllEditTriggers)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        paths = [
            u.toLocalFile() for u in urls
            if u.toLocalFile().lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.webp', '.gif', '.heic'))
        ]
        if paths:
            self.image_list = paths
            self.current_index = 0
            self.load_image_from_path(self.image_list[self.current_index])
        else:
            QMessageBox.warning(self, "Formato no válido", "Solo se permiten imágenes con formato compatible.")


    def reset_view(self):
        self.image_label.clear()
        self.image_label.setText("Imagen cargada aquí")
        self.header_label.setText("Ninguna imagen seleccionada")
        self.search_box.clear()
        self.table.setRowCount(0)
        self.image_path = None
        self.exif_data = {}
        self.exif_raw = {}
        self.gps_btn.setVisible(False)
        self.image_list = []
        self.current_index = -1
        self.image_counter.setText("")

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters([
            "Imágenes (*.jpg *.jpeg *.png *.tiff *.bmp *.webp *.gif *.heic)",
            "Todos los archivos (*)"
        ])
        if file_dialog.exec_():
            file_name = file_dialog.selectedFiles()[0]
            self.load_image_from_path(file_name)

    def load_image_from_path(self, file_name):
        try:
            img = Image.open(file_name)
            img.verify()
            self.image_path = file_name
            self.header_label.setText(os.path.basename(file_name))
            self.load_metadata()
            self.display_image()
            if self.image_list:
                self.image_counter.setText(f"{self.current_index + 1} / {len(self.image_list)}")
            else:
                self.image_counter.setText("")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la imagen:\n{e}")

    def load_metadata(self):
        self.exif_data = {}
        self.exif_raw = {}
        self.table.setRowCount(0)
        if not self.image_path:
            return
        try:
            img = Image.open(self.image_path)
            exif_bytes = img.info.get("exif", None)
            if not exif_bytes:
                QMessageBox.information(self, "Sin metadatos", "Esta imagen no contiene metadatos EXIF.")
                return
            exif_dict = piexif.load(exif_bytes)
            self.exif_raw = exif_dict
            for ifd_name in exif_dict:
                if ifd_name == "thumbnail":
                    continue
                for tag in exif_dict[ifd_name]:
                    tag_name = piexif.TAGS[ifd_name].get(tag, {}).get("name", tag)
                    value = exif_dict[ifd_name][tag]
                    if isinstance(value, bytes):
                        try:
                            shown_value = value.decode("utf-8").strip()
                        except:
                            shown_value = f"[Datos binarios: {len(value)} bytes]"
                    elif isinstance(value, tuple):
                        def convert_rational(val):
                            try:
                                return float(val[0]) / float(val[1]) if val[1] != 0 else 0
                            except:
                                return str(val)
                        if all(isinstance(v, tuple) and len(v) == 2 for v in value):
                            try:
                                shown_value = ", ".join(f"{convert_rational(v):.6f}" for v in value)
                            except:
                                shown_value = str(value)
                        else:
                            shown_value = str(value)
                    else:
                        shown_value = str(value)
                    self.exif_data[tag_name] = shown_value
            self.display_metadata()
            self.check_gps_button()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo extraer metadatos:\n{e}")

    def display_metadata(self):
        self.table.setRowCount(0)
        for row, (key, value) in enumerate(self.exif_data.items()):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(key)))
            self.table.setItem(row, 1, QTableWidgetItem(str(value)))

    def display_image(self):
        if not self.image_path:
            return
        try:
            img = Image.open(self.image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            temp_path = os.path.join(os.path.dirname(__file__), '_temp_preview.jpg')
            img.save(temp_path, format='JPEG')
            pixmap = QPixmap(temp_path)
            scaled = pixmap.scaledToHeight(380, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled)
            os.remove(temp_path)
        except Exception as e:
            self.image_label.setText("No se pudo mostrar la imagen")
            print(f"Error mostrando imagen: {e}")

    def filter_metadata(self):
        search = self.search_box.text().lower()
        for row in range(self.table.rowCount()):
            item_key = self.table.item(row, 0).text().lower()
            item_value = self.table.item(row, 1).text().lower()
            is_visible = search in item_key or search in item_value
            self.table.setRowHidden(row, not is_visible)

    def clean_exif(self):
        if not self.image_path:
            return
        try:
            img = Image.open(self.image_path)
            new_path, _ = QFileDialog.getSaveFileName(self, "Guardar como", "", "Imagen JPEG (*.jpg);;Todos los archivos (*)")
            if new_path:
                img.save(new_path, exif=piexif.dump({"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}))
                QMessageBox.information(self, "Limpieza", "Metadatos EXIF eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al limpiar los metadatos:\n{e}")

    def export_metadata(self):
        if not self.exif_data:
            QMessageBox.information(self, "Exportación", "No hay metadatos para exportar.")
            return

        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar metadatos como", "metadata.json", "JSON (*.json);;Texto (*.txt)", options=options)
        if filename:
            try:
                if filename.endswith('.txt'):
                    with open(filename, 'w', encoding='utf-8') as f:
                        for key, value in self.exif_data.items():
                            f.write(f"{key}: {value}")
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.exif_data, f, indent=4, ensure_ascii=False)
                QMessageBox.information(self, "Éxito", f"Metadatos exportados a{filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo exportar:{e}")

    def check_gps_button(self):
        gps_info = self.exif_raw.get("GPS", {})
        if gps_info:
            self.gps_btn.setText("Ver ubicación GPS")
            self.gps_btn.setEnabled(True)
            self.gps_btn.setStyleSheet("background-color: #4f5354; color: #83f1e8; padding: 8px;")
        else:
            self.gps_btn.setText("Sin datos GPS")
            self.gps_btn.setEnabled(False)
            self.gps_btn.setStyleSheet("background-color: #4f5354; color: #666666; padding: 8px;")

    def show_gps_location(self):
        gps_info = self.exif_raw.get("GPS", {})
        if not gps_info:
            return

        def dms_to_deg(value):
            return value[0][0] / value[0][1] + value[1][0] / value[1][1] / 60 + value[2][0] / value[2][1] / 3600

        try:
            lat = dms_to_deg(gps_info[2])
            if gps_info[1] == b'S':
                lat = -lat
            lon = dms_to_deg(gps_info[4])
            if gps_info[3] == b'W':
                lon = -lon

            url = f"https://www.google.com/maps?q={lat},{lon}&z=15"
            lat_ref = "N" if lat >= 0 else "S"
            lon_ref = "E" if lon >= 0 else "W"
            geohack_url = f"https://geohack.toolforge.org/geohack.php?params={abs(lat)}_{lat_ref}_{abs(lon)}_{lon_ref}"

            dialog = QDialog(self)
            dialog.setWindowTitle("Ubicación GPS")
            dialog.setGeometry(300, 200, 700, 500)
            dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

            layout = QVBoxLayout()

            webview = QWebEngineView()
            webview.load(QUrl(url))
            layout.addWidget(webview)

            buttons = QDialogButtonBox()

            copy_btn = QPushButton("Copiar Coordenadas")
            geohack_btn = QPushButton("Abrir en GeoHack")
            help_btn = QPushButton("¿Qué es esto?")
            close_btn = QPushButton("Cerrar")

            copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(f"{lat}, {lon}"))
            geohack_btn.clicked.connect(lambda: webbrowser.open(geohack_url))
            help_btn.clicked.connect(lambda: QMessageBox.information(
                self,
                "Ayuda sobre GPS",
                "Esta ubicación ha sido calculada a partir de los metadatos GPS incluidos en el fichero que has adjuntado.\n\n"
                "Puedes visualizar la ubicación en Google Maps (integrado) o abrirla en GeoHack para análisis forense detallado.\n\n"
                "GeoHack es una herramienta de la Fundación Wikimedia que muestra múltiples servicios de mapas a partir de coordenadas geográficas."
            ))
            close_btn.clicked.connect(dialog.close)

            buttons.addButton(copy_btn, QDialogButtonBox.ActionRole)
            buttons.addButton(geohack_btn, QDialogButtonBox.ActionRole)
            buttons.addButton(help_btn, QDialogButtonBox.HelpRole)
            buttons.addButton(close_btn, QDialogButtonBox.RejectRole)

            layout.addWidget(buttons)
            dialog.setLayout(layout)
            dialog.exec_()

        except Exception as e:
            QMessageBox.warning(self, "GPS", f"Error al obtener coordenadas:\n{e}")


        def dms_to_deg(value):
            return value[0][0]/value[0][1] + value[1][0]/value[1][1]/60 + value[2][0]/value[2][1]/3600

        try:
            lat = dms_to_deg(gps_info[2])
            if gps_info[1] == b'S': lat = -lat
            lon = dms_to_deg(gps_info[4])
            if gps_info[3] == b'W': lon = -lon

            url = f"https://www.google.com/maps?q={lat},{lon}&z=15"
            dialog = QDialog(self)
            dialog.setWindowTitle("Viendo la Ubicación GPS del fichero")
            dialog.setGeometry(300, 200, 700, 500)

            layout = QVBoxLayout()
            webview = QWebEngineView()
            webview.load(QUrl(url))
            layout.addWidget(webview)

            buttons = QDialogButtonBox()
            copy_btn = QPushButton("Copiar Coordenadas")
            close_btn = QPushButton("Cerrar")
            copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(f"{lat}, {lon}"))
            close_btn.clicked.connect(dialog.close)
            buttons.addButton(copy_btn, QDialogButtonBox.ActionRole)
            buttons.addButton(close_btn, QDialogButtonBox.RejectRole)

            layout.addWidget(buttons)
            dialog.setLayout(layout)
            dialog.exec_()

        except Exception as e:
            QMessageBox.warning(self, "GPS", f"Error al obtener coordenadas:\n{e}")
        
    def load_prev_image(self):
        if self.image_list and self.current_index > 0:
            self.current_index -= 1
            self.load_image_from_path(self.image_list[self.current_index])

    def load_next_image(self):
        if self.image_list and self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.load_image_from_path(self.image_list[self.current_index])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MetadataViewer()
    viewer.show()
    sys.exit(app.exec_())
