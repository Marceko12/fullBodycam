# Detección de Cuerpo Completo con Haar Cascade y OpenCV

Este proyecto realiza la **detección de cuerpo completo (Full Body Detection)** en tiempo real utilizando la cámara web del dispositivo. Para ello se utiliza el algoritmo **Haar Cascade Classifier** proporcionado por **OpenCV**, una de las bibliotecas más populares para visión por computadora en Python.

## 📷 Funcionalidad

- Captura de video en tiempo real desde la cámara web.
- Detección de cuerpos completos usando el clasificador Haarcascade preentrenado (`haarcascade_fullbody.xml`).
- Dibujo de rectángulos alrededor de los cuerpos detectados.

## 🚀 Requisitos

- Python 3.x
- OpenCV (cv2)

### Instalación de dependencias

```bash
pip install opencv-python
