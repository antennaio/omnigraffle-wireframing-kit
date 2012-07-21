[General]
project = string(default=Omnigraffle Wireframing Kit)

[Devices]
	[[__many__]]
		title = string
		device = string
		orientation = string

[Wireframes]
	[[__many__]]
		title = string(default=Wireframe Title)
		show_on_device = int
