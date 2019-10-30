Omnigraffle Wireframing Kit
===========================

Omnigraffle Wireframing Kit helps to organize your wireframes into a slick presentation. 

Demo
----

Open the files in the `/export` directory for a demo.

Installation
------------

You may want to start with creating a new [virtualenv](http://www.virtualenv.org):

```
virtualenv --no-site-packages wireframing-kit
. wireframing-kit/bin/activate
```

Clone and setup the kit:

```
git clone https://github.com/antennaio/omnigraffle-wireframing-kit.git
cd omnigraffle-wireframing-kit
pip install -r requirements.txt
fab start
```

Now you can open "http://localhost:5000" in your browser.

Configuration
-------------

Edit wireframes.ini to modify or add wireframes or devices to your project.

Exporting wireframes from Omnigraffle
-------------------------------------

Open Omnigraffle files from the "static/omnigraffle/" folder to edit the wireframes. When ready
go to "File > Export...". Select "HTML image map" format. Select "Entire Document" in the "Export Area" menu.
Confirm with "Save".
