import os
import requests
import time  # Import for adding delays

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

def file_exists_and_complete(url, path, headers):
    """
    Check if the file at 'path' exists and matches the content length of the file at 'url'.
    
    Parameters:
        url (str): The URL of the image to check.
        path (str): The file path to check.
        headers (dict): Headers to use for the request.
    
    Returns:
        bool: True if the file exists and matches the content length; False otherwise.
    """
    if not os.path.exists(path):
        return False
    
    # Get the content length from the server
    response = requests.head(url, headers=headers)
    if response.status_code == 200:
        content_length = int(response.headers.get('Content-Length', 0))
        file_size = os.path.getsize(path)
        if file_size == content_length:
            print(f"File {path} already exists and is complete.")
            return True
    else:
        print(f"Could not retrieve headers for {url}. HTTP Status Code: {response.status_code}")
    
    return False

def download_image(url, path):
    """
    Downloads an image from a specified URL and saves it to the given path if it doesn't already exist.
    
    Parameters:
        url (str): The URL of the image to download.
        path (str): The file path to save the image.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://www.tropicaltidbits.com/'
    }
    
    # Check if file exists and matches the server file size
    if file_exists_and_complete(url, path, headers):
        print(f"Skipping download for {url} as the file already exists and is complete.")
        return

    print(f"Attempting to download: {url}")  # Debug print
    try:
        response = requests.get(url, headers=headers, stream=True)
        print(f"HTTP Status Code for {url}: {response.status_code}")  # Debug print
        if response.status_code == 200:
            with open(path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded successfully: {path}")
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
    print(f"Created directory: {date_dir}")  # Debug print

    # Loop through each model and its maximum forecast step
    for model, max_steps in MODEL_STEPS.items():
        print(f"Processing model: {model}, with {max_steps} steps")  # Debug print
        
        # Create a subdirectory for each model
        model_dir = os.path.join(date_dir, model)
        os.makedirs(model_dir, exist_ok=True)
        print(f"Created model subdirectory: {model_dir}")  # Debug print
        
        # Download each step within the forecast range for the model
        for step in range(1, max_steps + 1):
            url = BASE_URLS[model].format(date=date, variable=variable, region=region, step=step)
            file_path = os.path.join(model_dir, f"{model}_{variable}_{region}_{step}.png")
            print(f"Generated URL for step {step}: {url}")  # Debug print
            print(f"File will be saved to: {file_path}")  # Debug print
            download_image(url, file_path)
            time.sleep(1)  # Delay of 1 second between requests to avoid rate limiting or IP blocking

    print("Download process completed.")  # Debug print
