from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
import csv
import io
from sqlalchemy import create_engine
from lxml.html import parse
import pfx_data_collection
import time


def write_to_table(df, db_engine, table_name, if_exists='fail'):
    string_data_io = io.StringIO()
    df.to_csv(string_data_io, sep='|', index=False)
    pd_sql_engine = pd.io.sql.pandasSQL_builder(db_engine)
    table = pd.io.sql.SQLTable(table_name, pd_sql_engine, frame=df,
                               index=False, if_exists=if_exists)
    table.create()
    string_data_io.seek(0)
    string_data_io.readline()  # remove header
    with db_engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            copy_cmd = "COPY %s FROM STDIN HEADER DELIMITER '|' CSV" % table_name
            cursor.copy_expert(copy_cmd, string_data_io)
        connection.connection.commit()

for url in pfx_data_collection.http_request_urls:
    time.sleep(1)
    page = parse(url)
    rows = page.xpath("body/table")[0].findall("tr")
    data = list()
    for row in rows:
            data.append([c.text for c in row.getchildren()])

    if len(data) == 1:
        continue
    else:
        pitcher_df = pd.DataFrame(data, columns = ["dateStamp", "park_sv_id", "play_guid",
        "ab_total", "ab_count", "pitcher_id", "batter_id", "ab_id", "des", "pitch_type",
        "pitch_id", "sz_top", "sz_bot", "pfx_xDataFile", "pfx_zDataFile", "mlbam_pitch_name",
        "zone_location", "pitch_con", "stand", "strikes", "balls", "p_throws", "gid",
        "pdes", "spin", "norm_ht", "inning", "pitcher_team", "tstart", "vystart",
        "ftime", "pfx_x", "pfx_z", "uncorrected_pfx_x", "uncorrected_pfx_z", "x0",
        "y0", "z0", "vx0", "vy0", "vz0", "ax", "ay", "az", "start_speed", "px",
        "pz", "pxold", "pzold", "tm_spin", "sb"])

        address = 'postgresql://@localhost:5432/pfxbaseballdata'
        engine = create_engine(address)
        write_to_table(pitcher_df, engine, 'new_pitch_game_data', "append")
