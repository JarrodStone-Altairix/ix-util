import os


class Cfg:
  fp_credentials = os.path.join(os.path.dirname(__file__), "credentials.json")
  fp_tokens = os.path.join(os.path.dirname(__file__), "tokens.pickle")

  auth_scopes = [
      "https://www.googleapis.com/auth/drive",
      "https://www.googleapis.com/auth/drive.file",
      "https://www.googleapis.com/auth/drive.appdata",
      "https://www.googleapis.com/auth/drive.readonly",
      "https://www.googleapis.com/auth/spreadsheets"]
