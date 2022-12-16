import cv2 as cv
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, VideoProcessorBase, WebRtcMode
import streamlit as st
from face_detection import DetectFace
from Pages import home_page, about_page



RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

def main():
    # Face Analysis Application #
    st.title("Real Time Face Emotion Detection Application")
    activiteis = ["Home", "Webcam Face Detection", "Add New Person", "About"]
    choice = st.sidebar.selectbox("Select Activity", activiteis)
    st.sidebar.markdown(
        """ Developed by Mohammad Juned Khan    
            Email : Mohammad.juned.z.khan@gmail.com  
            [LinkedIn] (https://www.linkedin.com/in/md-juned-khan)""")
    if choice == "Home":
        st.markdown(home_page.title(), unsafe_allow_html=True)
        st.write(home_page.body())
    elif choice == "Webcam Face Detection":
        st.header("Webcam Live Feed")
        st.write("Click on start to use webcam and detect your face emotion")
        webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV, rtc_configuration=RTC_CONFIGURATION,
                        video_processor_factory=DetectFace)
    elif choice == 'Add New Person':
        st.header("Add New Person")

        picture = st.camera_input("Take Photo")
        if picture:
            st.image(picture)
            name = st.text_input("Name")
            phone = st.number_input("Mobile Number", min_value=None, max_value=None,)
            email = st.text_input("Email")
            about = st.text_area("Add Details")
            st.button("Add")



    elif choice == "About":
        st.subheader(about_page.subheader())
        st.markdown(about_page.body_1(), unsafe_allow_html=True)
        st.markdown(about_page.body_2(), unsafe_allow_html=True)

    else:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
