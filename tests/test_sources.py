
import json
import unittest

from requests import Response
from unittest.mock import MagicMock, patch

from data_loaders.sources.espn_fantasy_football import EspnFantasyFootball


class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_espn_ff = EspnFantasyFootball(swid='test', espn_s2='test', league_id=123456)
        cls.mock_resp = MagicMock()
        cls.mock_resp.json.return_value = {'gameDetails': True}

    @patch('requests.get', side_effect=MagicMock())
    def test_get_new_url_view_data(self, mock_get):
        mock_get.side_effect = [self.mock_resp]
        test_new_url_data = self.test_espn_ff.get_view_data(year=2021, param='test')
        self.assertTrue(test_new_url_data['gameDetails'])

    @patch('requests.get', side_effect=MagicMock())
    def test_get_old_url_view_data(self, mock_get):
        self.mock_resp.json.return_value = [{'gameDetails': True}]
        mock_get.side_effect = [self.mock_resp]
        test_new_url_data = self.test_espn_ff.get_view_data(year=2013, param='test')
        self.assertTrue(test_new_url_data['gameDetails'])

if __name__ == '__main__':
    unittest.main()
