# API Documentation

This document describes the REST API endpoints available in the Django Blog project.

## Authentication

The API uses token-based authentication. To authenticate your requests, include the token in the Authorization header:

```
Authorization: Token your-token-here
```

To obtain a token, send a POST request to `/api/token/` with your credentials:

```json
{
    "username": "your-username",
    "password": "your-password"
}
```

## Endpoints

### Users

#### List Users
- **URL**: `/api/users/`
- **Method**: GET
- **Auth Required**: No
- **Response**:
```json
{
    "count": 10,
    "next": "http://example.com/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "profile": {
                "bio": "User bio",
                "avatar": "http://example.com/avatars/user1.jpg"
            }
        }
    ]
}
```

#### User Detail
- **URL**: `/api/users/{id}/`
- **Method**: GET
- **Auth Required**: No
- **Response**: Single user object

### Posts

#### List Posts
- **URL**: `/api/posts/`
- **Method**: GET
- **Auth Required**: No
- **Query Parameters**:
  - `category`: Filter by category ID
  - `tag`: Filter by tag ID
  - `author`: Filter by author ID
  - `status`: Filter by status (published/draft)
- **Response**:
```json
{
    "count": 20,
    "next": "http://example.com/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Post Title",
            "content": "Post content...",
            "author": {
                "id": 1,
                "username": "author1"
            },
            "created_at": "2024-03-20T10:00:00Z",
            "status": "published"
        }
    ]
}
```

#### Create Post
- **URL**: `/api/posts/`
- **Method**: POST
- **Auth Required**: Yes
- **Request Body**:
```json
{
    "title": "New Post",
    "content": "Post content...",
    "status": "draft",
    "category": 1,
    "tags": [1, 2]
}
```

#### Post Detail
- **URL**: `/api/posts/{id}/`
- **Method**: GET
- **Auth Required**: No
- **Response**: Single post object with full details

### Comments

#### List Comments
- **URL**: `/api/posts/{post_id}/comments/`
- **Method**: GET
- **Auth Required**: No
- **Response**:
```json
{
    "count": 5,
    "results": [
        {
            "id": 1,
            "content": "Comment text",
            "author": {
                "id": 1,
                "username": "commenter1"
            },
            "created_at": "2024-03-20T11:00:00Z"
        }
    ]
}
```

#### Create Comment
- **URL**: `/api/posts/{post_id}/comments/`
- **Method**: POST
- **Auth Required**: Yes
- **Request Body**:
```json
{
    "content": "New comment"
}
```

## Error Responses

The API uses standard HTTP status codes and returns error messages in the following format:

```json
{
    "error": "Error message",
    "detail": "Detailed error description"
}
```

Common status codes:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Rate Limiting

API requests are limited to:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

## Versioning

The API is versioned through the URL path. The current version is v1:
```
/api/v1/endpoint/
```

## Pagination

List endpoints support pagination with the following parameters:
- `page`: Page number
- `page_size`: Number of items per page (default: 10, max: 100)

## Filtering

List endpoints support filtering using query parameters. For example:
```
/api/posts/?category=1&status=published
```

## Sorting

List endpoints support sorting using the `ordering` parameter:
```
/api/posts/?ordering=-created_at  # Sort by creation date descending
``` 