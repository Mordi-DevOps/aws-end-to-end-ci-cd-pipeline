# AWS End-to-End CI/CD Pipeline — DevOps Portfolio Project

This repository demonstrates the evolution of a production-grade CI/CD platform on AWS, progressing from a basic container deployment pipeline to a secure private architecture and finally to an on-demand, cost-optimized infrastructure model **provisioned via Terraform (IaC)**.

> Note: CI/CD pipelines are configured to run on GitLab. This GitHub repository is for portfolio demonstration and documentation purposes.

---

## 📁 Repository Architecture Levels

| Level | Directory | Focus |
|------|-----------|-------|
| Level 1 | Level-1 | Foundational CI/CD pipeline (Jenkins + Docker + EC2) |
| Level 2 | Level-2 | Secure private AWS architecture (ALB + Private Subnets + SSM deploy + No SSH/EIPs) |
| Level 3 | Level-3 | **On-demand infrastructure + Terraform IaC (planned)** |

---

## 🧭 Architecture Evolution

### Level 1 — Functional Pipeline
- Jenkins builds, tests, and containerizes the application
- Image is pushed to Docker Hub
- App is deployed to EC2 (baseline automation)

### Level 2 — Production Security Upgrade
- All workloads moved to **private subnets**
- **ALB** is the single public entrypoint (HTTPS)
- Host-based routing:
  - `jenkins.mordimaor.com` → Jenkins
  - `gitlab.mordimaor.com` → GitLab
  - `app.mordimaor.com` → WeatherApp
- **SSM deploy** replaces SSH (no public SSH access)
- Jenkins agent connects via **WebSocket** (no SSH agents)

### Level 3 — On-Demand + Terraform (Planned)
- Goal: allow compute to be **OFF by default** and activate on user demand (scale-to-zero style)
- Implementation direction (planned):
  - Auto Scaling Group (min=0) + Lambda “waker” OR serverless migration
- **Terraform IaC**:
  - Provision VPC, subnets, ALB, security groups, IAM roles/policies, EC2/ASG
  - Remote state (S3 + DynamoDB locking)
  - Optional: Terraform stages integrated into Jenkins pipeline (plan/apply with approval)

---

## 🔧 Core Technologies

- Jenkins
- Docker
- AWS (EC2, VPC, ALB, SSM, IAM, Route 53)
- GitLab
- Docker Hub
- Slack
- Flask

---

## 📊 DevOps Capabilities Demonstrated

- CI/CD pipeline automation (build → test → package → deploy)
- Containerization and registry publishing
- Secure VPC networking (public/private segmentation, controlled egress)
- IAM least-privilege deployment model
- Webhook-driven builds (push triggers pipeline)
- SSM-based operations (no SSH)
- Architecture evolution + roadmap planning (Terraform + on-demand infra)

---

## 📐 Architecture Diagrams & Proof

- Diagrams: `architecture/`
- Validation screenshots: `screenshots/`

Each level directory includes its own README with detailed implementation notes and validation artifacts.

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

