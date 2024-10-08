import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is running. Press 's' to save a photo, move your face away to exit.")

    no_face_frames = 0
    threshold_no_face_frames = 30  

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            no_face_frames = 0
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        else:
            no_face_frames += 1

        cv2.imshow('Video Feed', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            image_path = 'captured_photo.jpg'
            cv2.imwrite(image_path, frame)
            print(f"Photo saved as {image_path}")

        if no_face_frames > threshold_no_face_frames:
            print("No face detected for a while. Exiting camera.")
            break

        elif key == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
