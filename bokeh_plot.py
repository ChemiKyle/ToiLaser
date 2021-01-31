import pandas as pd
from sqlalchemy import create_engine
from bokeh.io import show
from bokeh.models import HoverTool
from bokeh.plotting import figure

def generate_random_data():
    # adapted from: https://datascience.stackexchange.com/a/54695
    date_rng = pd.date_range(start="01/24/2021 00:00:00", end="01/30/2021 23:00:00", freq="min", tz="UTC")
    tdf = pd.DataFrame(date_rng, columns=['timestamp']).sample(50)
    tdf['location_id'] = 0

    engine = create_engine("cockroachdb://db_user:password@localhost:41335/toilaser")
    tdf.to_sql('log', con=engine, if_exists='append', index=False)

def fetch_data():
    cmd = ("SELECT * FROM log")
    engine = create_engine("cockroachdb://db_user:password@localhost:41335/toilaser")
    return pd.read_sql_query(cmd, engine)


def hexbin_weekdays():
    df = fetch_data()
    x = df.timestamp.dt.dayofweek
    y = df.timestamp.dt.hour

    p = figure(title="Activity over week", match_aspect=False,
               tools="wheel_zoom,reset", background_fill_color='#440154',
               x_range=(0, 6), y_range=(24, 0))
    p.grid.visible = False

    r, bins = p.hexbin(x, y, size=1, hover_color="pink", hover_alpha=0.8)

    p.circle(x=x, y=y + df.timestamp.dt.minute / 60.0 + df.timestamp.dt.second / (60.0**2),
             color="white", size=4, alpha=0.8)

    hover = HoverTool(tooltips=[("count", "@c")],
                      mode="mouse", point_policy="follow_mouse", renderers=[r])

    p.add_tools(hover)
    show(p)


if __name__ == "__main__":
    hexbin_weekdays()
