from pathlib import Path
from google_images_download import google_images_download


cow_breeds = ['Fresian','Shorthorn','Vosges','Jersey','Allgauer','Guernsey','Angler','Charolais','Brown Swiss']
output_folder = Path('D:\\Data\\Cows')

arguments = [{"keywords":f"{k} Cow","output_directory":f"{output_folder}"} for k in cow_breeds]

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

for arg in arguments:
    paths = response.download(arg)