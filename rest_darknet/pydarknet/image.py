import os
import uuid

from werkzeug.utils import secure_filename
from rest_darknet.views.response import NOT_ALLOWED_FILE

import rest_darknet_config

class Image(object):

    def __init__(self, request_file):
        self.request_file = request_file
        self.extension = self.request_file.filename.rsplit('.', 1)[1].lower() \
            if '.' in self.request_file.filename else None
        self.filename = secure_filename(self.__get_uuid_filename())
        if not self.__allowed_file():
            raise NotAllowedFileException(
                NOT_ALLOWED_FILE.body['error'],
                NOT_ALLOWED_FILE.status_code,
                NOT_ALLOWED_FILE.body
            )

    def __get_uuid_filename(self):
        return str(uuid.uuid4()) + '.{}'.format(self.extension)

    def __allowed_file(self):
        return  self.extension in rest_darknet_config.ALLOWED_EXTENSIONS

    def save_file(self):
        try:
            self.request_file.save(os.path.join(rest_darknet_config.UPLOAD_FOLDER, self.filename))
        except FileNotFoundError as e:
            raise e
        return self.filename


class NotAllowedFileException(Exception):

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload