from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {
    "keywords": "spiderman",
    "limit": 2,
    "output_directory": "spiderman",
    "format": "jpg"
}

response.download(arguments)
