# Bug Tracker Project

A simple Bug Tracking web application with backend REST API and a basic frontend to view and add bugs.

---

## Features

- Add new bugs with details like title, description, severity, and status.
- View all existing bugs in a list.
- Update bug status to "resolved".
- Delete bugs when fixed permanently.
- Bugs data stored in a JSON file (`bugs.json`) for persistence.
- Simple frontend interface to interact with bugs visually.
- Backend built with Python Flask.
- Frontend uses HTML, CSS, and JavaScript (fetch API).

---

## Technologies Used

- Python 3.x
- Flask
- HTML / CSS / JavaScript
- JSON for data storage

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <your_repo_url>
   cd bug-tracker

---

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

---
3. **Install Dependencies:**
    ```bash
    pip install Flask
---
4. **Run the flask app:**
    ```bash
    python app.py
---
5. **Open your browser and go to:**
    ```bash
    http://localhost:5000/
---

## API Endpoints

| Method | Endpoint       | Description                      | Request Body Example                                                                 | Notes                                         |
|--------|----------------|----------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------|
| GET    | `/bugs`        | Get all bugs                     | None                                                                                 | View all bugs                                 |
| POST   | `/bugs`        | Add a new bug                    | `{ "title": "Bug title", "description": "Details", "severity": "low" }`             | Add bug via frontend or API                   |
| PUT    | `/bugs/<id>`   | Update bug status to resolved    | `{ "status": "resolved" }`                                                           | Use Postman or REST client to update status   |
| DELETE | `/bugs/<id>`   | Delete a bug                     | None                                                                                 | Use Postman to delete bug                     |


 ---

## Using Postman to Update or Delete Bugs
1. Update Bug Status (Mark as Resolved):
- Method: PUT
- URL: http://localhost:5000/bugs/<bug_id> (replace <bug_id> with actual bug ID)
- Body (raw JSON):
  ```json
  {
    "status": "resolved"
  }
- Send the request. If successful, the bug status updates to "resolved".
  
---

## Delete Bug 
- Method: DELETE
- URL: http://localhost:5000/bugs/<bug_id>
- No body required.
- Send the request. The bug will be removed permanently from bugs.json.

---

## Usage
- Use the frontend page to view bugs and add new bugs.
- Use Postman or any REST client to update bug status or delete bugs.
- The bugs list updates live when you add or update bugs.

---

## Notes
- This project is a learning/demo tool to understand backend CRUD operations and frontend integration.
- Bugs are stored in a local JSON file (bugs.json), not in a real database.
- Feel free to extend this project with database integration, authentication, and richer UI.
---

## Author
Prathibha 



##
