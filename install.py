import os
import subprocess

# Clone the repository
subprocess.run(["git", "clone", "https://github.com/pierre-mazard/LINGUA-FRANCA.git"])

# Navigate to the project directory
os.chdir("LINGUA-FRANCA")

# Install Python dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])
