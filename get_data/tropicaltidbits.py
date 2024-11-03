import os
import requests

# Dictionary mapping each model to its maximum forecast step
MODEL_STEPS = {
    'gfs': 64,
    'ecmwf': 30,
    'gem': 40,
    'icon': 60,
    'navgem': 6,
    'ec-aifs': 60,
    'nam': 28
}

# Base URLs for each model, where {date}, {variable}, {region}, and {step} will be formatted
BASE_URLS = {
    'gfs': "https://www.tropicaltidbits.com/analysis/models/gfs/{date}/gfs_{variable}_{region}_{step}.png",
    'ecmwf': "https://www.tropicaltidbits.com/analysis/models/ecmwf/{date}/ecmwf_{variable}_{region}_{step}.png",
    'gem': "https://www.tropicaltidbits.com/analysis/models/gem/{date}/gem_{variable}_{region}_{step}.png",
    'icon': "https://www.tropicaltidbits.com/analysis/models/icon/{date}/icon_{variable}_{region}_{step}.png",
    'navgem': "https://www.tropicaltidbits.com/analysis/models/navgem/{date}/navgem_{variable}_{region}_{step}.png",
    'ec-aifs': "https://www.tropicaltidbits.com/analysis/models/ec-aifs/{date}/ec-aifs_{variable}_{region}_{step}.png",
    'nam': "https://www.tropicaltidbits.com/analysis/models/nam/{date}/nam_{variable}_{region}_{step}.png"
}

def download_image(url, path):
    """
    Downloads an image from a specified URL and saves it to the given path.
    
    Parameters:
        url (str): The URL of the image to download.
        path (str): The file path to save the image.
    """
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {path}")
        else:
            print(f"Failed to download {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_images(date, output_dir, variable, region):
    """
    Downloads forecast images from Tropical Tidbits for all models, organized by model and forecast steps.
    
    Parameters:
        date (str): The forecast date and time in YYYYMMDDHH format.
        output_dir (str): The base directory to store downloaded images.
        variable (str): The meteorological variable to download (e.g., 'apcpn', 'mslp_pcpn').
        region (str): The geographical region for the forecast (e.g., 'watl').
    """
    # Create the main directory for the specified date
    date_dir = os.path.join(output_dir, date)
    os.makedirs(date_dir, exist_ok=True)

    # Loop through each model and its maximum forecast step
    for model, max_steps in MODEL_STEPS.items():
        # Create a subdirectory for each model
        model_dir = os.path.join(date_dir, model)
        os.makedirs(model_dir, exist_ok=True)
        
        # Download each step within the forecast range for the model
        for step in range(1, max_steps + 1):
            url = BASE_URLS[model].format(date=date, variable=variable, region=region, step=step)
            file_path = os.path.join(model_dir, f"{model}_{variable}_{region}_{step}.png")
            download_image(url, file_path)
