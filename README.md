```markdown
# DanVerse API

DanVerse API is a Django RESTful API I designed to manage blog posts, comments, user profiles, tags, likes, and loves. It serves as the backend for your blogging platform.

## Features

- **Blog Posts:** Create, read, update, and delete blog posts.
- **Comments:** Allow users to comment on blog posts.
- **User Profiles:** Manage user profiles with additional information.
- **Tags:** Categorize blog posts using tags.
- **Likes and Loves:** Add likes and loves to blog posts.

<img width="1437" alt="restful" src="https://github.com/bongomin/DanVerse-API/assets/39218838/35039138-3cfb-42f5-9c41-62e2f7fd47ec">

## API Endpoints

The API provides the following endpoints:

- **Blog Posts:**
  - `GET /api/v1/blogs/`: Get a list of all blog posts.
  - `GET /api/v1/blogs/{blog_id}/`: Get details of a specific blog post.
  - `POST /api/v1/blogs/`: Create a new blog post.
  - `PUT /api/v1/blogs/{blog_id}/`: Update an existing blog post.
  - `DELETE /api/v1/blogs/{blog_id}/`: Delete a blog post.

- **Comments:**
  - `GET /api/v1/comments/`: Get a list of all comments.
  - `GET /api/v1/comments/{comment_id}/`: Get details of a specific comment.
  - `POST /api/v1/comments/`: Add a new comment.
  - `PUT /api/v1/comments/{comment_id}/`: Update an existing comment.
  - `DELETE /api/v1/comments/{comment_id}/`: Delete a comment.

- **User Profiles:**
  - `GET /api/v1/users/`: Get a list of all user profiles.
  - `GET /api/v1/users/{user_id}/`: Get details of a specific user profile.
  - `POST /api/v1/users/`: Create a new user profile.
  - `PUT /api/v1/users/{user_id}/`: Update an existing user profile.
  - `DELETE /api/v1/users/{user_id}/`: Delete a user profile.

- **Tags:**
  - `GET /api/v1/tags/`: Get a list of all tags.
  - `GET /api/v1/tags/{tag_id}/`: Get details of a specific tag.
  - `POST /api/v1/tags/`: Create a new tag.
  - `PUT /api/v1/tags/{tag_id}/`: Update an existing tag.
  - `DELETE /api/v1/tags/{tag_id}/`: Delete a tag.

- **Likes and Loves:**
  - `POST /api/v1/posts/{post_id}/like/`: Add a like to a blog post.
  - `POST /api/v1/posts/{post_id}/love/`: Add a love to a blog post.
  - `DELETE /api/v1/posts/{post_id}/like/`: Remove a like from a blog post.
  - `DELETE /api/v1/posts/{post_id}/love/`: Remove a love from a blog post.

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:bongomin/DanVerse-API.git
   cd danverse-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:

   Create a `.env` file in the project root and add the necessary environment variables.

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Deployment

The API is deployed on [Railway](https://danverse-api-production.up.railway.app/). Ensure your production environment variables are correctly configured.

## Contributing

If you would like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

```
