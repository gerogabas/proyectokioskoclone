# Proyecto:

socotroco

Este proyecto web esta siendo construido con:

- Front: React (en JavaScript) + React Router Dom + Tailwindcss
- Back: FastAPI (Python) + Uvicorn(server) + PostgreSQL

> [!NOTE]
> Para iniciar la web:
>
> - "npm install"
> - "npm run dev"
> - _*Abrir la url mostrada en consola*_
>
> Para iniciar uvicorn (la API):
>
> - "python -m venv env"
> - "source env\Scripts\activate" (en Windows)
> - "pip install -r requirements.txt"
> - "py -m uvicorn src.Back.api:app --reload"
> - *Ya deberia estar escuchando al puerto mostrado*

> [!TIP]
> Tip

> [!IMPORTANT]
> Importante

> [!WARNING]
> Warn

> [!CAUTION]
> Caution

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
