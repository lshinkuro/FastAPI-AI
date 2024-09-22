import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from io import BytesIO
from PIL import Image

# Fungsi untuk memproses gambar
def preprocess_image(image_data):
    # Menggunakan Pillow untuk membuka gambar dari byte array
    image = np.array(Image.open(BytesIO(image_data)))
    
    # Jika gambar tidak dalam format grayscale, konversi ke grayscale
    if len(image.shape) == 3:  # Jika gambar berwarna (RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image  # Jika sudah grayscale
    
    # Ubah ukuran gambar menjadi (48x48)
    resized = cv2.resize(gray, (48, 48))
    
    # Normalisasi gambar
    normalized = resized / 255.0
    
    # Ekspansi dimensi gambar agar sesuai dengan input model
    return np.expand_dims(normalized, axis=(0, -1))

# Buat model CNN sederhana (Anda bisa mengganti dengan model yang lebih canggih)
model = Sequential()
# Layer 1 - Conv Layer
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # Dropout to reduce overfitting

# Layer 2 - Conv Layer
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Layer 3 - Conv Layer
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Layer 4 - Conv Layer (Optional)
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Flatten the results to feed into a fully connected (Dense) network
model.add(Flatten())

# Fully Connected Layer 1
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

# Fully Connected Layer 2
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

# Output Layer (3 kelas: Senyum, Marah, Tertawa)
model.add(Dense(3, activation='softmax'))  # 3 classes
# Contoh penggunaan (Anda perlu mengganti dengan data training yang sesuai)
# ... (mulai latihan dengan data gambar yang sudah dilabel) ...

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fungsi untuk mendeteksi ekspresi wajah
def detect_expression(image_path):
  preprocessed_image = preprocess_image(image_path)
  prediction = model.predict(preprocessed_image)
  expression_labels = ['Senyum', 'Marah', 'Tertawa']
  predicted_expression = expression_labels[np.argmax(prediction)]
  return predicted_expression

# Contoh penggunaan
# image_path = 'path/to/your/image.jpg'  # Ganti dengan path gambar Anda
# expression = detect_expression(image_path)
# print(f"Ekspresi wajah yang terdeteksi: {expression}") 

# Anda perlu melatih model dengan data yang cukup untuk mendapatkan hasil yang baik.
#  Pertimbangkan untuk menggunakan dataset seperti FER2013.
# Anda juga dapat meningkatkan akurasi dengan menggunakan model yang lebih kompleks
#  dan teknik augmentasi data.