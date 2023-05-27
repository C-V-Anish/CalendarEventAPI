from django.shortcuts import redirect
from django.urls import reverse
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response

class GoogleCalendarInitView(APIView):
    def get(self, request):
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] # Define SCOPES for Google Calendar acess

        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', 
            scopes=SCOPES,
            redirect_uri='http://127.0.0.1:8000/rest/v1/calendar/redirect/' 
        ) # OAuth Flow Creation 

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent'
        ) # Authorization URL Creation

        request.session['oauth_state'] = state

        return Response({'authorization_url': authorization_url})

class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        code = request.query_params.get('code') # Retrieve Authorization Code from query parameters

        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', 
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri='http://127.0.0.1:8000/rest/v1/calendar/redirect/'
        )

        flow.fetch_token(code=code) # Get the access and refresh tokens using the Authorization Code 

        credentials = flow.credentials

        # Build the Google Calendar Service and get user's events
        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        return Response(events)
