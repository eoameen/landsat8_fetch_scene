# A tool for fetching Landsat-8 scenes

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
```sh
docker run --rm -it \
      -v `pwd`:/workspace \
      -v "$HOME/.aws:/home/.aws" \
      landsat8-fetch-scene python3 src/fetch_scene.py \
      --endpoint s3://landsat-pds/c1/L8/045/033/LC08_L1TP_045033_20200528_20200528_01_RT/ \
      --output_directory LC08_L1TP_045033_20200528_20200528_01_RT \
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
