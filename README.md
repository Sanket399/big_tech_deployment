# Big Tech Deployment

A minimal web application deployed through a fully automated CI/CD pipeline.  

The focus is on **automation, versioned Docker builds, and deployment workflows**, with built-in rollback in case of failed health checks.  

---

## Features

- Automatic Docker image build, tagging, and push to Docker Hub.
- Deployments via SSH to a VM.
- Health check validation with automatic rollback.
- Git tagging integrated with releases.
- Multi-tag Docker strategy: `build-<run_number>`, `1.0.<run_number>`, `latest`.

---

## Structure
    ├── app.py # Minimal static app
    ├── Dockerfile # Container configuration
    ├── requirements.txt # Dependencies
    ├── .github/workflows # CI/CD pipeline workflow
    └── LICENSE
---

## Next Steps

- Separate staging and production environments.
- Kubernetes-based deployment.
- Advanced CI/CD patterns: blue-green, canary, automated monitoring.

