# Google Calendar Integration with Django Rest API

- In this project, Google Calendar Integration was implemented using Django Rest API.<br/>
- OAuth2 mechanism was used to get users' calendar access.

## Getting Started

This project implements Google Calendar integration using Django Rest API. The OAuth2 mechanism is used to obtain users' calendar access. To get started, follow the steps below:

1. Clone the repository :-

   ```bash
   git clone https://github.com/your-username/project-name.git
   
2. Install virtual environment  :-

   ```bash
   python -m venv "evironment name"
   
2. Install the project dependencies :-

   ```bash
   pip install -r requirements.txt

3. Set up the project configuration :-

   - Configure the Django settings file (settings.py) with your database and other necessary        settings.<br/>
   - Add your Google API credentials and other configuration details in the project's settings.
  
4. Run database migrations :-

   ```bash
   python manage.py migrate

5. Start the development server :-

   ```bash
   python manage.py runserver

6. Access the API endpoints in your browser or through API clients like Postman.
  
## API Endpoints

This project exposes the following API endpoints :-

### 1. `/rest/v1/calendar/init/` - `GoogleCalendarInitView()`

This endpoint initiates the first step of the OAuth process. When accessed, it prompts the user for their credentials to authenticate and authorize access to their Google Calendar.

### 2. `/rest/v1/calendar/redirect/` - `GoogleCalendarRedirectView()`

This endpoint handles the redirect request sent by Google after the user has granted access to their calendar. It performs the following tasks:

- Handles the redirect request and receives the authorization code.
- Retrieves the access token using the authorization code.
- Retrieves a list of events from the user's calendar using the access token.

Please refer to the source code or API documentation for further details on the request methods, input parameters, and response formats for each endpoint.

## Dependencies

This project relies on the following dependencies:

- Django: version 4.2.1
- Django Rest Framework: version 3.9.3
- Google API Python Client: version 2.0

### Note:
To ensure the proper functioning of this assignment, it is necessary to possess valid Google account credentials stored in the project directory and to have a redirect URL added to your Google Cloud setup. Please refer to the documents and references section for further guidance on these requirements.

## Documents and References

| Name | Sources |
| ------ | ------ |
| Google Identity: Using OAuth 2.0 for Web Server Applications | [/identity/protocols/oauth2/web-server][PlDb] |
| Google Calendar API | [/calendar/api/v3/referenc][PlGh] |
| Google Account Credentials| [/identity/protocols/oauth2/web-server#exchange-authorization-code][PlIa] |


[PlDb]: <https://developers.google.com/identity/protocols/oauth2/web-server>
[PlGh]: <https://developers.google.com/calendar/api/v3/reference>
[PlIa]: <https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-codee>
