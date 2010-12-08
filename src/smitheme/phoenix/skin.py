from silva.core.smi.interfaces import ISMILayer
from silva.core import conf as silvaconf

class ISMIPhoenixLayer(ISMILayer):
    pass


class ISMIPhoenixSkin(ISMIPhoenixLayer):
    silvaconf.resource('phoenix.css')


