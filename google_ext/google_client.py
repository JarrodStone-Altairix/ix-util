import pickle
import os.path
from ix.google_ext.config import Cfg
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Google_Client:

  def __init__(self):

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    self.creds = None
    if os.path.exists(Cfg.fp_tokens):
      with open(Cfg.fp_tokens, "rb") as tokens:
        self.creds = pickle.load(tokens)

    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                Cfg.fp_credentials, Cfg.auth_scopes)
            self.creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(Cfg.fp_tokens, 'wb+') as tokens:
            pickle.dump(self.creds, tokens)

  def build_drive_service(self):
    return build('drive', Cfg.version, credentials=self.creds)

  def get_auth_headers(self):
    return {"Authorization": "Bearer " + self.creds.token}
