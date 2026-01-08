import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app.app:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        # Add these lines to ignore the database and virtual environment
        reload_excludes=["*.db", ".venv/*", "**/__pycache__/*"]
    )