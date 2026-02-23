# Level 2 — Secure Private AWS Architecture Upgrade

This level upgrades the foundational CI/CD pipeline into a production-grade AWS architecture emphasizing security, private networking, and zero-trust deployment practices.

---

## 🎯 Architecture Objectives

- Remove public SSH exposure
- Eliminate Elastic IPs from workloads
- Run all services in private subnets
- Introduce ALB public entrypoint
- Deploy via AWS SSM instead of SSH

---

## 🌐 Network Design

- Custom VPC (10.0.0.0/16)
- Public & Private subnets
- Internet Gateway
- NAT Instance for outbound access
- Route table segmentation

---

## 🏗 Workload Placement

| Service | Subnet | Access |
|--------|---------|--------|
| Jenkins Controller | Private | ALB + SSM |
| GitLab | Private | ALB + SSM |
| Jenkins Agent | Private | WebSocket |
| WeatherApp | Private | ALB |

---

## 🌍 Load Balancer Routing

| Host | Target |
|------|--------|
| jenkins.mordimaor.com | Jenkins |
| gitlab.mordimaor.com | GitLab |
| app.mordimaor.com | WeatherApp |

---

## 🚀 Deployment Upgrade

### Before
SSH deployment from Jenkins.

### After
AWS SSM Run Command deployment:

- Docker pull
- Container replacement
- Image pruning

---

## 🔐 Security Enhancements

- No inbound SSH
- No public EC2
- IAM-scoped deployment
- ALB TLS termination
- Private compute layer

---

## 📊 Validation

- Webhook-triggered builds
- SSM command success
- Healthy ALB targets
- HTTPS application access

---

## 🧠 DevOps Skills Demonstrated

- VPC architecture design
- Private subnet deployment
- IAM least-privilege policy creation
- WebSocket Jenkins agents
- Host-based ALB routing
- Secure CI/CD delivery
