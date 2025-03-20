# Diabetes risk identifier using machine learning
A **GUI-based Prediction Application** designed to process user inputs and generate predictions. This application leverages a clean user interface and integrates predictive functionality, likely powered by a machine learning model or related logic.
## 📝 Overview
This project allows users to input various parameters such as `age`, `bmi`, `sugar`, `systolic bp`, and receive insights or predictions based on their values. The GUI is designed for ease of use and includes dynamic entry fields, buttons, and canvas integration.
## ⚙️ Features
- **User Inputs**:
    - Input fields for attributes such as `Age`, `BMI`, `Blood Pressure`, and more.

- **Dynamic GUI**:
    - Uses canvas and images to create an interactive user-friendly interface.

- **Predictive Modeling**:
    - A `prediction` function handles the inputs and provides results or forecasts.

- **Asset Management**:
    - All graphical and static resources are managed dynamically using paths like `OUTPUT_PATH` and `ASSETS_PATH`.

## 🛠️ Installation
1. **Clone the Repository**:
``` bash
   git clone https://github.com/hodini007/diabetes_classifier_app.git
```
1. **Navigate into the Directory**:
``` bash
   cd diabetes_classifier_app
```
1. **Install the Dependencies**: Ensure you have Python installed, then use:
``` bash
   pip install -r requirements.txt
```
1. **Prepare Assets**: Place all necessary graphical assets (e.g., background images, entry images) into the appropriate `assets` directory or adjust the `ASSETS_PATH` in the code.

## 🚀 Usage
1. Run the application:
``` bash
   python gui.py
```
1. A GUI window will appear. Follow these steps:
    - Input your values in the respective fields (Age, BMI, Blood Pressure, etc.).
    - Click on the button to generate predictions.

2. View your result directly in the GUI window.

## 📂 Project Structure
``` 
├── assets/
│   ├── images/               # Store all image assets here
│   ├── icons/                # Store any icons for the GUI
│   └── ...                   # Other asset folders
├── main.py                   # Main application script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── utils/
    ├── helpers.py            # Utility/helper functions
    └── prediction.py         # Prediction logic
```
## 🔧 Configuration
- **Paths Configuration**:
    - Adjust `OUTPUT_PATH` and `ASSETS_PATH` in the script if the directories differ.

- _Assets_: Ensure all necessary images and icons (referenced by the code) are present in the `assets` directory.

## 🤔 Troubleshooting
- **Missing File Errors**:
    - Ensure `ASSETS_PATH` is pointing to the correct directory, and all required files are present.

- **Prediction Not Working**:
    - Make sure the `prediction` function is working correctly and the underlying model (if any) is trained and loaded.

- **GUI Not Displaying Correctly**:
    - Check the resolution of the images and ensure they fit properly within the canvas or window.

## 📜 License
This project is licensed under the **MIT License**.
## 📧 Contact
For any questions or support, reach out to:
**Your Name**
- Email: [raiyanrohit10@gmail.com]()
- GitHub: [hoodini007](https://https://github.com/hodini007)

You can customize this README further to reflect the specifics of your project, such as additional features, contributors, or advanced configuration details. Let me know if you need any additional sections or specific adjustments!
