
import json
import unittest

from requests import Response
from unittest.mock import MagicMock, patch

from data_loaders.sources.espn_fantasy_football import EspnFantasyFootball


class SourcesTests(unittest.TestCase):

    mock_resp = MagicMock()
    mock_resp.json.return_value = json.dumps({'firstname': 'John', 'lastname': 'Doe'})

    @patch('requests.get', side_effect=[mock_resp])
    def test_espn_fantasy_football(self, mock_request):
        source = EspnFantasyFootball()
        print(source.get_view_data(2019, 'mTeam'))

if __name__ == '__main__':
    unittest.main()
