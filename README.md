# 🚀 CI/CD Pipeline for Flask Application using Jenkins & AWS

This project demonstrates an end-to-end CI/CD pipeline that automatically deploys a Flask application on an AWS EC2 instance whenever code is pushed to GitHub.

---

## 📌 Overview

The entire deployment process is fully automated:

GitHub Push → Webhook → Jenkins Pipeline → Code Sync → Dependency Install → Service Restart → Live Application

This eliminates manual deployment and ensures the application is always up to date.

---

## 🧰 Tech Stack

- Python (Flask)
- Jenkins (CI/CD Automation)
- AWS EC2 (Ubuntu)
- Nginx (Reverse Proxy)
- Gunicorn (WSGI Server)
- GitHub Webhooks
- rsync (File Synchronization)
- Linux (Systemd Services)

---

## ⚙️ Architecture
GitHub → Webhook → Jenkins → EC2 → Flask (Gunicorn) → Nginx → Browser


---

## 🔄 CI/CD Workflow

1. Code is pushed to GitHub  
2. GitHub webhook triggers Jenkins pipeline  
3. Jenkins pulls the latest code  
4. Files are synced to EC2 using rsync  
5. Python dependencies are installed  
6. Flask application is restarted using systemd  
7. Application becomes live via Nginx  

---

## 📁 Project Structure

flask-app/
├── app.py
├── requirements.txt
└── Jenkinsfile


---

## ⚙️ Jenkins Pipeline

The deployment is handled through a Jenkins pipeline defined in:
flask-app/Jenkinsfile


### Pipeline Stages:

- Copy Files (rsync)
- Install Dependencies
- Restart Service (systemd)

---

## 🛠️ Setup (Local)

Clone the repository:
git clone https://github.com/Sahil-Reshim/jenkins-python-demo.git
cd jenkins-python-demo/flask-app


Create virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Run locally:
python app.py


---

## 🌐 Deployment

- Application is deployed on AWS EC2  
- Gunicorn serves the Flask app  
- Nginx acts as a reverse proxy  
- Jenkins handles automated deployment  
- GitHub webhook triggers pipeline on every push  

---

## 🔐 Key Learnings

- Designing CI/CD pipelines using Jenkinsfile  
- Handling Linux permissions (jenkins vs ubuntu users)  
- Configuring sudoers for secure automation  
- Managing systemd services  
- Using rsync for efficient deployment  
- Debugging real-world CI/CD issues  

---

## 🌍 Live Application
⚠️ Note: The live server is not kept running continuously to optimize cloud costs.
The project has been fully tested and demonstrated using AWS EC2.


---

## 🚀 Future Improvements

- Dockerize the application  
- Add HTTPS using Certbot  
- Multi-environment deployment (dev/prod)  
- Monitoring and logging integration  

---

## 👨‍💻 Author

Sahil Reshim!

