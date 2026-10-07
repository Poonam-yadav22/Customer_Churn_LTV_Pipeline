# 🖼️ CIFAR-10 Image Classification using CNN

A Deep Learning web application that classifies images into one of the **10 CIFAR-10 object categories** using a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras** and deployed using **Streamlit**. The app supports both **image upload** and **webcam capture** for real-time predictions. Streamlit makes it easy to build and deploy interactive machine learning applications in Python. :contentReference[oaicite:0]{index=0}

## 🚀 Live Demo

**🌐 Try the App:**  
https://cnncifarproject-eyqzk6a68ac7xjyd7jy4ve.streamlit.app/

---

## 📌 Features

- 🧠 CNN model trained on the CIFAR-10 dataset
- 📂 Upload images for prediction
- 📷 Capture images directly using your webcam
- 🎯 Predicts one of 10 object classes
- 📊 Displays confidence score
- 📈 Shows probability for every class
- ⚡ Fast and interactive Streamlit interface
- 📱 Responsive and beginner-friendly UI

---

## 🗂️ Supported Classes

| Class | Class |
|-------|-------|
| ✈️ Airplane | 🚗 Automobile |
| 🐦 Bird | 🐱 Cat |
| 🦌 Deer | 🐶 Dog |
| 🐸 Frog | 🐴 Horse |
| 🚢 Ship | 🚚 Truck |

---

## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow

---

## 🧠 CNN Architecture

```text
Input Image (32×32×3)
        │
        ▼
Conv2D (32 Filters)
        │
MaxPooling2D
        │
Conv2D (64 Filters)
        │
MaxPooling2D
        │
Conv2D (64 Filters)
        │
Flatten
        │
Dense (64)
        │
Dropout (0.5)
        │
Dense (10 - Softmax)
```

---

## 📈 Model Performance

| Metric | Result |
|--------|-------:|
| Training Accuracy | ~78% |
| Validation Accuracy | ~73% |
| Test Accuracy | **71.82%** |

---

## 📂 Project Structure

```text
CIFAR10-Image-Classifier/
│
├── app.py
├── cifar10_cnn.keras
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

Add screenshots of:

- 🏠 Home Screen
- 📂 Image Upload
- 📷 Camera Capture
- 🎯 Prediction Result
- 📊 Confidence & Probability Scores

---

## 🎯 Future Improvements

- Higher accuracy using Data Augmentation
- Batch Normalization
- Early Stopping
- Transfer Learning (ResNet50 / MobileNetV2)
- Top-3 Predictions
- Dark Mode UI

---

## 👨‍💻 Developer

**Prateek Verma**

B.Tech Information Technology

Deep Learning • Computer Vision • TensorFlow • Streamlit

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to fork it!

---

## 📄 License

This project is developed for educational and learning purposes.
