#!/usr/bin/env python

from pathlib import Path
import time
import json

from scrapers.nairabet import get


def main():

    # Create the data directory
    Path('data').mkdir(parents=True, exist_ok=True)

    # Fetch data and save to JSON
    data = get()
    with open(f'data/{int(time.time())}.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()