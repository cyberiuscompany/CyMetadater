1. Crear un ejecutable ligero ejecutable desde "dist/CyMetadater/"
pyinstaller CyMetadater.spec

1. Crear un .exe único con todo incluido
pyinstaller --onefile --windowed --icon=cyberius.ico CyMetadater.py
pyinstaller --onefile --windowed --icon=cyberius.ico --version-file=version.txt CyMetadater.py

