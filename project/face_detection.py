import cv2 as cv
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, VideoProcessorBase, WebRtcMode
import streamlit as st
from training_model import ModelController
try:
    face_cascade = cv.CascadeClassifier('XML/haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")
def getHaarcascade():
    try:
        return cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    except Exception:
        print(Exception)
        st.write("Error loading cascade classifiers")

class DetectFace(VideoTransformerBase):
    process_this_frame = True
    model_obj = ModelController({
        "images": ['img_training_data/formal.jpg', 'img_training_data/jeny.jpg'],
        "names": ['Tareque', 'Jeny']
    })

    face_locations, face_names = [], []

    def transform(self, frame):
        frame = frame.to_ndarray(format="bgr24")

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if self.process_this_frame:
            # print("upcomming")
            self.face_locations, self.face_names = self.model_obj.real_time_compare_face(frame)



        self.process_this_frame = not self.process_this_frame


        #Display the result

        # for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
        #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     # Draw a box around the face
        #     cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        #     font = cv.FONT_HERSHEY_DUPLEX
        #     cv.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # # Detect the faces
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

        # faces = getHaarcascade().detectMultiScale(
        #     image=img_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h), name in zip(faces, self.face_names):
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(frame, name, (h + 6, w - 6), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

        print(self.face_names)
        return frame




