# Color Swatches Generator

A full-stack application for generating and displaying color swatches in various color spaces.

## Prerequisites
- Python 3.12.6
- Node.js 20.17.0
- pipenv
- npm

## Project Structure
```
kanopi/
├── backend/
│   ├── color_project/        # Django project settings
│   ├── colors/              # Main Django app
│   │   ├── core/            # Base classes
│   │   ├── implementations/ # Color spaces
│   │   ├── services/        # Business logic
│   │   ├── api/            # API endpoints
│   │   └── tests/          # Unit tests
│   ├── Pipfile
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API client
│   │   └── App.jsx
│   └── package.json
└── run.sh
```

## Setup & Installation

### Backend
```bash
cd backend
pipenv install
pipenv install django djangorestframework django-cors-headers
```

### Frontend
```bash
cd frontend
npm install @mui/material @emotion/react @emotion/styled @mui/icons-material
```

## Running the Application

1. Make script executable:
```bash
chmod +x run.sh or chmod 755 run.sh
```

2. Start servers:
```bash
./run.sh
```

Access:
- Frontend: http://localhost:3000
- API: http://localhost:8000/api/swatches/

## API Endpoints

`GET /api/swatches/`
- Query params: `count` (default: 5)
- Returns array of color objects in different spaces (RGB, HSL)
