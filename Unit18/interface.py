import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Nazwy klas Fashion-MNIST
CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# 1️⃣ Wczytanie zapisanego modelu
model = load_model("fashion_mnist_model")


def predict_and_show(image):
    """
    image: numpy array o kształcie (28, 28)
    """

    # 2️⃣ Preprocessing
    img = image.astype("float32") / 255.0
    img = img.reshape(1, 28, 28, 1)

    # 3️⃣ Predykcja
    probs = model.predict(img, verbose=0)
    pred_class = np.argmax(probs)
    confidence = np.max(probs)

    # 4️⃣ Wizualizacja
    plt.imshow(image, cmap="gray")
    plt.title(
        f"Predykcja: {CLASS_NAMES[pred_class]} "
        f"(pewność: {confidence:.2f})"
    )
    plt.axis("off")
    plt.show()

    return pred_class, confidence


# ▶️ Przykładowe użycie (test)
if __name__ == "__main__":
    from tensorflow.keras.datasets import fashion_mnist

    (_, _), (X_test, _) = fashion_mnist.load_data()
    predict_and_show(X_test[0])