try:
    from flask import Flask, render_template
except (ImportError):
    print 'Please install Flask first.'
    exit(1)

try:
    from configobj import ConfigObj, ConfigObjError
    from validate import Validator
except (ImportError):
    print 'Please install ConfigObj first.'
    exit(1)

import re
import os.path

from kit import WireframeSet, DeviceSet

app = Flask(__name__)
app.config['DEBUG'] = True

omnigraffle_folder = 'omnigraffle'

config_file = 'wireframes.ini'
config_spec = 'wireframes.spec'

try:
    config = ConfigObj(config_file, configspec=config_spec)
except (ConfigObjError, IOError), e:
    print 'Fatal error: %s' % e
    exit(1)

validator = Validator()
result = config.validate(validator)

if not result:
    print 'Fatal error: Config file validation failed!'
    exit(1)


@app.context_processor
def project_title():
    """Project title available in templates."""
    return dict(project_title=config['General']['project'])


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', wireframes=WireframeSet(config))


@app.route('/<int:wireframe_id>-<string:device>-<string:orientation>.html', methods=['GET'])
def show(wireframe_id, device, orientation):

    # open wireframe exported from Omnigraffle
    path = 'static' + os.sep + omnigraffle_folder + os.sep + device + '-' + orientation
    filename = str(wireframe_id) + '-' + device + '-' + orientation + '.html'

    try:
        f = open(os.path.join(path, filename), "r")
    except IOError:
        return render_template('not_found.html', wireframes=WireframeSet(config))

    # fix img src
    wireframe = re.sub(r'src=\"', 'src="%s/' % path, f.read())

    devices = DeviceSet(config)
    devices.set_page(wireframe_id)
    devices.active_id = devices.get_id(device, orientation)

    wireframes = WireframeSet(config)
    wireframes.active_id = wireframe_id

    return render_template('show.html', wireframes=wireframes, devices=devices, wireframe=wireframe)


if __name__ == '__main__':
    app.run()
