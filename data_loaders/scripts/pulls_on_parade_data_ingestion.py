# postgres has been installed
# need to examine the api schema and figure out the correct db layout

from json import dumps
from os import environ, path

from yaml import load, FullLoader

from data_loaders.sources.espn_fantasy_football import EspnFantasyFootball

config_f    = open(environ['CONFIG_LOC'], 'r')
config_data = load(config_f, Loader=FullLoader)

espn_fantasy_football = EspnFantasyFootball(swid=config_data['swid'], espn_s2=config_data['espn_s2'], league_id=config_data['league_id'])

views = ['mSettings', 'mRoster', 'mStandings', 'mMatchup', 'mMatchupScore', 'mScoreboard', 'mStatus', 'mPendingTransactions', 'mLiveScoring', 'mPositionalRatings']

for view in views:
    for year in range(2013, 2023):
        data = espn_fantasy_football.get_view_data(year, view)
        with open(path.join(config_data['backup_locs']['pulls_on_parade'], '{}_dump_{}.txt'.format(view, year)), 'w') as f:
            f.write(dumps(data, indent=4))
