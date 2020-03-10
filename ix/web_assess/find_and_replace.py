from ix.google_ext.google_client import Google_Client
from ix.web_assess.core import resolve_identities


def find_and_replace(identities, find, replace, searchByRegex=False):

  # Setup
  client = Google_Client()
  srvc = client.build_sheets_service()
  sheets = srvc.spreadsheets()

  # Build json request
  req_json = {
      "find": find,
      "replacement": replace,
      "searchByRegex": searchByRegex,
      "matchCase": False,
      "matchEntireCell": False,
      "includeFormulas": False,
      "allSheets": True
  }

  # Update all files
  for file_id, _, _, in resolve_identities(identities):
    result = sheets.batchUpdate(
        spreadsheetId=file_id, body={
            "includeSpreadsheetInResponse": False,
            "requests": [{"findReplace": req_json}]}).execute()

    print(result)
