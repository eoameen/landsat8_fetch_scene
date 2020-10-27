import os
import argparse
from glob import glob
from typing import List
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def _validate_input(bands: List[int]) -> bool:
    """Validate input to fetch_scene"""
    for band in bands:
        if band not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            raise ValueError("Incorrect bands. \
                Bands should be numbers between 1 and 11")
    return True


def fetch_scene(
        s3_endpoint: str,
        out_dir: str,
        bands: List[int]
        ) -> List[str]:
    """
    Download bands of a landsat-8 scene using awscli.
    In addition to input bands, metadata, thumbnails and
    quality assurance band are always included.
    """
    _validate_input(bands)
    # fetch scene
    cmd = f'aws s3 sync {s3_endpoint} {out_dir} \
        --exclude "*" \
        --include "*_BQA.TIF" --include "*.json" \
        --include "*.txt" --include "*.jpg"'
    for band in bands:
        cmd += (f' --include "*_B{band}.TIF"')
    logger.info("Downloading scene files ..")
    subprocess.run(
        cmd,
        shell=True,
        check=True,
        stdout=open(os.devnull, 'w'),
        stderr=subprocess.STDOUT
        )
    # return sorted file list
    files = sorted(glob(f'{out_dir}/*'))
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--endpoint",
        help="s3 endpoint. Make sure it exists.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_directory",
        help="Path to putput directory. Default is output/.",
        type=str,
        default="output",
    )
    parser.add_argument(
        "-b",
        "--bands",
        help="List of Landsat8 bands to download. Default all bands.",
        type=int,
        nargs="*",
        default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    )
    args = parser.parse_args()
    fetch_scene(args.endpoint, args.output_directory, args.bands)
