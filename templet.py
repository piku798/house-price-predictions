import os

# Define the project root name
project_name = "house-price-predictions"

# Define folder structure
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models",
    "app/templates",
    "app/static",
    "tests",
]

# Define files to be created with initial content
files = {
    ".gitignore": "venv/\n__pycache__/\n*.pyc\n.ipynb_checkpoints/\n.DS_Store\n",
    "README.md": f"# {project_name}\n\nIndustry-level ML project for predicting house prices.",
    "requirements.txt": "",
    "LICENSE": "MIT License\n\n# (Update with your own license text)",
    "src/__init__.py": "",
    "src/config.py": "# Configuration file for file paths and hyperparameters",
    "src/data_preprocessing.py": "# Code for data cleaning and preprocessing",
    "src/train_model.py": "# Code for training the ML model",
    "src/evaluate.py": "# Code to evaluate model performance",
    "src/predict.py": "# Load trained model and make predictions",
    "src/utils.py": "# Utility/helper functions",
    "app/app.py": "# Flask application entry point",
    "app/templates/index.html": "<!-- HTML frontend for prediction UI -->",
    "tests/test_model.py": "# Basic test for prediction function",
    "notebooks/eda.ipynb": "",  # Empty notebook placeholder
}

# Create project root directory
if not os.path.exists(project_name):
    os.mkdir(project_name)

# Create subfolders
for folder in folders:
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)

# Create files
for file_path, content in files.items():
    full_path = os.path.join(project_name, file_path)
    with open(full_path, "w") as f:
        f.write(content)

print(f"✅ Project '{project_name}' structure created successfully.")
