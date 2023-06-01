from pathlib import Path
import time
import json

from scrapers.nairabet import get


def main():

    # Create the data directory
    Path('data').mkdir(parents=True, exist_ok=True)

    while True:

        # Fetch data and save to JSON
        try:
            data = get()
            with open(f'data/{int(time.time())}.json', 'w') as f:
                json.dump(data, f)
        except BaseException as e:
            pass

        # Wait 5 minutes
        time.sleep(60 * 5)


if __name__ == "__main__":
    main()