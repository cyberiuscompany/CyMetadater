
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@CyberiusCompany)
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/CyMetadater/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

<p align="center">
  <a href="README.md">
    <img src="https://flagcdn.com/w40/es.png" alt="Spanish" title="Spanish">
    <strong>Spanish</strong>
  </a>
  &nbsp;|&nbsp;
  <a href="README.en.md">
    <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
    <strong>English</strong>
  </a>
</p>

# CyMetadater
This is a visual tool developed in Python with PyQt5 that allows you to analyze, view, clean, and export EXIF metadata from images. It is designed for forensic analysis, privacy, and multimedia file audits.

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p>

---

## Main Features

- ✅ Load images manually or by drag and drop.
- 📸 Preview of the selected image.
- 🔍 Detailed visualization of EXIF metadata (including GPS, date, camera, etc.).
- 🧹 Full EXIF metadata cleaning (anonymization).
- 🌍 GPS coordinate detection with integrated Google Maps view.
- 🧭 Direct link to GeoHack (Wikipedia Maps) for forensic geo-analysis.
- 📤 Export metadata to `.json` and `.txt` formats.
- 🔎 Dynamic metadata search in the table.
- 🧭 Navigate through multiple loaded images.
- 🎯 Minimize to system tray.
- 🛡️ Visual style adapted for digital audits and dark themes.

### 📁 Supported Image Formats

CyMetadater supports the analysis of metadata in the following image formats:

| Format  | Typical Devices / Sources                                      |
|---------|----------------------------------------------------------------|
| `.jpg`  | Digital cameras, Android phones, iPhones, WhatsApp             |
| `.jpeg` | iPhones, scanners, compact cameras, editing software           |
| `.png`  | Screenshots (PC and mobile), graphic editors                   |
| `.tiff` | Professional scanners, printers, photography software          |
| `.bmp`  | Windows Paint, old Windows screenshots                         |
| `.webp` | Web images (Google Chrome, WhatsApp Web, mobile apps)         |
| `.gif`  | Social media, browsers, messaging apps                         |
| `.heic` | iPhones (8/9/10/11+), iPads, some modern Macs                  |

---

## 🎥 Demonstration

<p align="center">
  <img src="Demo.gif" width="1200" alt="Demonstration of CyMetadater">
</p>

---

## 📸 Tool Screenshots

<h2 align="center">Main Interface</h2>
<p align="center">
  <img src="Fotos Herramienta/Interfaz Pricipal.png" alt="Screenshot 1" width="500"/>
</p>

<h2 align="center">Analyzing Photo without GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Analisis Foto sin GPS.png" alt="Screenshot 2" width="500"/>
</p>

<h2 align="center">Analyzing Photo with GPS</h2>
<p align="center">
  <img src="Fotos Herramienta/Analisis Foto con GPS.png" alt="Screenshot 3" width="500"/>
</p>

<h2 align="center">GPS Button</h2>
<p align="center">
  <img src="Fotos Herramienta/Boton Ubicación GPS.png" alt="Screenshot 4" width="500"/>
</p>

<h2 align="center">GPS Location Found</h2>
<p align="center">
  <img src="Fotos Herramienta/Ubicación GPS encontrada.png" alt="Screenshot 5" width="500"/>
</p>

## Requirements

- Python 3.7 or higher
- PyQt5
- piexif
- pillow
- pillow-heif
- PyQtWebEngine

## 📁 Project Structure

```bash
├── .github/                        # GitHub configuration files (actions, templates, etc.)
├── Fotos Herramienta/             # Demo images or screenshots
├── .gitattributes                 # Git attribute configuration
├── cyberius.ico                   # Application icon
├── CyMetadater.py                 # Main file with GUI and logic
├── CyMetadater.spec               # PyInstaller configuration file
├── Demo.gif                       # Animated demo of the tool
├── DISCLAIMER.md                  # Legal disclaimer
├── icono.png                      # Alternative icon for UI
├── LICENCE                        # Project license (probably MIT)
├── Mesa Salon Cyberius_SinGPS.JPG  # Sample image without GPS
├── README.md                      # Main documentation in Spanish
├── README.txt                     # Alternate README for portable versions
├── requirements.txt               # Dependency list
├── Silla Lectura Cyberius_ConGPS.HEIC  # Sample image with GPS
└── version.txt                    # Current tool version
```
---

### 🧼 Platforms that Remove EXIF Metadata

| Platform            | Removes EXIF? | Important Notes                                                                |
|---------------------|----------------|----------------------------------------------------------------------------------|
| **WhatsApp**        | ✅ Yes         | Compresses and removes all EXIF including location.                             |
| **Instagram**       | ✅ Yes         | Removes metadata for both posts and stories.                                   |
| **Facebook**        | ✅ Yes         | Removes EXIF publicly; retains it internally for analysis.                      |
| **Twitter (X)**     | ✅ Yes         | Removes metadata (allowed partial EXIF until 2020 for JPG).                     |
| **Telegram**        | 🚫 No          | Keeps EXIF when sent as file; removes when sent as compressed image.           |
| **Google Photos**   | ✅ Partial     | Removes some EXIF on shared links but keeps it in your private account.         |
| **iCloud**          | 🚫 No          | Retains full EXIF when uploading from Apple devices.                            |
| **Discord**         | ✅ Yes         | Removes metadata from previews; sometimes keeps it in file downloads.           |
| **LinkedIn**        | ✅ Yes         | Strips metadata from profile and post images.                                   |
| **TikTok**          | ✅ Yes         | Thumbnails and exported content are EXIF-clean.                                 |
| **Reddit**          | ✅ Yes         | Removes all EXIF from uploaded images.                                          |
| **WeTransfer**      | 🚫 No          | Transfers files exactly as-is, with all metadata intact.                        |

---

## 📄 Additional Documentation

- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 How to Contribute](.github/CONTRIBUTING.md)
- [🔐 Security](.github/SECURITY.md)
- [⚠️ Legal Notice](DISCLAIMER.md)
- [📜 License](LICENSE)
- [📢 Support](.github/SUPPORT.md)

---

## ⚙️ 1.1 Basic Installation via Git (🪟 Windows)

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
python -m venv venv (Optional)
.env\Scriptsctivate (Optional)
pip install -r requirements.txt
python CyMetadater.py
```

## ⚙️ 1.2 Basic Installation via Git (🐧 Linux / macOS)

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python CyMetadater.py
```

## ⚙️ 2.1 Basic .exe Build (Lightweight version, Windows)

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
pip install pyinstaller
pyinstaller CyMetadater.spec

CyMetadater/
├── dist/
│   └── CyMetadater/
│       └── CyMetadater.exe  ← THIS IS THE EXECUTABLE

⚠️ **Warning!**
If you compile using `pyinstaller CyMetadater.spec`, the `.exe` will be generated inside `dist/`:
`dist/CyMetadater/CyMetadater.exe`
`dist/CyMetadater.exe`

This `.exe` will only work if kept in its original folder, since it depends on adjacent libraries in the same directory.
```

## ⚙️ 2.2 Advanced .exe Build (Standalone binary, Windows)

```bash
git clone https://github.com/cyberiuscompany/CyMetadater.git
cd CyMetadater
pip install pyinstaller
pyinstaller --onefile --windowed --icon=cyberius.ico --version-file=version.txt CyMetadater.py

CyMetadater/
├── dist/
│   └── CyMetadater.exe  ← THIS IS THE EXECUTABLE

⚠️ **Warning!**
This binary can be moved freely, since it includes all necessary resources internally,
but it may take longer to start due to size and load time of embedded libraries and DLLs.
```
