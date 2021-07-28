# Landsat-8: Fetch scene
A tool for fetching Landsat-8 (OLI-TIRS) scenes from [`usgs-landsat`](https://registry.opendata.aws/usgs-landsat/) bucket on AWS.


## Build image

```sh
docker build -t landsat8-fetch-scene .
```

## Credentials
Make `.aws/credentials` file and put it in your home directory.
`.aws/credentials` should be like
```
[default]
aws_secret_access_key=xxxxxxxxxxxxxxxxxxxx
aws_access_key_id=xxxxxxxxxxxxxxxxxxxx
```

## Usage
Fetch landsat-8 scene given: 1) scene s3 endoint, 2) output directory, and 3) list of bands/files.
```sh
docker run --rm -it -v `pwd`:/workspace landsat8-fetch-scene python3 src/fetch_scene.py --help
```

```sh
usage: fetch_scene.py [-h] -i ENDPOINT [-o OUTPUT_DIRECTORY]
                      [-b [BANDS [BANDS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -i ENDPOINT, --endpoint ENDPOINT
                        s3 endpoint. Make sure it exists.
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        Path to putput directory. Default is output/.
  -b [BANDS [BANDS ...]], --bands [BANDS [BANDS ...]]
                        List of Landsat8 bands to download. Default all bands.
```

* Example:
```bash
docker run --rm -it \
      -v `pwd`:/workspace \
      -v "$HOME/.aws:/home/.aws" \
      landsat8-fetch-scene python3 src/fetch_scene.py \
      --endpoint s3://usgs-landsat/collection02/level-1/standard/oli-tirs/2021/046/028/LC08_L1TP_046028_20210725_20210725_02_RT/ \
      --output_directory output \
      --bands 5 6 7
```

## Linting
Autopep8
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-fetch-scene /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        autopep8 -i -a -a -r ."
```

Flake8
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-fetch-scene /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        flake8 --config=.flake8"
```

## Type checking
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    landsat8-fetch-scene /bin/bash -c \
        "pip3 install -r requirements-dev.txt && \
        mypy --config-file mypy.ini ./src/*.py"
```

## Testing
```bash
docker run \
    --rm -it \
    -v `pwd`:/workspace \
    -v "$HOME/.aws:/home/.aws" \
    -e "PYTHONPATH=." \
    landsat8-fetch-scene /bin/bash -c \
        "pip3 install -r requirements-dev.txt && pytest tests"
```
