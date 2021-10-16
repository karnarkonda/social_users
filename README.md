# Social_Friends
A basic Django API App

## Project Setup ##

1. Install a local Postgresql database service.
2. Create a `socials` database with a `postgres` user and password `postgres`.
3. Install the project dependencies with `pip install -r requirements.txt` command.
4. Create the database migrations by running `python manage.py makemigrations`.
5. Create the table schema using `python manage.py migrate`.
6. Seed database with dummy data `python manage.py loaddata Users.json` & `python manage.py loaddata Users_friends.json`.
7. Start the development server. `python manage.py runserver`.

## API Docs ##

1. List All Users API - `GET <localhost>/socials/users`

2. List users that are friends with a specific user API - `GET <localhost>/socials/user/friends`
    Request params: `user_id`=`integer`
    
3. List users that are not friends of a specific user API - `GET <localhost>/socials/user/not_friends`
    Request params: `user_id`=`integer`
    
4. List common friends between 2 users API - `GET <localhost>/socials/user/common_friends`
    Request params: `user1`=`integer`, `user2`=`integer`
    
5. List potential friends of a user API - `GET <localhost>/socials/user/potential_friends`
    Request params: `user_id`=`integer`
    
6. Add friendships to a user API - `GET <localhost>/socials/user/add_friends`
    Request params: `user_id`=`integer`, `friends`=[{"first_name": 'string', "last_name": 'string'}, .... n]

