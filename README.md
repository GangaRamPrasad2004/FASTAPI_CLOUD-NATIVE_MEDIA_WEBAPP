# FastAPI Cloud-Native Media Webapp

A high-performance **Modular Monolithic** backend designed to handle media sharing at scale. This project demonstrates a decoupled architecture by offloading heavy media assets to a Cloud CDN while maintaining metadata integrity through an asynchronous relational data layer.

## 🚀 Key Features
- **Modular Monolith Architecture:** Ensures high-cohesion and low-coupling between business logic and data access.
- **Cloud-Native Media Handling:** Integrated with **ImageKit.io** for 0% local server storage footprint.
- **Asynchronous Data Layer:** Built with **FastAPI** and **SQLAlchemy** (Async) for high responsiveness under concurrent loads.
- **Modern Tooling:** Managed with **uv** for lightning-fast dependency resolution and deterministic builds.

## 🏗️ System Architecture
The project follows a decoupled design where the API acts as an orchestrator between the user, the database, and the cloud storage provider.



## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **Framework:** FastAPI
- **Database:** SQLite/PostgreSQL (via SQLAlchemy ORM)
- **Media Delivery:** ImageKit Cloud CDN
- **Package Manager:** uv

## 📥 Getting Started

### Prerequisites
- Install **uv**: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/GangaRamPrasad2004/FASTAPI_CLOUD-NATIVE_MEDIA_WEBAPP.git](https://github.com/GangaRamPrasad2004/FASTAPI_CLOUD-NATIVE_MEDIA_WEBAPP.git)
   cd FASTAPI_CLOUD-NATIVE_MEDIA_WEBAPP

   I have integrated the uv commands and the Environment Variables setup directly into the "Installation" section of your README.md.

This is a critical addition because it tells other developers (and recruiters) exactly how to recreate your environment. Using uv sync specifically marks you as a modern Python developer.

📄 Updated README.md (Installation Section)
Markdown

## 📥 Getting Started

### Prerequisites
- Install **uv**: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Installation & Setup
1. Sync Dependencies
  This project uses uv, a high-performance Python package manager. Running this command(uv init.) will automatically create a virtual environment and install all     required dependencies with pinpoint precision.
   (bash)uv sync
2. Environment Variables
  To ensure Security Awareness and proper Secrets Management, you must configure your cloud credentials locally. Create a .env file in the root directory to store    your ImageKit and Database settings:
      (File: .env)
     # ImageKit Cloud Credentials
     IMAGEKIT_PUBLIC_KEY=your_public_key
     IMAGEKIT_PRIVATE_KEY=your_private_key
     IMAGEKIT_URL_ENDPOINT=your_url_endpoint
     # Database Configuration
     DATABASE_URL=sqlite+aiosqlite:///./test.db
     Note: The .env file is excluded from version control via .gitignore to prevent sensitive credential leaks.
3. Run the Application
  Execute the following command to start the FastAPI development server. Using uv run ensures the app runs within the optimized project environment.
     (Bash)uv run uvicorn main:app --reload
