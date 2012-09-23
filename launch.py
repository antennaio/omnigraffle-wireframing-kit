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


def format_filename(device, orientation, id='1'):
    """Format a file name."""
    return id + '-' + device + '-' + orientation + '.html'


def wireframes(active_id=0):
    """Make a list of dictionaries with all wireframes."""
    wireframes = []

    for c in xrange(0, len(config['Wireframes'])):
        wireframe_id = c + 1
        w = config['Wireframes']['Wireframe ' + str(wireframe_id)]
        show_on_device = w['show_on_device']
        d = config['Devices']['Device ' + str(show_on_device)]

        data = {
            'title': w['title'],
            'url': format_filename(d['device'], d['orientation'], str(wireframe_id))
        }

        if active_id == wireframe_id:
            data['active'] = True

        wireframes.append(data)

    return wireframes


@app.context_processor
def project_title():
    """Project title available in templates."""
    return dict(project_title=config['General']['project'])


@app.context_processor
def initial_wireframe():
    """Initial wireframe available in templates."""
    w = config['Wireframes']['Wireframe 1']
    show_on_device = w['show_on_device']
    d = config['Devices']['Device ' + str(show_on_device)]
    return dict(initial_wireframe=format_filename(device=d['device'], orientation=d['orientation']))


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', wireframes=wireframes())


@app.route('/<int:wireframe_id>-<string:device>-<string:orientation>.html', methods=['GET'])
def show(wireframe_id, device, orientation):
    # open wireframe exported from Omnigraffle
    path = 'static' + os.sep + omnigraffle_folder + os.sep + device + '-' + orientation
    wireframe_filename = format_filename(device, orientation, str(wireframe_id))

    try:
        f = open(os.path.join(path, wireframe_filename), "r")
    except IOError:
        return render_template('not_found.html', wireframes=wireframes())

    # fix img src
    file_content = re.sub(r'src=\"', 'src="%s/' % path, f.read())


    # make a list of dictionaries with devices on which this wireframe will be displayed
    devices = []

    for c in xrange(0, len(config['Devices'])):
        device_id = c + 1
        d = config['Devices']['Device ' + str(device_id)]

        path = 'static' + os.sep + omnigraffle_folder + os.sep + d['device'] + '-' + d['orientation']
        device_filename = format_filename(d['device'], d['orientation'], str(wireframe_id))

        if os.path.isfile(os.path.join(path, device_filename)):
            data = {
                'title': d['title'],
                'url': device_filename
            }

            if device_filename == wireframe_filename:
                data['active'] = True

            devices.append(data)

    return render_template('show.html', wireframes=wireframes(wireframe_id), wireframe=file_content, devices=devices)


if __name__ == '__main__':
    app.run()