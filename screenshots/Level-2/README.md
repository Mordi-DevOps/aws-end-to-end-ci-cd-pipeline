# Level 2 — Architecture & Deployment Validation Screenshots

This directory contains validation evidence for the Level-2 secure architecture upgrade.

The screenshots demonstrate private networking, secure deployment mechanisms, load balancing, and production-grade AWS infrastructure design.

---

## 📸 Screenshot Index

### 01 — WeatherApp Running
**File:** `01-Weatherapp-running.jpg`  
Proof that the application is successfully accessible via HTTPS through the Application Load Balancer.

---

### 02 — VPC Resource Map
**File:** `02-VPC-Resource-map.jpg`  
Shows the full VPC layout including public/private subnets, routing, and associated resources.

---

### 03 — NAT Instance
**File:** `03-NAT-Instance.jpg`  
Displays the NAT EC2 instance used to provide outbound internet access for private workloads.

---

### 04 — NAT Instance via SSM
**File:** `04-NAT-Instance-from-SSM-view.jpg`  
Confirms administrative access to the NAT instance using AWS Systems Manager (no SSH exposure).

---

### 05 — Private EC2 Workloads
**File:** `05-EC2-private-workloads.jpg`  
Shows all application infrastructure instances running without public IPs inside private subnets.

---

### 06 — ALB HTTPS Listener Rules
**File:** `06-HTTPS-443-Listener-rules.jpg`  
Displays host-based routing configuration for:

- jenkins.mordimaor.com  
- gitlab.mordimaor.com  
- app.mordimaor.com

---

### 07 — Target Groups Healthy
**File:** `07-Target-groups-healthy.jpg`  
Confirms all services are registered and passing ALB health checks.

---

### 08 — SSM Managed Instances
**File:** `08-SSM-managed-instances.jpg`  
Shows AWS Systems Manager managing all compute nodes for secure administration.

---

### 09 — SSM Deployment Command Success
**File:** `09-SSM-deploy-command-success.jpg`  
Proof of successful CI/CD deployment executed via SSM Run Command (no SSH).

---

### 10 — Jenkins Deploy Stage Success
**File:** `10-Jenkins-deploy-SSM-command-Success.jpg`  
Pipeline console output confirming successful SSM-based deployment execution.

---

### 11 — Security Group Restrictions
**File:** `11-SG-inbound-only-from-ALB.jpg`  
Demonstrates restricted inbound rules allowing traffic only from the Load Balancer.

---

### 12 — GitLab Host Routing
**File:** `12-gitlab-host-routing-https.jpg`  
Validates HTTPS access and host-based routing to the GitLab service via ALB.

---

### 13 — Jenkins Host Routing
**File:** `13-jenkins-host-routing-https.jpg`  
Validates HTTPS access and host-based routing to the Jenkins controller via ALB.

---

## 🔐 Security Validation Summary

These artifacts collectively prove:

- No public SSH exposure  
- No public EC2 workloads  
- Private subnet deployment  
- ALB as single public entrypoint  
- IAM + SSM administrative access  
- Secure CI/CD deployment flow  

---

This screenshot set serves as operational and architectural evidence for the Level-2 production upgrade.
