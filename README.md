
# DevSecOps Dashboard — CI/CD Security Demo

This dashboard is the visual demonstration layer of the **DevSecOps Python Login Project**.  
It is designed to help during **viva / project presentations** by showing how the CI/CD pipeline behaves after a secure login.

The dashboard does **not** replace Jenkins or SonarQube — instead, it provides a **user-friendly representation** of the pipeline results and security posture.

---

## 📌 What the Dashboard Represents

Once the dummy login system code is pushed to **GitHub**, the backend is processed through the following DevSecOps pipeline:

| Stage | Tool | Purpose |
|-------|------|---------|
| 1 | GitHub | Developer code push triggers pipeline |
| 2 | Jenkins CI | Automates pipeline execution |
| 3 | SonarQube Scan | Static Application Security Testing (SAST) & Quality Gate |
| 4 | Docker Build | Application containerized only if quality gate SUCCESS |
| 5 | Local Deploy | Docker container runs locally as a deployment step |

If **SonarQube finds high-severity vulnerabilities**, the pipeline stops and:
🛑 No Docker image is built  
🛑 No deployment happens  

If security passes the **quality gate**:
🟢 Image is built  
🟢 Container deployment happens  
🟢 Dashboard can be shown live

---
### 🔎 Pipeline Gate Logic

| Quality Gate Status | Behavior |
|---------------------|----------|
| 🟢 **PASS**     | Pipeline continues → Docker image built → Application deployment |
| 🔴 **FAIL** | Pipeline stops → No deployment → Prevents vulnerabilities from going live |

✔ This is a real DevSecOps security enforcement example


## 🎯 Dashboard Goals

This UI allows presenters to visually explain:

- The final security posture of the system  
- The role of SonarQube and Jenkins in enforcing security  
- The DevSecOps automation flow  
- The effect of **security gate** on deployment

It highlights:

- Vulnerabilities (after latest scan)
- Code Smells
- Build status from Jenkins
- Container deployment status
- Full pipeline stage breakdown

---

## 🖥️ Live Demo Workflow

1. User logs in via `index.html`
2. Login success redirects to `dashboard.html`
3. Dashboard shows:
   - Security scan results
   - Build health
   - Whether deployment occurred
   - Pipeline stages

Students can use this dashboard during viva to **explain DevSecOps without opening Jenkins / SonarQube UI**.

---

## 📂 Files

```

Dummy-login-python/
├── frontend/
│   ├── index.html       # Login page UI
│   ├── dashboard.html   # Visual view of pipeline result
│   ├── app.js
│   ├── dashboard.js
│   └── styles.css
│
├── auth.py              # Simple backend authentication logic
├── login.py             # Main backend
├── config.py            # Configuration variables
│
├── requirements.txt     # Python dependencies
├── Dockerfile           # Containerization for final deployment
├── Jenkinsfile          # CI/CD automation pipeline
├── sonar-project.properties # SonarQube scan configuration
│
├── README.md
└── DevSecOps Project Report .docx 
```

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python |
| Containerization | Docker |
| CI/CD | Jenkins |
| Security Scan | SonarQube |

---

## 🔮 Possible Future Additions

- Live API connection to Jenkins/SonarQube via webhooks
- History chart (vulnerabilities over time)
- Re-login via JWT token security
- Role-based dashboard access

---

## 🙌 About Team:
Dimple Lulla (Team Lead)	   500120422	Batch-2
Anshi Agrawal (Project Lead)	500124498	Batch-1
Vansh Thakral	               500125288	Batch-1
Jiya Tyagi	                  500119743	Batch-2

This dashboard is for academic demonstration of:
- **DevSecOps**
- **Security Gates in CI/CD**
- **Secure deployment flow automation**
```
