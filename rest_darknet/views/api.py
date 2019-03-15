
from flask import Blueprint
from flask import jsonify
from flask import request

from rest_darknet import load_image_color
from rest_darknet.pydarknet.image import Image, NotAllowedFileException

module = Blueprint('api', __name__, url_prefix='/api/v1')

from rest_darknet.views.response import *
from rest_darknet.pydarknet.classifier import Classifier

from rest_darknet_config import UPLOAD_FOLDER


@module.route('/upload_image', methods=['POST'])
def upload_image():
    # check if the post request has the file part
    if 'image' not in request.files:
        return jsonify(NO_IMAGE_FOUND.body), NO_IMAGE_FOUND.status_code

    file = request.files['image']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        return jsonify(NO_SELECTED_IMAGE.body), NO_SELECTED_IMAGE.status_code
    if file:
        try:
            img = Image(file)
        except NotAllowedFileException:
            return jsonify(NOT_ALLOWED_FILE.body), NOT_ALLOWED_FILE.status_code
        try:
            filename = img.save_file()
        except FileNotFoundError:
            return jsonify(INTERNAL_SERVER_ERROR.body), INTERNAL_SERVER_ERROR.status_code
        response = SuccessResponse({"filename": filename}, "OK")
        return jsonify(response.body), response.status_code



@module.route('/classify', methods=['GET'])
def image_classify():
    _limit = 10
    clf = Classifier()
    img_url = request.args.get('img')
    image_instance = load_image_color(UPLOAD_FOLDER + '/{}'.format(img_url))
    if request.args.get('limit'):
        _limit = int(request.args.get('limit'))
    result = {
        "result": clf.classify(image_instance)[:_limit]
    }
    return jsonify(result), 200