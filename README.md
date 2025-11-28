# DevSecOps Dashboard — CI/CD Security Demonstration

A fully secure and functional DevSecOps pipeline with automated quality gates, containerized deployment, and a visual dashboard for academic presentations.

---

## ⭐ Project Overview

This project demonstrates a complete **DevSecOps workflow** using a dummy Python login system integrated into a secure CI/CD pipeline.

The custom **DevSecOps Dashboard** acts as a visual layer to show:

- How automated CI/CD pipelines function
- How security gates (SAST) enforce safe deployments
- How code flows through **GitHub → Jenkins → SonarQube → Docker → Deployment**

The dashboard is a presentation-friendly UI and does not replace Jenkins or SonarQube.

---

## 🚀 What’s New in This Updated Version?

✔ All previously detected vulnerabilities have been resolved  
✔ SonarQube Quality Gate passes successfully  
✔ Jenkins pipeline builds and deploys without errors  
✔ Docker image builds correctly and runs as a container  
✔ Dashboard displays healthy security posture  
✔ Project is stable and presentation-ready  

---

## 📌 CI/CD Pipeline Flow

The pipeline runs automatically when code is pushed to GitHub.

### **Stage Summary**

| Stage | Tool | Purpose |
|-------|-------|---------|
| **1. GitHub Push** | GitHub | Triggers Jenkins pipeline |
| **2. Continuous Integration** | Jenkins | Executes automated build steps |
| **3. Static Code Analysis** | SonarQube | SAST, code quality checks |
| **4. Docker Build** | Docker | Builds image only if quality gate passes |
| **5. Deployment** | Docker Engine | Runs the container locally |

---

## 🔐 Security Gate Logic (Updated)

### **Quality Gate Result → Pipeline Behavior**

| Quality Gate | Pipeline Behavior |
|--------------|------------------|
| 🟢 **PASS (Current Status)** | Build continues → Docker image created → Deployment successful |
| 🔴 FAIL | Build stops → No deployment → Vulnerable code blocked |

✔ **Current Status: PASS** — zero high-severity issues.

---

## 🎯 Purpose of the Dashboard

The dashboard provides a visual and simplified explanation of DevSecOps concepts:

- ✔ Security status overview  
- ✔ SonarQube results  
- ✔ Jenkins build status  
- ✔ Docker deployment confirmation  
- ✔ Pipeline stage visualization  

This makes it easier to present the project without opening heavy tools live.

---

## 🖥 Live Demo Workflow

1. User logs in via **index.html**  
2. Upon successful login → redirected to **dashboard.html**  
3. Dashboard displays:
   - Security scan summary  
   - Quality Gate **PASSED**  
   - Jenkins build success  
   - Deployment confirmation  
   - Pipeline stage flow  

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python |
| **CI/CD** | Jenkins |
| **Security Scanning** | SonarQube |
| **Containerization** | Docker |

---

## 🔮 Future Enhancements

- 🔗 Real-time API integration with Jenkins & SonarQube  
- 📊 Security history & analytics charts  
- 🔐 JWT-based secure login  
- 👥 Role-based access dashboard  
- 🧪 Add DAST testing (OWASP ZAP)  
- 🛡 Trivy container vulnerability scanning  

---

## 👥 Team Members

- **Dimple Lulla** — Team Lead (500120422), Batch-2  
- **Anshi Agrawal** — Project Lead (500124498), Batch-1  
- **Vansh Thakral** —  (500125288), Batch-1  
- **Jiya Tyagi** —     (500119743), Batch-2  

---

## ✅ Conclusion

This project showcases a complete **end-to-end DevSecOps ecosystem**, demonstrating how secure development, automated testing, and controlled deployments prevent vulnerabilities from entering production.


---

