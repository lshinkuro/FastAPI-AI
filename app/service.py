import numpy as np
from sklearn.linear_model import LinearRegression

# Aplikasi AI Sederhana: Prediksi Harga Rumah

# Import library yang dibutuhkan

# Data contoh (harga rumah berdasarkan luas dan lokasi strategis)
luas_rumah = np.array([100, 150, 200, 250, 300, 100, 150, 200, 250, 300]).reshape((-1, 1))
lokasi_strategis = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])  # 1: strategis, 0: tidak strategis
harga_rumah = np.array([700, 950, 1200, 1500, 1800, 500, 700, 900, 1100, 1300])

# Gabungkan data luas dan lokasi menjadi satu matriks fitur
X = np.column_stack((luas_rumah, lokasi_strategis))

# Buat model regresi linear
model = LinearRegression()

# Latih model dengan data
model.fit(X, harga_rumah)

# Fungsi untuk prediksi harga rumah
def prediksi_harga(luas, strategis):
  harga = model.predict(np.array([[luas, strategis]]))[0]
  return harga
