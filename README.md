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
