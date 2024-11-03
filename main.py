import argparse
import os
from get_data import tropicaltidbits

def main():
    parser = argparse.ArgumentParser(description="Descargar productos de pronósticos tropicales.")
    parser.add_argument('-s', '--source', required=True, choices=['tropicaltidbits', 'weathernerds'],
                        help="Fuente de datos (e.g., tropicaltidbits, weathernerds).")
    parser.add_argument('-d', '--date', required=True, help="Fecha y hora en formato YYYYMMDDHH.")
    parser.add_argument('-p', '--path', required=True, help="Directorio de destino para las imágenes.")
    parser.add_argument('-v', '--variable', required=True, choices=['apcpn', 'mslp_pcpn'],
                        help="Variable meteorológica (e.g., apcpn, mslp_pcpn).")
    parser.add_argument('-r', '--region', required=True, choices=['watl'],
                        help="Región geográfica (e.g., watl).")
    
    args = parser.parse_args()

    # Verificación y llamada al módulo correspondiente
    if args.source == 'tropicaltidbits':
        tropicaltidbits.download_images(args.date, args.path, args.variable, args.region)
    else:
        print("Fuente de datos no implementada.")
        
if __name__ == "__main__":
    main()
