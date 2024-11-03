import os
import requests

# Diccionario que mapea cada modelo a su paso máximo
MODEL_STEPS = {
    'gfs': 64,
    'ecmwf': 30,
    'gem': 40,
    'icon': 60,
    'navgem': 6,
    'ec-aifs': 60,
    'nam': 28
}

# Diccionario de URLs base
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
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {path}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_images(date, output_dir, variable, region):
    # Crear el directorio principal de fecha YYYYMMDDHH
    date_dir = os.path.join(output_dir, date)
    os.makedirs(date_dir, exist_ok=True)

    # Descargar imágenes para cada modelo
    for model, steps in MODEL_STEPS.items():
        # Crear subcarpeta para cada modelo
        model_dir = os.path.join(date_dir, model)
        os.makedirs(model_dir, exist_ok=True)
        
        # Descargar cada paso de tiempo (STEP) para el modelo
        for step in range(1, steps + 1):
            url = BASE_URLS[model].format(date=date, variable=variable, region=region, step=step)
            file_path = os.path.join(model_dir, f"{model}_{variable}_{region}_{step}.png")
            download_image(url, file_path)
