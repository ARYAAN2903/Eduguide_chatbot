import io
import tempfile

import flask
from flask import render_template
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import googleapiclient.discovery
from google_auth import build_credentials, get_user_info

from werkzeug.utils import secure_filename

app = flask.Blueprint('google_drive', __name__)

def build_drive_api_v3():
    credentials = build_credentials()
    return googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

@app.route('/login')
def login():
    credentials = build_credentials()  # replace with your function to get user credentials
    drive_api = build_drive_api_v3(credentials)
    files = []
    page_token = None
    while True:
        response = drive_api.files().list(q="trashed = false",
                                          fields="nextPageToken, files(id, name)").execute()
        files.extend(response.get('files', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    
    all_files = list_files(credentials)
    files.extend(all_files)
    
    return render_template('list.html', files=files)


def save_image(file_name, mime_type, file_data):
    drive_api = build_drive_api_v3()

    generate_ids_result = drive_api.files().generateIds(count=1).execute()
    file_id = generate_ids_result['ids'][0]

    body = {
        'id': file_id,
        'name': file_name,
        'mimeType': mime_type,
    }

    media_body = MediaIoBaseUpload(file_data,
                                   mimetype=mime_type,
                                   resumable=True)

    drive_api.files().create(body=body,
                             media_body=media_body,
                             fields='id,name,mimeType,createdTime,modifiedTime').execute()

    return file_id


@app.route('/gdrive/upload', methods=['GET', 'POST'])
def upload_file():
    if 'file' not in flask.request.files:
        return flask.redirect('/api')

    file = flask.request.files['file']
    if (not file):
        return flask.redirect('/api')
        
    filename = secure_filename(file.filename)

    fp = tempfile.TemporaryFile()
    ch = file.read()
    fp.write(ch)
    fp.seek(0)

    mime_type = flask.request.headers['Content-Type']
    save_image(filename, mime_type, fp)

    return flask.redirect('/api')

def list_files():
    drive_api = build_drive_api_v3()
    files = drive_api.files().list(q="trashed = false and modifiedTime > '2022-01-01T00:00:00'").execute()
    return files.get('files', [])

@app.route('/gdrive/list', methods=['GET'])
def list_files_route():
    files = list_files()
    return flask.render_template('list_files.html', files=files)

@app.route('/gdrive/view/<file_id>', methods=['GET'])
def view_file(file_id):
    drive_api = build_drive_api_v3()

    metadata = drive_api.files().get(fields="name,mimeType", fileId=file_id).execute()

    request = drive_api.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()

    fh.seek(0)

    return flask.send_file(
                     fh,
                     download_name=metadata['name'],
                     mimetype=metadata['mimeType']
               )

    
def download_file(file_id):
    drive_api = build_drive_api_v3()

    # Get the metadata of the file
    file_metadata = drive_api.files().get(fileId=file_id).execute()

    # Download the file content
    request = drive_api.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()


    # Return the file content and metadata
    return fh.getvalue(), file_metadata

@app.route('/gdrive/download/<file_id>', methods=['GET'])
def download_file_route(file_id):
    file_content, file_metadata = download_file(file_id)
    return flask.send_file(
        io.BytesIO(file_content),
        mimetype=file_metadata['mimeType'],
        download_name=file_metadata['name'],
        as_attachment=True
    )


def delete_file(file_id):
    drive_api = build_drive_api_v3()

    # Delete the file from Google Drive
    drive_api.files().delete(fileId=file_id).execute()

    # Return a success message
    return 'File deleted successfully.'



@app.route('/gdrive/delete/<file_id>', methods=['GET'])
def delete_file_route(file_id):
    message = delete_file(file_id)
    return flask.Response(message)

