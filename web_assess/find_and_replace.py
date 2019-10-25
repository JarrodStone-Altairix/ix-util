
from ix.google_ext.google_client import Google_Client

sheet_id = "1NIpJWnckDMW1BEzRf_4uQgdPczAKA6UVgHBKrNL_bTY"
req_json = {
    "find": "enum.input=",
    "replace": "enum.magic=",
}
client = Google_Client()

srvc = client.build_sheets_service()
srvc.spreadsheets().batchUpdate(sheet_id, req_json)