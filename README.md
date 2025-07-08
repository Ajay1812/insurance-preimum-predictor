# 🏥 Insurance Premium Prediction App

This project is a full-stack machine learning web app to predict insurance premiums.

- ✅ **Backend:** FastAPI for serving the model (`ajayk01/insurance-premium-backend`)
- ✅ **Frontend:** Streamlit for user interaction (`ajayk01/insurance-premium-frontend`)
- ✅ **Dockerized:** Runs both services in isolated containers that communicate over a shared network.

---

## 📂 Project Structure

```
├── Backend
│   ├── app.py
│   ├── config
│   │   └── city_tier.py
│   ├── Dockerfile
│   ├── Model
│   │   ├── model.pkl
│   │   └── predict.py
│   ├── requirements.txt
│   └── schema
│       ├── prediction_response.py
│       └── user_input.py
├── docker-compose.yml
├── extras
│   ├── insurance.csv
│   └── serve_ml_with_fastAPI.ipynb
├── Frontend
│   ├── Dockerfile
│   ├── frontend.py
│   └── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repository

```bash

```

docker pull ajayk01/insurance-premium-backend
docker pull ajayk01/insurance-premium-frontend

docker network create insurance-network

# Run backend

docker run -d \
 --name fastapi-backend \
 --network insurance-network \
 -p 8000:8000 \
 ajayk01/insurance-premium-backend

# Run frontend

docker run -d \
 --name streamlit-frontend \
 --network insurance-network \
 -p 8501:8501 \
 ajayk01/insurance-premium-frontend
