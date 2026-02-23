# Level 3 — On-Demand Infrastructure + Terraform Automation (Planned)

This future upgrade introduces dynamic infrastructure lifecycle management and Infrastructure as Code (IaC) automation.

The objective is to evolve the platform into a cost-optimized, event-driven, fully reproducible cloud environment.

---

## 🎯 Objectives

1. Allow all compute infrastructure to remain OFF by default
2. Automatically start infrastructure upon user demand
3. Reduce idle cloud costs
4. Provision infrastructure using Terraform
5. Enable environment recreation in minutes

---

## ⚡ On-Demand Infrastructure Design

When a user accesses:

app.mordimaor.com

the backend infrastructure automatically activates.

---

### Proposed Activation Flow

1. User sends HTTP request to ALB / entry endpoint
2. Detection layer (Lambda / API Gateway / health monitor) evaluates backend state
3. If instances are stopped:
   - Trigger Auto Scaling Group scale-up
   - Or start EC2 instances directly
4. Wait for ALB target health checks to pass
5. Route traffic to the application

---

## 🏗 Implementation Options

### Option A — Auto Scaling Group + Lambda Waker

- WeatherApp in Auto Scaling Group
- Desired capacity = 0 by default
- Lambda function increases capacity on demand
- Health check polling before routing

### Option B — EventBridge Scheduler

- Scheduled stop/start windows
- Business-hours compute model

### Option C — Serverless Migration

Future migration to:

- AWS App Runner
- ECS Fargate
- Lambda + API Gateway

---

## 💰 Cost Optimization Benefits

- Zero idle EC2 cost
- Pay-per-use compute
- Reduced NAT / data transfer costs
- Elastic runtime scaling

---

# 🌍 Terraform Infrastructure as Code Plan

Level 3 will introduce full Terraform provisioning for all AWS resources.

---

## 📦 Terraform Scope

Infrastructure modules will include:

### Networking
- VPC
- Public / Private subnets
- Route tables
- Internet Gateway
- NAT Gateway / NAT Instance

### Compute
- Jenkins Controller EC2
- GitLab EC2
- Jenkins Agents
- WeatherApp instances / ASG

### Load Balancing
- Application Load Balancer
- Target Groups
- Listener rules

### Security
- Security Groups
- IAM Roles
- IAM Policies
- Instance profiles

### DNS
- Route53 hosted zone
- Domain records

---

## 🧱 Terraform Module Structure (Planned)

iac/
├── modules/
│ ├── vpc/
│ ├── alb/
│ ├── ec2/
│ ├── security-groups/
│ └── iam/
│
├── environments/
│ ├── dev/
│ └── prod/
│
├── backend.tf
├── providers.tf
└── main.tf


---

## 🔐 Terraform State Management

Planned remote backend:

- S3 state storage
- DynamoDB state locking

Benefits:

- Team-safe deployments
- Drift detection
- Versioned infra state

---

## 🚀 Future CI/CD for Terraform

Infrastructure provisioning will integrate into Jenkins pipeline:

Flow:

1. Terraform validate
2. Terraform plan
3. Manual approval gate
4. Terraform apply
5. Post-deploy verification

---

## 🧠 DevOps Skills Demonstrated

Level 3 will showcase:

- Infrastructure lifecycle automation
- Scale-to-zero architecture
- Event-driven compute activation
- Terraform IaC design
- Remote state management
- Modular infrastructure coding
- Cost optimization engineering

---

## 📊 Planned Validation Artifacts

Future screenshots & proofs:

- Auto Scaling desired capacity change
- Lambda execution logs
- Terraform plan/apply output
- Remote state bucket
- DynamoDB lock table
- Recreated environment proof

---

Implementation diagrams and automation scripts will be added in future updates.

