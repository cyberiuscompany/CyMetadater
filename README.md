
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
  <strong>Español</strong>
  &nbsp;|&nbsp;
  <a href="README.en.md">
    <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
    <strong>English</strong>
  </a>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="日本語" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>


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
- 🧭 Navegación por varias imágenes cargadas a la vez.
- 🎯 Minimización a bandeja del sistema (System Tray).
- 🛡️ Estilo visual adaptado a auditorías digitales y temas oscuros.

### 📁 Formatos de imagen compatibles

CyMetadater permite analizar metadatos de los siguientes formatos de imagen:

| Formato | Dispositivos / Origen común                                  |
|---------|--------------------------------------------------------------|
| `.jpg`  | Cámaras digitales, móviles Android, iPhone, WhatsApp         |
| `.jpeg` | iPhone, escáneres, cámaras compactas, software de edición    |
| `.png`  | Capturas de pantalla (PC y móvil), editores gráficos         |
| `.tiff` | Escáneres profesionales, impresoras, software de fotografía  |
| `.bmp`  | Windows Paint, capturas antiguas de Windows                  |
| `.webp` | Imágenes web (Google Chrome, WhatsApp Web, apps móviles)     |
| `.gif`  | Redes sociales, navegadores, apps de mensajería              |
| `.heic` | iPhone (8/9/10/11+), iPad, algunos Mac modernos                 |
  
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

### 🧼 Plataformas que eliminan metadatos EXIF al subir imágenes

| Plataforma           | ¿Elimina metadatos EXIF? | Detalles importantes                                                                 |
|----------------------|---------------------------|----------------------------------------------------------------------------------------|
| **WhatsApp**         | ✅ Sí                     | Comprime y elimina todos los EXIF, incluso ubicación.                                 |
| **Instagram**        | ✅ Sí                     | Borra metadatos al subir, tanto en publicaciones como historias.                     |
| **Facebook**         | ✅ Sí                     | Elimina EXIF en fotos subidas públicamente, aunque conserva internamente para análisis. |
| **Twitter (X)**      | ✅ Sí                     | Borra metadatos, aunque antes de 2020 permitía conservar algunos si eran JPG.        |
| **Telegram**         | 🚫 No (por defecto)       | Si se envía como archivo, mantiene EXIF. Si se envía como foto comprimida, lo borra. |
| **Google Fotos**     | ✅ Parcial                | Elimina algunos EXIF al compartir enlaces, pero mantiene todo en tu cuenta personal. |
| **iCloud**           | 🚫 No                     | Mantiene EXIF al subir fotos desde dispositivos Apple.                                |
| **Discord**          | ✅ Sí                     | Elimina metadatos en la vista previa. A veces puede conservar algunos en la descarga.|
| **LinkedIn**         | ✅ Sí                     | Elimina metadatos al subir imágenes a tu perfil o publicaciones.                     |
| **TikTok**           | ✅ Sí                     | Las miniaturas y vídeos/imágenes exportadas están limpias de EXIF.                   |
| **Reddit**           | ✅ Sí                     | Borra todos los metadatos de las imágenes subidas.                                   |
| **WeTransfer**       | 🚫 No                     | Transfiere los archivos tal como están, incluidos los metadatos.                     |

---

## 📄 Documentación adicional

- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [🔐 Seguridad](.github/SECURITY.md)
- [⚠️Aviso legal](DISCLAIMER.md)
- [📜 Licencia](LICENSE)
- [📢 Soporte](.github/SUPPORT.md)


---
## ⚙️ 📸 Obtener fotos para análisis de ejemplo

```bash
Abrir una consola Powershell

Ejecutar el siguiente comando:
Invoke-WebRequest "https://raw.githubusercontent.com/cyberiuscompany/CyMetadater/main/Fotos%20de%20Ejemplo/Cara%20Cyberius%20foto%20con%20XML.jpg" -OutFile "Cara Cyberius foto con XML.jpg"; Invoke-WebRequest "https://raw.githubusercontent.com/cyberiuscompany/CyMetadater/main/Fotos%20de%20Ejemplo/Mesa%20Salon%20Cyberius_SinGPS.JPG" -OutFile "Mesa Salon Cyberius_SinGPS.JPG"; Invoke-WebRequest "https://raw.githubusercontent.com/cyberiuscompany/CyMetadater/main/Fotos%20de%20Ejemplo/Silla%20Lectura%20Cyberius_ConGPS.HEIC" -OutFile "Silla Lectura Cyberius_ConGPS.HEIC"

```

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

