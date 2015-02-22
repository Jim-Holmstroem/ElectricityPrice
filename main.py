from __future__ import division, print_function

from operator import attrgetter

from matplotlib import pyplot

import pandas as pd


def one_year_data(year):
    """
    """
    float_ = lambda x: float('nan' if x=='-' else x)

    raw = pd.read_csv(
        'data/elspot-prices_{year}_hourly_sek.csv'.format(
            year=year,
        ),
        header=2,
        usecols=(0, 'Hours', 'SE3'),
        converters={
            'SE3': float_,
            'Hours': lambda x: x.split()[0] + ':00:00',
        }
    )

    index = pd.to_datetime(raw.icol(0) + ' ' + raw.icol(1))

    no_duplicate_time = lambda x: x.groupby(level=0).last()

    data = no_duplicate_time(
        raw.join(pd.DataFrame(index, columns=['time', ])).set_index('time')[
            ['SE3', ]
        ]
    )

    return data


def data(years=('2013', '2014'), currency='sek'):
    return pd.concat(
        map(
            one_year_data,
            years
        )
    )


df = data()


def boxplot_over_variable(df, variable='hour'):
    df.groupby(attrgetter(variable)).boxplot(subplots=False, rot=45)
    pyplot.show()
