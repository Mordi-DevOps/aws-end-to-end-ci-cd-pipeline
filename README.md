# AWS End-to-End CI/CD Pipeline — DevOps Portfolio Project

This repository demonstrates the evolution of a production-grade CI/CD platform on AWS, progressing from a basic container deployment pipeline to a secure private architecture and finally to an on-demand, cost-optimized infrastructure model.

The project is structured into multiple architectural levels, each representing an upgrade in maturity, security posture, and automation capability.

---

## 📁 Repository Architecture Levels

| Level | Directory | Focus |
|------|-------------|-------|
| Level 1 | webapp | Foundational CI/CD pipeline |
| Level 2 | webapp-upgrade-1 | Secure private AWS architecture |
| Level 3 | webapp-upgrade-2 | On-demand infrastructure (planned) |

---

## 🧭 Architecture Evolution

### Level 1 — Functional Pipeline
- Jenkins builds and deploys Dockerized app
- Public EC2 deployment
- SSH-based delivery

### Level 2 — Production Security Upgrade
- Private subnets
- ALB public entrypoint
- SSM deployment
- No SSH / No EIPs

### Level 3 — Cost Optimization (Planned)
- Auto start/stop infrastructure
- Scale-to-zero compute
- Event-driven activation

---

## 🔧 Core Technologies

- Jenkins
- Docker
- AWS EC2 / VPC / ALB / SSM
- GitLab
- Docker Hub
- Slack
- Flask

---

## 📊 Key DevOps Capabilities Demonstrated

- CI/CD pipeline automation
- Containerization
- Secure VPC design
- IAM least-privilege deployment
- Webhook-driven builds
- Private compute architecture
- Load-balanced application routing

---

## 📐 Architecture Diagrams

See:

architecture/


For visual system designs across project levels.

---

## 🧠 Engineering Focus

This project emphasizes:

- Security-first infrastructure
- Automation over manual operations
- Production-grade networking
- Infrastructure evolution planning
- Cost-aware architecture design

---

Each level directory contains its own detailed README explaining design decisions, implementation steps, and validation proof.

