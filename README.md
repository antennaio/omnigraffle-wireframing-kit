Omnigraffle Wireframing Kit
===========================

Omnigraffle Wireframing Kit helps to organize your wireframes into a slick presentation. 

Demo
----

Go to [http://netboy.pl/omnigraffle-wireframing-kit](http://netboy.pl/demo/omnigraffle-wireframing-kit) for a demo.

Installation
------------

You may want to start with creating a new [virtualenv](http://www.virtualenv.org):

```
virtualenv --no-site-packages wireframing-kit
. wireframing-kit/bin/activate
```

Clone and setup the kit:

```
git clone https://github.com/netboy/omnigraffle-wireframing-kit.git
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
go to "File > Export...", select "HTML image map" format and confirm with "Save".