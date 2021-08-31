# Piedpiper

A Django-based web applicaton to chat with your friends as well as the people around the globe. This is an application designed with the user in mind.
A user has power to create custom channels and invite other members.
The application is designed in such a way that users can express what they want to express either by text or images or gifs etc. 

## Tech Stack
- **Django**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Redis**
- **Web Sockets**

Demo : [Piedpiper](https://youtu.be/km2-S0rkKRA)

## Piedpiper Benefits
- Improved Communication
- Streamlined workflow
- Increased Accountability
- saves time
- No third party authentication
- Custom room name available

## Installatiion Guide

A very simple and minimilist procedure to install and use the application

1. Clone the repository to a suitable location in your local machine
```
  git clone https://github.com/JackCompass/piedpiper
```
  
2. Download the dependency of the project by running the command in the shell
```
  pip3 install -r requirements.txt
```
3. Create all the migration by the help of this command 
```
  python3 manage.py makemigrations
  python3 manage.py migrate
```
3. To create a superuser account run this command in the shell (Not mandatory)
```
  python3 manage.py createsuperuser
```
4. You have instlled all the packages successfully. Now it's time spin the app
```
  python3 manage.py runserver
```
5. Navigate to your [localhost](http://localhost:8000/)
