# Social Media API - Posts and Comments
## 1. Post Endpoints
### GET /api/posts/
- Retrieves all posts (Paginated)
- Example Response:
  {
    "count": 100,
    "next": "http://127.0.0.1:8000/api/posts/?page=2",
    "results": [
      {
        "id": 1,
        "title": "My First Post",
        "content": "Hello world!",
        "author": "user123",
        "created_at": "2025-03-26T12:00:00Z"
      }
    ]
  }
