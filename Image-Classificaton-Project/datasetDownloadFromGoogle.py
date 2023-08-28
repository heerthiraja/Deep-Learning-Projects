from simple_image_download import simple_image_download as sim

response = sim.simple_image_download

response().download('harrypotter', 60)

#print(response().urls('batmanjoker', 45))

#response().download('batmanjoker', 5,extensions={'.jpg'})
#print(response().urls('batmanjoker', 5,extensions={'.jpg'}))