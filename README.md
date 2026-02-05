# Django Blog API

A REST API built using Django REST Framework that provides authentication, role-based access control, and blog features such as posts, likes, comments, search, and pagination.

This project is intended to demonstrate real-world backend development practices and is fully testable using Postman.

---

## Features

### Authentication and Security
- JWT-based authentication (login, logout, refresh)
- Custom login response including user details
- Token-based forgot password flow
- Role-based access control (user, manager)
- Admin-only user promotion

### User Roles

**User**
- Register and log in
- Create, update, and delete own blog posts
- Like and unlike posts
- Add comments to posts
- View and search all posts

**Manager**
- All user permissions
- Update or delete any blog post
- Delete any comment

**Admin (Superuser)**
- Promote users to manager
- Full access through Django admin

---

## Blog Functionality
- Create, read, update, and delete posts
- Like and unlike posts
- Comment system
- Author-based permissions
- Global post visibility
- Search by title, content, or author
- Pagination and ordering

---

## Tech Stack
- Backend: Django, Django REST Framework
- Authentication: JWT (SimpleJWT)
- Database: SQLite (development)
- API Testing: Postman

---

## Project Structure









---

## Authentication Flow


All protected endpoints require the following header:


---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|------|---------|-------------|
| POST | /api/auth/register/ | Register new user |
| POST | /api/auth/login/ | Login and get JWT |
| POST | /api/auth/logout/ | Logout |
| POST | /api/auth/refresh/ | Refresh access token |
| POST | /api/auth/forgot-password/ | Send password reset link |
| POST | /api/auth/reset-password/ | Reset password |

### Admin
| Method | Endpoint | Description |
|------|---------|-------------|
| POST | /api/auth/admin/promote-user/ | Promote user to manager |

### Blog Posts
| Method | Endpoint | Description |
|------|---------|-------------|
| GET | /api/posts/ | List posts (search, pagination) |
| POST | /api/posts/ | Create post |
| GET | /api/posts/{id}/ | Get post |
| PUT | /api/posts/{id}/ | Update post |
| DELETE | /api/posts/{id}/ | Delete post |
| POST | /api/posts/{id}/like/ | Like or unlike post |

### Comments
| Method | Endpoint | Description |
|------|---------|-------------|
| GET | /api/posts/{id}/comments/ | List comments |
| POST | /api/posts/{id}/comments/ | Add comment |
| PUT | /api/comments/{id}/ | Update comment |
| DELETE | /api/comments/{id}/ | Delete comment |

---

## Search and Pagination


---

## Running the Project Locally

```bash
git clone https://github.com/samp6654/django-blog-api.git
cd django-blog-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
