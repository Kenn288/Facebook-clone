python manage.py startapp core ;;These are the accounts
python manage.py startapp posts
python manage.py startapp friends
python manage.py startapp messages 
python manage.py startapp notifications
python manage.py startapp comments




;;The folder structure of the project is as follows:
facebook_clone/
│
├── facebook_clone/                # Main project folder (settings, URLs, WSGI)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
│
├── accounts/also called core                      # User-related features (login, registration, profiles)
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/              # Templates for login, profile, etc.
│   ├── views.py
│   ├── models.py                  # UserProfile, FriendRequest models
│   ├── urls.py                    # URLs related to accounts
│   ├── forms.py                   # Forms for login, registration, etc.
│   └── ...
│
├── posts/                         # For handling posts and user feed
│   ├── migrations/
│   ├── templates/
│   │   └── posts/                 # Templates for viewing and creating posts
│   ├── views.py
│   ├── models.py                  # Post model
│   ├── urls.py                    # URLs related to posts
│   └── ...
│
├── comments/                      # For handling comments on posts
│   ├── migrations/
│   ├── templates/
│   │   └── comments/              # Templates for viewing and adding comments
│   ├── views.py
│   ├── models.py                  # Comment model
│   ├── urls.py                    # URLs related to comments
│   └── ...
│
├── friends/                       # Friend requests, friend list
│   ├── migrations/
│   ├── views.py
│   ├── models.py                  # Friend relationships
│   ├── urls.py                    # Friend-related URLs
│   └── ...
│
├── messages/                      # Messaging system
│   ├── migrations/
│   ├── templates/
│   │   └── messages/              # Templates for direct messaging
│   ├── views.py
│   ├── models.py                  # Message model
│   ├── urls.py                    # URLs for messaging
│   └── ...
│
├── notifications/                 # Notifications for friend requests, likes, etc.
│   ├── migrations/
│   ├── views.py
│   ├── models.py                  # Notification model
│   ├── urls.py                    # URLs for notifications
│   └── ...
│
├── static/                        # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                         # User-uploaded files (profile pictures, post images)
│
├── templates/                     # Global templates (base.html, layout)
│
├── manage.py                      # Django management commands
└── venv/                          # Virtual environment
