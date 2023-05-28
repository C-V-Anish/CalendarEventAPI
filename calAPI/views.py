from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

REDIRECT_URL = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] # Define SCOPES for Google Calendar access
SECRET_FILE = 'client_secret.json'

class GoogleCalendarInitView(APIView):
    def get(self, request):
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                SECRET_FILE, 
                scopes=SCOPES,
                redirect_uri=REDIRECT_URL
            ) # OAuth Flow Creation

            authorization_url, state = flow.authorization_url(
                access_type='offline',
                prompt='consent'
            ) # Authorization URL Creation

            request.session['oauth_state'] = state

            return Response({'authorization_url': authorization_url})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        try:
            code = request.query_params.get('code') # Retrieve Authorization Code from query parameters

            flow = InstalledAppFlow.from_client_secrets_file(
                SECRET_FILE, 
                scopes=SCOPES,
                redirect_uri = REDIRECT_URL
            )

            flow.fetch_token(code=code) # Get the access and refresh tokens using the Authorization Code 

            credentials = flow.credentials

            # Build the Google Calendar Service and get user's events
            service = build('calendar', 'v3', credentials=credentials)
            events_result = service.events().list(calendarId='primary', maxResults=10).execute()
            events = events_result.get('items', [])

            return Response(events)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
