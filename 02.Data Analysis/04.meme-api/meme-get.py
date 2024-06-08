import requests
# import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

meme_req = requests.get("https://meme-api.com/gimme")
meme_url = meme_req.json()["url"]


meme_download = requests.get(meme_url)
meme_download = Image.open(BytesIO(meme_download.content))

meme_download.show()

# plt.imshow(meme_download)
# plt.axis("off")
# plt.show()