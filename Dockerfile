# Menggunakan image Python sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Update dan install dependencies sistem yang dibutuhkan
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglib2.0-0 \
    pkg-config \
    libhdf5-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file aplikasi ke dalam container
COPY . .

# Menentukan port yang akan digunakan
EXPOSE 8000

# Menjalankan aplikasi dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

