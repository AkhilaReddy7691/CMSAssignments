##Quiz App on Kubernetes

This project is a simple web-based Quiz App deployed using Docker and Kubernetes (Minikube). It showcases how to containerize a static web app and run it on a local Kubernetes cluster.

---

##Technologies Used

- HTML, CSS, JavaScript
- Docker 
- Kubernetes (Minikube) 
- Nginx (as web server)

---

##Project Structure

quiz-app/
├── index.html 
├── style.css 
├── script.js 
├── Dockerfile 
├── quiz-app-deployment.yaml 
└── quiz-app-service.yaml


---

##Setup Instructions

###Prerequisites

- Docker installed
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed
- kubectl installed

---

###Step-by-Step Deployment

1. Start Minikube

   ```bash
 minikube start

2. Build the Docker image

docker build -t quiz-app:latest .

3. Apply Kubernetes Deployment

kubectl apply -f quiz-app-deployment.yaml

4. Apply Kubernetes Service

kubectl apply -f quiz-app-service.yaml

5. Access the App

minikube service quiz-app-service

---

##Features

Interactive multiple-choice quiz

Tracks user score

Responsive UI

Full local Kubernetes deployment with NodePort


