class Link(object):
    """Generic link."""

    def __init__(self, id, page, title, device, orientation):
        self.id = id
        self.page = page
        self.title = title
        self.device = device
        self.orientation = orientation

    def url(self):
        """Returns an URL."""
        return str(self.page) + '-' + self.device + '-' + self.orientation + '.html'


class LinkSet(object):
    """A set of links."""

    def __init__(self):
        self.links = []

    def __iter__(self):
        return iter(self.links)

    active_id = 0


class WireframeSet(LinkSet):
    """A set of wireframes."""

    def __init__(self, config):
        super(WireframeSet, self).__init__()

        self.config = config

        for c in xrange(0, len(self.config['Wireframes'])):
            wireframe_id = c + 1
            w = self.config['Wireframes']['Wireframe ' + str(wireframe_id)]
            d = self.config['Devices']['Device ' + w['show_on_device']]
            self.links.append(Link(wireframe_id, wireframe_id, w['title'].decode('utf-8'), d['device'].decode('utf-8'), d['orientation'].decode('utf-8')))


class DeviceSet(LinkSet):
    """A set of devices."""

    def __init__(self, config):
        super(DeviceSet, self).__init__()

        self.config = config

        for c in xrange(0, len(self.config['Devices'])):
            device_id = c + 1
            d = self.config['Devices']['Device ' + str(device_id)]
            self.links.append(Link(device_id, None, d['title'].decode('utf-8'), d['device'].decode('utf-8'), d['orientation'].decode('utf-8')))

    def get_id(self, device, orientation):
        for d in self.links:
            if d.device == device and d.orientation == orientation:
                return d.id

    def set_page(self, page):
        for d in self.links:
            d.page = page
