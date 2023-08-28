from google_images_search import GoogleImagesSearch

# Set up the GoogleImagesSearch object
gis = GoogleImagesSearch('<your Google API key>', '<your Google custom search engine ID>')

# Define your search parameters
search_params = {
    'q': 'harry potter',
    'num': 5,  # Number of images to download
    'safe': 'high',  # Safety level for the images
    'fileType': 'jpg'  # File type of the images
}

# Perform the search and download the images
gis.search(search_params)
for image in gis.results():
    image.download('harrypotter')  # Specify the download folder

# Print the status of each downloaded image
for image in gis.results():
    print(image.status)
