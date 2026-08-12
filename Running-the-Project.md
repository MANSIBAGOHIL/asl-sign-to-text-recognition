## Running the Project

This repository contains three independent implementations: Random Forest, CNN, and YOLOv8. Use Python 3.10 for the best compatibility with the TensorFlow/Keras code.

### Prerequisites

- Python 3.10
- A webcam for real-time recognition
- Git

### 1. Clone the repository

```bash
git clone https://github.com/MANSIBAGOHIL/asl-sign-to-text-recognition.git
cd asl-sign-to-text-recognition
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> The CNN interface uses Tkinter and the `en_US` dictionary through PyEnchant. Tkinter is normally included with Python on Windows. Linux users may also need to install Tkinter and the Enchant system library through their package manager.

### Run the Random Forest webcam demo

The trained Random Forest model is already included as `random-forest/model.p`.

```bash
cd random-forest
python inference_classifier.py
```

Show an ASL alphabet sign to the webcam. Press `q` to close the recognition window.

To rebuild the Random Forest model from the included image dataset:

```bash
python create_dataset.py
python train_classifier.py
python inference_classifier.py
```

### Run the CNN desktop application

Before starting the CNN application, update the model paths in `cnn-asl/Application.py`. The script currently looks directly inside `Models`, but the uploaded model files are stored inside `Models/ICT_model`.

For example, change:

```python
open("Models\\model_new.json", "r")
```

to:

```python
open("Models/ICT_model/model_new.json", "r")
```

Apply the same change to all four `.json` paths and all four `.h5` paths in `Application.py`. Then run:

```bash
cd cnn-asl
python Application.py
```

The application opens a webcam-based Tkinter interface that displays the detected character, builds words and sentences, and provides spelling suggestions.

To retrain the CNN, first replace the local `D:\\STTC\\...` dataset paths in `cnn-asl/Models/Model.ipynb` with the location of your dataset. Then open the notebook:

```bash
jupyter notebook "Models/Model.ipynb"
```

### Run YOLOv8 inference

The repository includes trained YOLOv8 weights. From the repository root, run webcam inference with:

```bash
cd yolo-asl
yolo task=detect mode=predict model="runs/detect/train8/weights/best.pt" source=0 conf=0.25 show=True
```

To run inference on an image or folder, replace `source=0` with a path:

```bash
yolo task=detect mode=predict model="runs/detect/train8/weights/best.pt" source="path/to/image-or-folder" conf=0.25 save=True
```

### Retrain YOLOv8

Before training, update `yolo-asl/data.yaml` because it currently contains paths from the original Windows computer. Use paths matching your local repository, for example:

```yaml
path: .
train: train/images
val: valid/images
test: test-dataset/images

nc: 26
names: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
```

The current file repeats `F` in the class list and declares 27 classes. Correct it to the 26 unique letters shown above before retraining.

Run training from the `yolo-asl` directory:

```bash
yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=25 plots=True
```

Validate the trained model:

```bash
yolo task=detect mode=val model="runs/detect/train/weights/best.pt" data=data.yaml
```

Ultralytics creates a new numbered training directory when `runs/detect/train` already exists. Adjust the validation model path to the directory produced by your run.
