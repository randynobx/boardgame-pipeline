'''Tests for BoardGameGeek XMLAPI2 helper functions'''

import re
from dags.py import bggxmlapi2 as api


def test_build_query():
    '''Test build_query() for single id'''
    qtype = 'thing'
    test_params = {
        'id': 224517,
        'stats': 1,
        'type': 'boardgames'
    }
    exp_url = 'https://boardgamegeek.com/xmlapi2/thing?id=224517&stats=1&type=boardgames'
    test_query_url = api.build_query(qtype, test_params)
    assert isinstance(test_query_url, str), 'Did not return a string'
    assert test_query_url == exp_url


def test_build_query_batch():
    '''Test build_query() for mulitple ids'''
    qtype = 'thing'
    test_params = {
        'id': '224517,160010,150',
        'stats': 1,
        'type': 'boardgames'
    }
    exp_url = 'https://boardgamegeek.com/xmlapi2/thing?id=224517,160010,150&stats=1&type=boardgames'
    test_query_url = api.build_query(qtype, test_params)
    assert isinstance(test_query_url, str), 'Did not return a string'
    assert test_query_url == exp_url


def test_fetch_game():
    '''Test fetch game for single id'''
    test_id = 224517
    text = api.fetch_game(test_id)
    assert isinstance(text, str), 'Did not return a str'
    ans_item = r'<item type="boardgame" id="224517">'
    pattern = re.compile(ans_item)
    test_item = re.search(pattern, str(text))[0]
    assert test_item == ans_item, f'Wrong item returned. Received {test_item}'


def test_fetch_game_batch():
    '''Test fetch game for multiple ids'''
    test_id = '224517,160010,150'
    text = api.fetch_game(test_id)
    assert isinstance(text, str), 'Did not return a str'
    pattern =  re.compile(r'<item type="boardgame" id="\d+">')
    items_search = re.findall(pattern, str(text))
    assert len(items_search) == 3
