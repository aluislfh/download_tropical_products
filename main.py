import argparse
import os
from get_data import tropicaltidbits

def main():
    parser = argparse.ArgumentParser(
        description="Download tropical forecast products from various sources.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Argument for the data source
    parser.add_argument(
        '-s', '--source',
        required=True,
        choices=['tropicaltidbits', 'weathernerds'],
        help="Data source (e.g., tropicaltidbits, weathernerds). Currently, only 'tropicaltidbits' is supported."
    )
    
    # Argument for the forecast date and time
    parser.add_argument(
        '-d', '--date',
        required=True,
        help="Forecast date and time in YYYYMMDDHH format (e.g., 2024110312 for Nov 3, 2024, 12 UTC)."
    )
    
    # Argument for the download path
    parser.add_argument(
        '-p', '--path',
        required=True,
        help="Destination directory for saving images. Each forecast run will create a subdirectory named with the date (e.g., YYYYMMDDHH)."
    )
    
    # Argument for the meteorological variable
    parser.add_argument(
        '-v', '--variable',
        required=True,
        choices=['apcpn', 'mslp_pcpn'],
        help="Meteorological variable to download (e.g., 'apcpn' for accumulated precipitation, 'mslp_pcpn' for mean sea-level pressure and precipitation)."
    )
    
    # Argument for the geographical region
    parser.add_argument(
        '-r', '--region',
        required=True,
        choices=['watl'],
        help="Geographical region. Currently, only 'watl' (Western Atlantic) is supported."
    )
    
    args = parser.parse_args()

    # Check and call the appropriate module for data download
    if args.source == 'tropicaltidbits':
        tropicaltidbits.download_images(args.date, args.path, args.variable, args.region)
    else:
        print("Data source not implemented. Please check the available options with --help.")
        
if __name__ == "__main__":
    main()
