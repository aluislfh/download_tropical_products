# Download Tropical Forecast Products

## About
Download products and create animations from various weather data sources, including Tropical Tidbits, Weathernerds, NHC, WPC, and Tomer Burg (arctic.som.ou.edu). Currently, only Tropical Tidbits is available, with additional sources to be added gradually.

## Project Structure

```plaintext
download_tropical_products
├── create_animations
│   └── create_gif_and_mp4.py    # Script to create GIFs and MP4 animations from downloaded images
├── get_data
│   ├── tropicaltidbits.py       # Script for downloading images from Tropical Tidbits
│   └── weathernerds.py          # Placeholder for future integration with Weathernerds
├── main.py                      # Main entry point of the application
└── README.md                    # Project documentation
```

### File Descriptions

- **`create_animations/create_gif_and_mp4.py`**: Script for generating GIF and MP4 animations from downloaded forecast images.
- **`get_data/tropicaltidbits.py`**: Script to download forecast images from Tropical Tidbits by model, date, region, and variable.
- **`get_data/weathernerds.py`**: Placeholder for future Weathernerds integration.
- **`main.py`**: Main script to handle command-line arguments, allowing users to select the data source, date, region, and variables, and calling the appropriate download script.
- **`README.md`**: Documentation file describing the project.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/download_tropical_products.git
   cd download_tropical_products
   ```
2. Ensure you have Python 3 installed. This script uses `requests` for downloading images, which you can install with:
   ```bash
   pip install requests
   ```

## Usage

The main entry point for the project is `main.py`, which accepts various command-line arguments to download forecast images from Tropical Tidbits. Currently, only `tropicaltidbits` as a data source is supported, with additional sources to be added over time.

### Command-line Options

```bash
python main.py -s SOURCE -d DATE -p PATH -v VARIABLE -r REGION
```

- `-s` or `--source`: Source of forecast data. Currently supported options:
  - `tropicaltidbits`
  - *(Future options: `nhc`, `wpc`, `weathernerds`, `tomerburg`)*

- `-d` or `--date`: Forecast date and time in the format `YYYYMMDDHH` (e.g., `2024110312` for November 3, 2024, 12 UTC).
  
- `-p` or `--path`: Directory path where downloaded images will be saved. Each run creates a subfolder with the date `YYYYMMDDHH` inside this directory.

- `-v` or `--variable`: Meteorological variable to download. Currently supported options:
  - `apcpn`: Accumulated precipitation
  - `mslp_pcpn`: Mean sea-level pressure and precipitation

- `-r` or `--region`: Geographical region. Currently supported options:
  - `watl`: Western Atlantic

### Example

To download forecast images from Tropical Tidbits for the date `2024110312`, save them in the directory `/path/to/downloads`, and specify `mslp_pcpn` as the variable and `watl` as the region:

```bash
python main.py -s tropicaltidbits -d 2024110312 -p /path/to/downloads -v mslp_pcpn -r watl
```

This command will:

1. Create a subdirectory under `/path/to/downloads` named `2024110312`.
2. Within `2024110312`, create subfolders for each model (`gfs`, `ecmwf`, `gem`, `icon`, `navgem`, `ec-aifs`, `nam`).
3. Download the relevant images for each model up to the specified forecast steps.

## Future Development

- **Additional Sources**: Support for NHC, WPC, Weathernerds, and Tomer Burg data sources will be added.
- **Improved Animation Features**: Enhance the animation capabilities in `create_animations` to support custom frame rates and other configurations.
- **Additional Regions and Variables**: Expand the list of supported regions and meteorological variables for more comprehensive data access.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


### Key Points in the README

- Provides an overview of the project and its current limitations.
- Describes the project structure, including the purpose of each file.
- Lists dependencies and usage instructions, specifying the options available for `main.py`.
- Includes an example command, demonstrating how to use the script with various options.
- Mentions future plans for additional data sources and functionality.
