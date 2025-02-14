FinChrono/
├── backend/                  # Backend folder (Flask, Celery)
│   ├── app/                  # Flask app folder
│   │   ├── __init__.py       # Initialize Flask app
│   │   ├── routes.py         # API routes (e.g., for fetching stock data, handling user requests)
│   │   ├── models.py         # Database models (SQLAlchemy models)
│   │   ├── tasks.py          # Celery tasks (for background jobs like notifications)
│   │   ├── config.py         # Configuration file (Flask settings, Celery, DB setup)
│   │   └── utils.py          # Utility functions (e.g., for pulling data from FactSet)
│   ├── migrations/           # Database migrations (if using Flask-Migrate)
│   ├── .env                  # Environment variables (e.g., DB creds, FactSet API key)
│   ├── requirements.txt      # Python dependencies (Flask, Celery, etc.)
│   ├── Dockerfile            # Dockerfile for containerizing backend app
│   └── run.py                # Script to run the Flask app
├── frontend/                 # Frontend folder (React, D3.js, Push Notifications)
│   ├── public/               # Public assets (HTML, images, etc.)
│   ├── src/                  # React app source files
│   │   ├── components/       # React components (e.g., stock charts, notifications)
│   │   ├── App.js            # Main React app file
│   │   ├── index.js          # Entry point to the React app
│   │   ├── stockData.js      # API calls to interact with the backend for stock data
│   │   ├── notifications.js  # Push notification handling
│   │   ├── dashboard.js      # User dashboard (stock portfolio, reminders)
│   │   ├── chart.js          # D3.js/Chart.js visualizations for stock data
│   │   └── styles.css        # Styles for the frontend (CSS)
│   ├── package.json          # Node dependencies (React, Chart.js, Push notifications, etc.)
│   └── webpack.config.js     # Webpack config for bundling the React app
├── .gitignore                # Git ignore file
└── README.md                 # Project overview and instructions
