# Piedpiper

A Django-based web applicaton to chat with your friends as well as the people around the globe in realtime. This is an application designed with the user in mind.
A user can create custom channels and invite other members.
The application supports communicating through text, images or gifs. 

Demo : [Piedpiper](https://youtu.be/km2-S0rkKRA)

## Tech Stack
- **Django**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Redis**
- **Web Sockets**

## Piedpiper Benefits
- Realtime instant Communication
- Privacy focused
- Streamlined workflow
- No third party authentication
- Custom room name available

## Installation Guide
1. Clone the repository to a suitable location on your local machine, and cd into it
```
  git clone https://github.com/JackCompass/piedpiper
  cd piedpiper
```
  
2. Download the dependencies of the project by running this command in the shell
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
4. You have installed all the packages successfully. Now it's time to spin the app server
```
  python3 manage.py runserver
```
5. Navigate to your [localhost](http://localhost:8000/)
