# Simple Social

A full-stack, lightweight social media application built with FastAPI and Streamlit. Users can sign up, log in, share images or videos with captions, view a unified feed, and delete their own posts. Media management and real-time transformations are handled gracefully via ImageKit.

## Authentication

Authentication is robustly handled using the **[FastAPI Users](https://fastapi-users.github.io/fastapi-users/)** library, providing a secure and extensible auth system out-of-the-box.

- **Method**: **JWT (JSON Web Tokens)** via **Bearer Transport**.
- **Strategy**: Tokens are configured with a 3600-second (1-hour) expiration lifetime.
- **Password Hashing**: Secure password hashing is enforced under the hood (using bcrypt/argon2).
- **Storage**: User credentials and UUID-based profiles are stored asynchronously in an SQLite database using `SQLAlchemyUserDatabase`.
- **Endpoints**: Fully integrated endpoints for login (`/auth/jwt/login`), registration (`/auth/register`), and user profile management (`/users/me`).

## Key Packages Used

### Backend
- **`fastapi`**: A modern, high-performance web framework for building the API endpoints.
- **`fastapi-users[sqlalchemy]`**: Manages the complete user lifecycle and JWT authentication flows.
- **`sqlalchemy` & `aiosqlite`**: Provides asynchronous Object-Relational Mapping (ORM) and asynchronous SQLite database interaction for responsive queries.
- **`imagekitio`**: Interacts with the ImageKit API for uploading media and generating URL-based transformations (e.g., dynamic text overlays, blurring, and resizing).
- **`pydantic`**: Enforces strict data validation and serialization for API requests and responses.

### Frontend
- **`streamlit`**: Powers the interactive web interface, allowing for a sleek, pure Python frontend implementation.
- **`requests`**: Handles RESTful HTTP API calls from the Streamlit frontend to the FastAPI backend, including securely passing the Bearer tokens.

### Tooling
- **`uv`**: Used for extremely fast Python package installation, dependency resolution, and environment management (as defined by `uv.lock`).

## Features

- **User Management**: Secure sign up, log in, and session tracking.
- **Media Uploads**: Support for images (`png`, `jpg`, `jpeg`) and videos (`mp4`, `avi`, `mov`, `mkv`, `webm`).
- **Smart Media Display**: Uniform media rendering using ImageKit transformations (e.g., maintaining aspect ratio with padded resize and blurred backgrounds for videos).
- **Caption Overlays**: Text captions are encoded and overlaid directly onto the images/videos dynamically.
- **Feed**: A chronological feed displaying posts from all users.
- **Access Control**: Users are authorized to delete only their own posts.

## Setup & Running

1. **Install Dependencies**:
   Assuming you have `uv` installed, sync your environment:
   ```bash
   uv sync
   ```
   *(Alternatively, use standard pip if preferred)*

2. **Configure Environment**:
   Ensure your `ImageKit` credentials and environment variables are set up appropriately (required by `app/image.py`).

3. **Start the Backend**:
   Run the FastAPI server on port 8000:
   ```bash
   fastapi dev app/app.py
   # OR: uvicorn app.app:app --reload
   ```

4. **Start the Frontend**:
   In a new terminal window, launch the Streamlit app:
   ```bash
   streamlit run app/frontend.py
   ```