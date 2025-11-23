# CCore-AI Demo Application

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Chroma-7E57C2?logo=undertow&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
</p>

<p>
  <img src="https://github.com/LaurisNeimanis/ccore-ai-demo/actions/workflows/build-backend.yml/badge.svg" />
  <img src="https://github.com/LaurisNeimanis/ccore-ai-demo/actions/workflows/build-frontend.yml/badge.svg" />
</p>

Application layer of the **CCore-AI** stack.  
This repository contains a fully containerized backend + frontend demo used by the
infrastructure project **ccore-ai-infra**.

---

## 1. Prerequisites

- Docker ≥ 24
- Docker Compose plugin
- GitHub Actions enabled for CI
- GHCR (images are public)

---

## 2. Features

- **FastAPI** backend
- **Streamlit** frontend
- **Chroma** vector DB (local demo mode)
- Clean Dockerfile separation (backend / frontend)
- GitHub Actions → GHCR build pipelines
- Production deployment is **pull-only** (no builds on EC2)

---

## 3. Technology Overview

### 3.1 Backend (FastAPI)

- Modular structure (API / services / config)
- Healthcheck endpoints for orchestration
- Deterministic builds via Poetry

### 3.2 Frontend (Streamlit)

- Minimal interactive UI
- Direct API communication
- Zero local dependencies (Docker only)

### 3.3 Chroma Vector Database

- Embedded vector store
- Basic RAG-style retrieval example
- No proprietary datasets

### 3.4 DevOps & Containers

- Separate backend + frontend Dockerfiles
- CI builds → GHCR images
- Production uses pull-based updates from **ccore-ai-infra**

---

## 4. Architecture (Repository-Local)

```mermaid
flowchart LR
    UI[Streamlit Frontend] --> API[FastAPI Backend]
    API --> DB[(Chroma Vector DB)]
```

> Nginx reverse proxy is added only at the infrastructure layer  
> (see `ccore-ai-infra` repo).

---

## 5. CI / CD Pipeline

```mermaid
flowchart LR
    A[Commit to Repo] --> B[GitHub Actions Build]
    B --> C[Build Backend & Frontend Images]
    C --> D[Push to GHCR]
    D --> E[ccore-ai-infra Deployment]
```

Production server never builds containers —  
it only **pulls** the latest images defined here.

---

## 6. Local Development

Run locally:

```bash
docker compose -f compose/docker-compose.dev.yml up --build
```

Frontend available at:

```
http://localhost:8501
```

Backend available at:

```
http://localhost:8000
```

---

## 7. Production Deployment (via ccore-ai-infra)

- Terraform provisions AWS infrastructure
- Ansible installs Docker Engine
- Ansible deploys a Docker Compose stack that pulls:

  - `ghcr.io/laurisneimanis/ccore-ai-demo-backend:latest`
  - `ghcr.io/laurisneimanis/ccore-ai-demo-frontend:latest`

- Nginx HTTPS termination and directory layout are handled by the infra project

🔗 Infrastructure repo:  
https://github.com/LaurisNeimanis/ccore-ai-infra

---

## 8. Security & Best Practices

- Deterministic CI builds
- No secrets baked into images
- Backend not exposed publicly (proxy-only architecture)
- HTTPS termination handled by infra
- GHCR authentication handled via GitHub Actions

---

## 9. Purpose

This repository provides a **clean demonstration** of:

- API + UI separation
- Containerized app design
- CI → image pipeline
- Integration with an IaC-controlled infrastructure stack

No production datasets or business logic included.

---

## License

MIT License.
