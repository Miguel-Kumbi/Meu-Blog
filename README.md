# Blog (Django)

A simple blog application built with **Django and Python**, developed as a practical project to consolidate web development, database modeling, authentication, authorization, and Django best practices.

The project focuses on building a realistic but intentionally simple blogging platform rather than an over-engineered content management system.

---

## Project Overview

This project is a full-stack web application built with Django.

Users can create accounts, authenticate, create blog posts, save them as drafts, edit their own posts, publish them, and delete them. Published posts are displayed on the public homepage, while unpublished posts remain accessible through the user's draft area.

The project was developed incrementally, with emphasis on:

- Clean Django architecture
- Separation of responsibilities
- Secure authentication and authorization
- Reusable templates
- Form validation
- Database relationships
- User ownership
- Practical Django conventions

---

## Features

### User Management

- User registration
- User login
- User logout
- Authentication-protected actions
- User-specific draft area

### Blog Posts

- Create posts
- Edit posts
- Delete posts
- Publish drafts
- View individual posts
- Display published posts on the homepage
- Display unpublished posts as drafts
- Associate posts with categories
- Associate posts with multiple tags
- Display author information
- Display creation and publication dates

### Authorization

Users can only modify their own posts.

Protected operations include:

- Editing posts
- Deleting posts
- Publishing posts

Unauthorized actions result in a proper **HTTP 403 Forbidden** response.

### Error Handling

Custom error pages are implemented for:

- `403 Forbidden`
- `404 Not Found`

The application uses Django's error-handling mechanisms to return the correct HTTP status codes.

---

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web framework |
| SQLite | Development database |
| HTML5 | Page structure |
| Bootstrap 5 | UI and responsive styling |
| Git | Version control |

---

## Project Structure

The main project structure is organized as follows:

```text
blog/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── includes/
│   │       ├── drafts.html
│   │       ├── home.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_confirm_publish.html
│   │       ├── post_create.html
│   │       ├── post_detail.html
│   │       ├── post_update.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── 403.html
│   └── 404.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Data Model

The application contains three main blog entities:

### Category

Categories organize posts into broader topics.

```text
Category
   │
   └───< Post
```

Each category can contain multiple posts.

### Tag

Tags provide a more flexible way of classifying posts.

```text
Post >────< Tag
```

The relationship is many-to-many, allowing:

- one post to have multiple tags;
- one tag to belong to multiple posts.

### Post

A post contains:

- Title
- Slug
- Content
- Author
- Category
- Tags
- Creation date
- Update date
- Publication date

The `published_at` field determines whether a post is published or remains a draft.

```text
published_at = NULL
        ↓
     Draft

published_at != NULL
        ↓
    Published
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal.

### 6. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

## Authentication & Authorization

The application distinguishes between authentication and authorization.

### Authentication

Unauthenticated users can:

- Browse published posts
- View post details
- Register
- Log in

Authenticated users can additionally:

- Create posts
- Manage their drafts
- Edit their own posts
- Publish their own posts
- Delete their own posts


---

## AI Use

AI assistance was used to:

- Define the project's development roadmap
- Discuss application structure
- Identify incorrect implementations
- Generation of HTML structures (Creating page skeletons)
- Creating Bootstrap components (Generate the exact code for Bootstrap components)
- Suggest improvements
- Technical explanations
- This README


---

## Future Improvements

Possible future improvements include:

- PostgreSQL support
- Pagination
- Post search
- Category and tag filtering
- Comments
- Likes and Deslikes
- User profile pages
- Password reset
- Image uploads
- REST API with Django REST Framework


These features are intentionally outside the current scope of the project.

