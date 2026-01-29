# hrms-fastapi
HRMS – FastAPI + React + PostgreSQL

A production-grade, multi-tenant HRMS (Human Resource Management System) built using FastAPI, React, and PostgreSQL, designed with clean architecture, domain-driven design, and scalability in mind.

This project is built as a modular monolith, following real-world enterprise patterns used in HRMS/HCM platforms.

🚀 Key Objectives

Build a realistic HRMS system, not a toy CRUD app

Demonstrate backend architecture & system design skills

Follow industry-standard patterns (Clean Architecture, RBAC, multi-tenancy)

Serve as a portfolio project for senior backend roles

🏗️ Architecture Overview
High-Level Design

Backend: FastAPI (async, modular monolith)

Frontend: React + TypeScript (planned)

Database: PostgreSQL

Cache / Queue: Redis (planned)

Auth: JWT + Role-Based Access Control

Multi-Tenancy: Shared DB + tenant_id isolation

The system starts as a modular monolith and is designed to be split into microservices if required.

🧱 Design Principles Used

Clean Architecture

Domain-Driven Design (DDD)

Service + Repository Pattern

Environment-based Configuration

12-Factor App Principles

📁 Project Structure
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
├── docker-compose.yml     # infra (planned)
├── .env.example
└── README.md

⚙️ Backend Tech Stack

Python 3.11+

FastAPI

Pydantic v2 + Pydantic Settings

Uvicorn

PostgreSQL (planned)

Redis (planned)

Alembic (planned)

Celery (planned)

🔐 Authentication & Security (Planned)

JWT-based authentication (access + refresh tokens)

Role-Based Access Control (RBAC)

Organization-level data isolation

Password hashing with bcrypt

Audit-friendly design

🧩 Core Modules (Planned)
Phase 1 – Foundation ✅

Application bootstrap

Environment configuration

Centralized logging

Health check endpoint

Phase 2 – Auth & Org Management

Organization onboarding

User & role management

JWT authentication

Phase 3 – Employee Management

Employee lifecycle

Department & designation

Reporting hierarchy

Phase 4 – Attendance & Leave

Punch-in / punch-out

Leave policies & workflows

Monthly summaries

Phase 5 – Payroll

Salary structure

Attendance-based payroll

Async payslip generation