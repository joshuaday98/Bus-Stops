import csv
from bus_stops.models import NYCStop
import pandas as pd

BASE_DIR = 'C:/PDXCODE/github_projects/bus_stop/bus_stop/utils/data/'

def clean_data():
    stops_sets = ['stop-subway.csv',
                  'stops-bronx.csv',
                  'stops-brooklyn.csv',
                  'stops-manhattan.csv',
                  'stops-queens.csv',
                  'stops-staten.csv']
    frame_set = []

    for stops in stops_sets:
        with open(BASE_DIR + stops) as file:
            url = '-clean.'.join(stops.split('.'))

            df = pd.read_csv(file)
            clean = df.drop_duplicates()
            frame_set.append(clean)
            clean.to_csv(path_or_buf=BASE_DIR + url)

    all_stops = pd.concat(frame_set).drop_duplicates()
    all_stops.to_csv(path_or_buf=BASE_DIR + 'all_stops.csv')



def make_models():
    with open(BASE_DIR + 'all_stops.csv') as file:
        reader = csv.DictReader(file)
        next(reader)
        for row in reader:
            if row['stop_id'].isdigit():
                transit_type = 'bus'
            else:
                transit_type = 'sub'

            stop = NYCStop.objects.create(
                   stop_id=row['stop_id'],
                   street=row['stop_name'],
                   lat=float(row['stop_lat']),
                   lng=float(row['stop_lon']),
                   type=transit_type)
            stop.save()

            print('Stop {} Created!'.format(row['stop_id']))

    print('Done!')
