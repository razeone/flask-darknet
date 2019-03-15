# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import rest_darknet_config

from rest_darknet.pydarknet.lib_wrapper import load_network
from rest_darknet.pydarknet.lib_wrapper import load_image_color
from rest_darknet.pydarknet.lib_wrapper import get_metadata


neural_net = load_network(rest_darknet_config.CONFIG_FILE,
                          rest_darknet_config.WEIGHTS_FILE,
                          0)
meta = get_metadata(rest_darknet_config.META_FILE)

app = Flask(__name__)
app.config.from_object('rest_darknet_config')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from rest_darknet.views import api
app.register_blueprint(api.module)