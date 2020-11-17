import json
import locale
import glob
import os

from staticjinja import Site

def collect_data_filepaths(directory_path='data', ):
    for file in os.listdir(directory_path):
        if file.endswith(".json"):
            yield os.path.join(directory_path, file)


if __name__ == "__main__":

    #gpus = []
    # for filename in data_filepaths:
    #    with open(filename, 'r') as file:
    #        site_gpus = json.loads(file.read())
    #        gpus.extend(site_gpus)

    with open('data.json', 'r') as file:
        context = {
            'gpus': json.loads(file.read())
        }

    site = Site.make_site(env_globals=context)

    site.render(use_reloader=True)
