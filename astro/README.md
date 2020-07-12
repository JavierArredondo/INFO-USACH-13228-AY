# Witsi witsi araña
Para ejecutar el Productor en forma de desarrollo es necesario tener descargado algunos archivos `tar.gz` en un directorio data. La recomendación es ir a la página de [ZTF Archive](https://ztf.uw.edu/alerts/public/) y descargar archivos razonablemente livianos.
Los pasos a seguir serían:

```bash
mkdir data
cd data
wget https://ztf.uw.edu/alerts/public/ztf_public_20200330.tar.gz
```

Luego ejecutar el script
```bash
python breeder.py
``` 

Si ejecutan el script de un servidor, es posible que el script realice la tarea de descargar los n-últimos archivos. Para descargar los últimos 5 archivos deben ejecutar:
```bash
python breeder.py 5
```