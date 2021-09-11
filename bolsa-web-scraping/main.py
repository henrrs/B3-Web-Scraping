# [START app]

#[START imports]
import logging
import os

from flask import current_app, Flask, request
from utils import get_current_date, download_zip_file, concate_strings, save_to_gcs

import pytz
#[END imports]

app = Flask(__name__)

app.config['BOLSA_BASE_URL'] = os.environ['BOLSA_BASE_URL']
app.config['FILE_NAME'] = os.environ['FILE_NAME']
app.config['FILE_FORMAT'] = os.environ['FILE_FORMAT']
app.config['TIME_ZONE'] = os.environ['TIME_ZONE']
app.config['BUCKET_NAME'] = os.environ['BUCKET_NAME']

BTZ = pytz.timezone(app.config['TIME_ZONE'])

# [START index]
@app.route('/', methods=['GET'])
def index():
    date = get_current_date(BTZ)

    final_file_name = concate_strings(app.config['FILE_NAME'], date, app.config['FILE_FORMAT'])
    final_url = concate_strings(app.config['BOLSA_BASE_URL'], final_file_name)

    content = download_zip_file(final_url, final_file_name)
    save_to_gcs(app.config['BUCKET_NAME'], final_file_name, content)

    return 'OK', 200
# [END index]

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END app]