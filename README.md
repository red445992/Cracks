# Django Social Media App

This project is a simple social media platform built using Django. It allows users to sign up, log in, upload posts, follow other users, like posts, and more. The app is a great example of a full-stack Django application with user authentication and interactive features.

## Features

- **User Signup:** New users can sign up for the platform.
- **User Login/Logout:** Users can log in and log out of their accounts.
- **Profile Setup:** Each user has a personalized profile.
- **Post Upload:** Users can upload posts with text and images.
- **Post Feed:** A feed displaying posts from users.
- **Like Posts:** Users can like posts in the feed.
- **Profile Page:** Users have their own profile pages displaying their posts and information.
- **Follow/Unfollow:** Users can follow and unfollow other users.
- **Search Users:** Users can search for others by username.
- **User Suggestions:** The app suggests users to follow based on their activity.

## Project Structure

```plaintext
social_book/
├── manage.py
├── main/          # Main app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── db.sqlite3
├── requirements.txt       # Project dependencies
└── README.md              # Project description
```

## Setup Instructions

Follow these steps to get the project up and running locally:

### 1. Clone the Repository

Start by cloning the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/social-media-app.git
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
* And activate the env
```bash
.\venv\Scripts\activate

```

### 3. install dependencies
```bash
pip install -r requirements.txt
```
### 4. apply database migrations
```bash
 python manage.py migrate
```
###5.Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
###6. run the development server
```bash
python manage.py runserver
```