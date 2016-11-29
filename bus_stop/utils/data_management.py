import csv
from bus_stops.models import Stop
import pandas as pd

BASE_DIR = 'C:/PDXCODE/github_projects/bus_stop/bus_stop/utils/data/'

def clean_data():
    stops_sets = ['stop-subway.csv',
                  'stops-bronx.csv',
                  'stops-brooklyn.csv',
                  'stops-manhattan.csv',
                  'stops-queens.csv',
                  'stops-staten.csv']
    for stops in stops_set:
        with open(BASE_DIR + stops) as file:
            url = '-clean.'.join(stops.split('.'))

            df = pd.DataFrame.from_csv(file)
            clean = df.drop_duplicates()
            df.to_csv(path_or_buf=BASE_DIR + url)



def make_models():
    stops_sets = ['stop-subway-clean.csv',
                  'stops-bronx-clean.csv',
                  'stops-brooklyn-clean.csv',
                  'stops-manhattan-clean.csv',
                  'stops-queens-clean.csv',
                  'stops-staten-clean.csv']
    for stops in stops_sets:
        with open(BASE_DIR + stops) as file:
            reader = csv.DictReader(file)
            next(reader)
            for row in reader:
                stop = Stop.objects.create(
                       stop_id=row['stop_id'],
                       street=row['stop_name'],
                       lat=float(row['stop_lat']),
                       lng=float(row['stop_lon']))
                stop.save()
                print('Stop {} Created!'.format(row['stop_id']))

    print('Done!')
