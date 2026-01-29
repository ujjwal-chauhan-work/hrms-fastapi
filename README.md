# HRMS FastAPI

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A production-grade, multi-tenant HRMS (Human Resource Management System) built using **FastAPI**, **React**, and **PostgreSQL**, designed with clean architecture, domain-driven design, and scalability in mind.

This project is built as a **modular monolith**, following real-world enterprise patterns used in HRMS/HCM platforms.

---

## 🚀 Key Objectives

- ✅ Build a **realistic HRMS system**, not a toy CRUD app
- 🏗️ Demonstrate **backend architecture & system design** skills
- 📐 Follow **industry-standard patterns** (Clean Architecture, RBAC, multi-tenancy)
- 💼 Serve as a **portfolio project** for senior backend roles

---

## 🏗️ Architecture Overview

### High-Level Design

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI (async, modular monolith) |
| **Frontend** | React + JavaScript |
| **Database** | PostgreSQL |
| **Cache / Queue** | Redis |
| **Authentication** | JWT + Role-Based Access Control |
| **Multi-Tenancy** | Shared DB + `tenant_id` isolation |

> **Note:** The system starts as a modular monolith and is designed to be split into microservices if required.

---

## 🧱 Design Principles

- **Clean Architecture** - Separation of concerns with clear boundaries
- **Domain-Driven Design (DDD)** - Business logic at the core
- **Service + Repository Pattern** - Abstraction for data access
- **Environment-based Configuration** - 12-Factor App compliant
- **Scalability First** - Ready for horizontal scaling

---

## 📁 Project Structure

```
hrms/
├── backend/
│   ├── app/
│   │   ├── core/          # config, logging, security
│   │   ├── auth/          # authentication & RBAC
│   │   ├── employees/     # employee domain
│   │   ├── attendance/    # attendance domain
│   │   ├── leave/         # leave domain
│   │   ├── db/            # database session & base
│   │   ├── api/           # versioned API routers
│   │   └── main.py        # application entrypoint
│   ├── tests/
│   └── requirements.txt
│
├── frontend/              # React app (planned)
├── docker-compose.yml     # infrastructure (planned)
├── .env.example
└── README.md
```

---

## ⚙️ Backend Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Core language |
| **FastAPI** | Web framework |
| **Pydantic v2** | Data validation |
| **Pydantic Settings** | Configuration management |
| **Uvicorn** | ASGI server |
| **PostgreSQL** | Primary database *(planned)* |
| **Redis** | Caching & queue *(planned)* |
| **Alembic** | Database migrations *(planned)* |
| **Celery** | Background tasks *(planned)* |

---

## 🔐 Authentication & Security *(Planned)*

- 🔑 **JWT-based authentication** (access + refresh tokens)
- 👥 **Role-Based Access Control (RBAC)**
- 🏢 **Organization-level data isolation**
- 🔒 **Password hashing** with bcrypt
- 📝 **Audit-friendly design**

---

## 🧩 Core Modules

### Phase 1 — Foundation ✅

- [x] Application bootstrap
- [x] Environment configuration
- [x] Centralized logging
- [x] Health check endpoint

### Phase 2 — Auth & Org Management

- [ ] Organization onboarding
- [ ] User & role management
- [ ] JWT authentication

### Phase 3 — Employee Management

- [ ] Employee lifecycle
- [ ] Department & designation
- [ ] Reporting hierarchy

### Phase 4 — Attendance & Leave

- [ ] Punch-in / punch-out
- [ ] Leave policies & workflows
- [ ] Monthly summaries

### Phase 5 — Payroll

- [ ] Salary structure
- [ ] Attendance-based payroll
- [ ] Async payslip generation

---

## 🚦 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 15+ *(for future phases)*
- Redis *(for future phases)*

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/hrms-fastapi.git
cd hrms-fastapi

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Copy environment variables
cp .env.example .env

# Run the application
cd backend
uvicorn app.main:app --reload
```

### Access the API

- **API Documentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health

---

## 🧪 Testing

```bash
# Run tests (coming soon)
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

---

## 🐳 Docker Support

```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🗺️ Roadmap

- [ ] Complete authentication module
- [ ] Implement employee management
- [ ] Add attendance tracking
- [ ] Build leave management system
- [ ] Develop payroll processing
- [ ] Create React frontend
- [ ] Add comprehensive test coverage
- [ ] Implement CI/CD pipeline
- [ ] Add API rate limiting
- [ ] Implement caching layer
- [ ] Add monitoring & observability

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- Clean Architecture principles by Robert C. Martin
- Domain-Driven Design by Eric Evans

---

## 📧 Contact

For questions or feedback, please reach out via [email@example.com](mailto:email@example.com)

---
