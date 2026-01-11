import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

MODEL_PATH = "AUG_ACC0936-models.keras"

CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

if len(sys.argv) != 2:
    print("Użycie: python interface.py <ścieżka_do_obrazu>")
    sys.exit(1)

image_path = sys.argv[1]
model = load_model(MODEL_PATH)
img = cv2.imread(image_path)

if img is None:
    print("Nie można wczytać obrazu!")
    sys.exit(1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_28 = cv2.resize(img_gray, (28, 28))
img_norm = img_28.astype("float32") / 255.0
img_input = img_norm.reshape(1, 28, 28, 1)

probs = model.predict(img_input, verbose=0)
pred_class = np.argmax(probs)
confidence = np.max(probs)

plt.imshow(img_28, cmap="gray")
plt.title(
    f"Predykcja: {CLASS_NAMES[pred_class]} "
    f"(pewność: {confidence:.2f})"
)
plt.axis("off")
plt.show()

print(f"Predykcja klasa nr: {pred_class}")
print(f"Predykcja: {CLASS_NAMES[pred_class]}")
print(f"Pewność: {confidence:.3f}")
