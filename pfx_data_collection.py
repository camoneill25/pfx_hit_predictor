import pandas as pd
import numpy as np

player_id_df = pd.read_csv('/Users/camerononeill/Developer/Baseball_Pitch_Predictor/player_id.csv', encoding = "ISO-8859-1")
schedule_df = pd.read_csv('/Users/camerononeill/Developer/Baseball_Pitch_Predictor/schedule_table.csv')

player_id_dct = dict()
for i in range(len(player_id_df)):
    player_id_dct[player_id_df.iloc[i]['mlb_id']] = player_id_df.iloc[i]['mlb_pos'], player_id_df.iloc[i]['mlb_team']

schedule_dct = dict()
for i in range(len(schedule_df)):
    for team in schedule_df.columns.values.tolist()[1::]:
        matchup = [team, schedule_df.iloc[i][team]]
        date = schedule_df.iloc[i]['Date']
        if date in schedule_dct and matchup[1] == matchup[1]:
            schedule_dct[date].append(matchup)
        elif date not in schedule_dct and matchup[1] == matchup[1]:
            schedule_dct[date] = [matchup]

web_address = "http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel=664641&game=gid_2017_04_06_seamlb_houmlb_1/&s_type=&h_size=700&v_size=500"

base_web_address_1 = "http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel="
base_web_address_2 = "&game="
base_web_address_3 = "/&s_type=&h_size=700&v_size=500"
http_request_urls = []
for date, teams in schedule_dct.items():
    month, day, year = date.split("/")
    for team in teams:
        for player_id, (position, player_team) in player_id_dct.items():
            if position == 'P' and (team[0] == player_team or team[1] == player_team):
                http_request_urls.append((base_web_address_1 + str(player_id) +
                base_web_address_2 +
                "gid_{:04}_{:02}_{:02}_{}mlb_{}mlb_{}".format(int(2017), int(month), int(day), team[1].lower(), team[0].lower(), 1) +
                base_web_address_3))
