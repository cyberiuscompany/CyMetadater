[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@CyberiusCompany)
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

# CyMetadater
Esta es una herramienta visual desarrollada en Python con PyQt5 que permite analizar, visualizar, limpiar y exportar metadatos EXIF de imágenes. Está pensada para tareas de análisis forense, privacidad y auditoría de archivos multimedia.

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## Características principales

- ✅ Carga de imágenes por botón o arrastrar y soltar.
- 📸 Vista previa de la imagen seleccionada.
- 🔍 Visualización detallada de metadatos EXIF (incluye GPS, fecha, cámara, etc.).
- 🧹 Limpieza completa de metadatos EXIF (anonimización).
- 🌍 Detección de coordenadas GPS con vista integrada en Google Maps.
- 🧭 Enlace directo a GeoHack (Wikipedia Maps) para análisis geográfico forense.
- 📤 Exportación de metadatos a formatos `.json` y `.txt`.
- 🔎 Búsqueda dinámica de metadatos dentro de la tabla.
- 🖼️ Soporte para múltiples formatos de imagen: `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`, `.webp`, `.gif`, `.heic`.
- 🧭 Navegación por varias imágenes cargadas a la vez.
- 🎯 Minimización a bandeja del sistema (System Tray).
- 🛡️ Estilo visual adaptado a auditorías digitales y temas oscuros.

---

## 🎥 Demostración

<p align="center">
  <img src="Demo.gif" width="1200" alt="Demostración de CyberiusUnzipCracker">
</p>

---

## 📸 Fotos de Herramienta

<h2 align="center">Interfaz Principal</h2>
<p align="center">
  <img src="Fotos Herramienta/Interfaz Pricipal.png" alt="Foto 1" width="500"/>
</p>

<h2 align="center">Analizando Foto sin GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Analisis Foto sin GPS.png" alt="Foto 2" width="500"/>
</p>

<h2 align="center">Analizando Foto con GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Analisis Foto con GPS.png" alt="Foto 3" width="500"/>
</p>

<h2 align="center">Boton Ubicación GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Boton Ubicación GPS.png" alt="Foto 3" width="500"/>
</p>

<h2 align="center">Encntrando ubicación GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Ubicación GPS encontrada.png" alt="Foto 3" width="500"/>
</p>

## Requisitos

- Python 3.7 o superior
- PyQt5
- piexif
- pillow
- pillow-heif
- PyQtWebEngine

## 📁 Estructura del proyecto

```bash
├── .github/                        # Archivos de configuración para GitHub (acciones, plantillas, etc.)
├── Fotos Herramienta/             # Imágenes de demostración o capturas del uso de la herramienta
├── .gitattributes                 # Configuración de atributos Git
├── cyberius.ico                   # Icono principal de la aplicación
├── CyMetadater.py                 # Archivo principal con la interfaz y la lógica de la aplicación
├── CyMetadater.spec               # Archivo de configuración para PyInstaller (compilación a ejecutable)
├── Demo.gif                       # Demostración animada del funcionamiento de la herramienta
├── DISCLAIMER.md                  # Aviso legal o descargo de responsabilidad
├── icono.png                      # Icono alternativo o para la interfaz
├── LICENCE                        # Licencia del proyecto (probablemente MIT)
├── Mesa Salon Cyberius_SinGPS.JPG  # Imagen de prueba sin datos GPS
├── README.md                      # Documentación principal del proyecto
├── README.txt                     # Versión alternativa del README (quizás para ejecutables)
├── requirements.txt               # Lista de dependencias del proyecto
├── Silla Lectura Cyberius_ConGPS.HEIC  # Imagen de prueba con datos GPS
└── version.txt                    # Versión actual de la herramienta
```
---

## 📄 Documentación adicional

- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [🔐 Seguridad](.github/SECURITY.md)
- [⚠️Aviso legal](DISCLAIMER.md)
- [📜 Licencia](LICENSE)
- [📢 Soporte](.github/SUPPORT.md)


---

## ⚙️ 1.1 Instalación básica con clonado 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
python -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python CyMetadater.py
```

## ⚙️ 1.2 Instalación básica con clonado 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
python CyMetadater.py
```

## ⚙️ 2.1 Compilación básica de .exe dependiente tras clonado desde 🪟 Windows

```bash
# Crear el .exe del programa siendo versión binario ligero, dependiente de sus librerias
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
pip install pyinstaller
pyinstaller CyMetadater.spec

# Ejecutar el .exe del programa
CyMetadater/
├── dist/
│   └── CyMetadater/
│       └── CyMetadater.exe  ← ESTE ES EL EJECUTABLE

⚠️ **¡Atención!**
Si compilas con `pyinstaller CyMetadater.spec`, el ejecutable `.exe` se generará dentro de la carpeta `dist/`:
`dist/CyMetadater/CyMetadater.exe`
`dist/CyMetadater.exe`
Este .exe solo va funcionar, siempre y cuando no lo muevas de su carpeta, dado que **depende** las 
librerias que se encuentre en la carpeta adyance que veras junto al .exe
```

## ⚙️ 2.2 Compilación avanzada de .exe independiente tras clonado desde 🪟 Windows

```bash
# Crear el .exe del programa siendo versión binario pesado, con todo incluido
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
pip install pyinstaller
pyinstaller --onefile --windowed --icon=cyberius.ico --version-file=version.txt CyMetadater.py

# Ejecutar el .exe del programa
CyMetadater/
├── dist/
│   └── CyMetadater/
│       └── CyMetadater.exe  ← ESTE ES EL EJECUTABLE

⚠️ **¡Atención!**
Este binario lo puedes mover de lugar, dado que dentro del .exe contiene todo lo necesario para funcionar
pero tardara mas en abrirse, al ocupar mas tamaño y cargar mas funciones, librerías y DLLs.
```

