# postgres has been installed
# need to examine the api schema and figure out the correct db layout

from os import environ

from yaml import load, FullLoader

from data_loaders.sources.espn_fantasy_football import EspnFantasyFootball

config_f    = open(environ['CONFIG_LOC'], 'r')
config_data = load(config_f, Loader=FullLoader)

espn_fantasy_football = EspnFantasyFootball(swid=config_data['swid'], espn_s2=config_data['espn_s2'], league_id=config_data['league_id'])

data = espn_fantasy_football.get_view_data(2022, 'mTeam')

for k in data.keys():
    print(type(data[k]))
