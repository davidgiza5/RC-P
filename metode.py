
class BasicResource():
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server)
        self.payload = "Basic Resource"
        self.tip_resursa = "resursa"
        self.continut = "text"


    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, BasicResource())
        return res

    def render_DELETE(self, request):
        return True




