from __future__ import division, print_function

import pandas as pd


def one_year_data(year):
    """
    """

    raw = pd.read_csv(
        'data/elspot-prices_{year}_hourly_sek.csv'.format(
            year=year,
        ),
        header=2,
        usecols=(0, 'Hours', 'SE1', 'SE2', 'SE3', 'SE4'),
        converters={
            'Hours': lambda x: x.split()[0] + ':00:00'
        }
    )

    index = pd.to_datetime(raw.icol(0) + ' ' + raw.icol(1))

    data = raw.join(pd.DataFrame(index, columns=['time', ])).set_index('time')[
        ['SE1', 'SE2', 'SE3', 'SE4']
    ]

    return data


def data(years=('2013', '2014', '2015'), currency='sek'):
    return pd.concat(
        map(
            one_year_data,
            years
        )
    )
