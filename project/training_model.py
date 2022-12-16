import face_recognition as fr
import numpy as np


class ModelController:
    def __init__(self, data={'images':[], 'names':[]}):
        self.images = data['images']
        self.known_faces = []
        self.known_faces_names = data['names']
        self.train_model()

    def train_model(self): # feed images to model
        print("Model is being trained..")
        for image in self.images:
            encoded_image = fr.face_encodings(fr.load_image_file(image))[0]
            self.known_faces.append(encoded_image)
        print("Model training has been finished.")

    def get_know_faces(self): # get known faces
        return self.known_faces

    def compare_face_from_image(self, new_face): #compare faces with known faces
        print("Encoding new face...")
        encoded_new_face = fr.face_encodings(fr.load_image_file(new_face))[0]
        print('Comparing the face...')
        matches = fr.compare_faces(self.known_faces, encoded_new_face)
        if True in matches:

            first_match_index = matches.index(True)
            name = self.known_faces_names[first_match_index]
            print("Name: ", name)
        else:
            print("Not Found")

    def real_time_compare_face(self, frame):
        rgb_frame = frame[:, :, ::-1]
        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = fr.compare_faces(self.known_faces, face_encoding)
            name = "Unknown"
            face_distances = fr.face_distance(self.known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.known_faces_names[best_match_index]

            face_names.append(name)
        return face_locations, face_names



# model1 = ModelController({
#     'images': ['img_training_data/jeny.jpg', 'img_training_data/marufa.jpeg', 'img_training_data/tareque.jpg'],
#     'names' : ['Jeny', 'marufa', 'tareque']
# })
#
# # model1.train_model()
# model1.compare_face_from_image('img_training_data/formal.jpg')
