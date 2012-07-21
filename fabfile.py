from fabric.api import local, lcd

url = 'http://localhost:5000'
export_folder = 'export'

def setup():
    local('pip install -r requirements.txt')


def start():
    local('python launch.py')


def export():
    """Create a static copy of the wireframes."""
    local('mkdir -p %s' % export_folder)
    with lcd(export_folder):
        local('rm -rf *')
        local('wget -mk -w0.2 --no-host-directories %s' % url)