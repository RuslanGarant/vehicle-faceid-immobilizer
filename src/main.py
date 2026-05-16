import cv2
import face_recognition
import time

# Simulation of hardware relay for vehicle ignition
class VehicleIgnitionRelay:
    def __init__(self):
        self.is_locked = True

    def unlock_ignition(self):
        self.is_locked = False
        print("[HARDWARE] Ignition UNLOCKED. Ready to start engine.")

    def lock_ignition(self):
        self.is_locked = True
        print("[HARDWARE] Ignition LOCKED. Access denied.")

def authorize_driver(allowed_driver_image_path):
    # Load the authorized driver's face profile
    allowed_image = face_recognition.load_image_file(allowed_driver_image_path)
    allowed_encoding = face_recognition.face_encodings(allowed_image)[0]

    # Initialize vehicle camera (DSM / In-cabin camera)
    video_capture = cv2.VideoCapture(0)
    relay = VehicleIgnitionRelay()

    print("[SYSTEM] Scanning driver's face...")
    time.sleep(1) # Simulate camera warmup

    ret, frame = video_capture.read()
    if not ret:
        print("[ERROR] Camera failure. Safety protocol: Ignition remains locked.")
        return

    # Find faces in the current camera frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    authenticated = False
    for face_encoding in face_encodings:
        # Compare face with the database ID
        matches = face_recognition.compare_faces([allowed_encoding], face_encoding)
        if True in matches:
            authenticated = True
            break

    if authenticated:
        print("[SUCCESS] Driver verified successfully.")
        relay.unlock_ignition()
    else:
        print("[SECURITY ALERT] Unauthorized driver detected. Engine start blocked.")
        relay.lock_ignition()

    video_capture.release()

if __name__ == "__main__":
    # Path to the registered driver's ID photo in the system
    DRIVE_ID_DATABASE = "data/authorized_driver.jpg"
    authorize_driver(DRIVE_ID_DATABASE)
