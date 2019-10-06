import pygal_maps_world.maps
wm=pygal_maps_world.maps.World()
wm.title='North,Central,and South America'
wm.add('North America',['ca','mx','us'])

wm.render_to_file('americas.svg')
