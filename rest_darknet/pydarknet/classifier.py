
from rest_darknet import neural_net
from rest_darknet import meta
from rest_darknet.pydarknet.lib_wrapper import network_predict_image

class Classifier(object):

    def __init__(self):
        self.probabilities = None


    @staticmethod
    def classify(img):
        out = network_predict_image(neural_net, img)
        result = []
        for i in range(meta.classes):
            result.append((meta.names[i].decode("utf-8") , out[i]))
        return sorted(result, key=lambda x: -x[1])

