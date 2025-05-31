import cv2

def main():
    # Cargar clasificador Haar para cuerpo completo
    fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

    # Ajusta estos tamaños para filtrar detecciones por tamaño (distancia aproximada)
    MIN_SIZE = (100, 200)  # mínimo ancho y alto de cuerpo detectado
    MAX_SIZE = (1000, 2000)  # máximo ancho y alto para evitar detecciones enormes (ruido)

    # Iniciar captura de video
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # ancho
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # alto

    cv2.namedWindow("Detección Cuerpo Completo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Detección Cuerpo Completo", 1280, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar cuerpos completos
        bodies = fullbody_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(120, 240),  # Más grande para filtrar objetos pequeños
            flags=cv2.CASCADE_SCALE_IMAGE
        )


        # Imprimir tamaños detectados para ajuste manual
        for (x, y, w, h) in bodies:
            print(f"Detección tamaño: ancho={w}, alto={h}")

        # Filtrar detecciones por tamaño para "distancia"
        filtered_bodies = []
        for (x, y, w, h) in bodies:
            if MIN_SIZE[0] <= w <= MAX_SIZE[0] and MIN_SIZE[1] <= h <= MAX_SIZE[1]:
                filtered_bodies.append((x, y, w, h))

        # Dibujar rectángulos en detecciones filtradas
        for (x, y, w, h) in filtered_bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Cuerpo Detectado", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Detección Cuerpo Completo", frame)

        # Salir con tecla ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
