#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Baseball Reference Reader
"""

import urllib
from BeautifulSoup import BeautifulSoup
import re
import itertools
from string import ascii_letters
import sys


class BaseballReferenceReader(object):

    PLAYERS_NAME_DELI = " "
    PLAYERS_PAGE_URL = 'http://www.baseball-reference.com/players/%(letter)s/'

    STANDARD_BATTING_COLUMNS = (
        'Year',
        'Age',
        'Team',
        'League',
        'G',
        'PA',
        'AB',
        'R',
        'H',
        '2B',
        '3B',
        'HR',
        'RBI',
        'SB',
        'CS',
        'BB',
        'SO',
        'BA',
        'OBP',
        'SLG',
        'OPS',
        'OPS+',
        'TB',
        'GDP',
        'HBP',
        'SH',
        'SF',
        'IBB',
        'Pos',
        'Awards'
    )

    STANDARD_PITCHING_COLUMNS = (
        'Year',
        'Age',
        'Team',
        'League',
        'Win',
        'Lose',
        'W-L%',
        'ERA',
        'G',
        'GS',
        'GF',
        'CG',
        'SHO',
        'SV',
        'IP',
        'H',
        'R',
        'ER',
        'HR',
        'BB',
        'IBB',
        'SO',
        'HBP',
        'BK',
        'WP',
        'BF',
        'ERA+',
        'WHIP',
        'H9',
        'BB9',
        'SO9',
        'SOBB',
        'Awards'
    )

    PITCHING_STANDARD_RE = 'pitching_standard\.((18|19|20)[0-9]{2})'

    BATTING_STANDARD_RE = 'batting_standard\.((18|19|20)[0-9]{2})'

    PITCHING_STANDARD_TABLE = "pitching_standard"

    BATTING_STANDARD_TABLE = "batting_standard"

    POSITION_PITCHER = "p"

    POSITION_BATTER = "b"

    def __init__(self,):
        """
        Initialize
        """
        pass

    def _stats_from_soup(self, soup, stats_re, columns, table_id):
        """
        Get Player Stats from Soup
        """
        _table = self._find_standard_table(soup, table_id)
        if _table:
            stats = self._decompose_table(_table, stats_re, columns)
            return stats

    def _find_standard_table(self, soup, table_id):
        """
        Find Standard Table from Soup
        """
        for table in soup.findAll('table'):
            try:
                if table['id'] == table_id:
                    return table
            except KeyError:
                '''table does not have an "id" attribute, oh-well, the
                table we're looking for does'''
                pass

    def _decompose_table(self, table, stats_re, columns):
        """
        Stats List from Table
        """
        stats = []
        _table_body = table.findAll('tbody')[0]
        for table_row in _table_body.findAll('tr'):
            table_row_id = table_row.get('id')
            if not table_row_id:
                continue
            year = re.findall(stats_re, table_row_id)
            row_values = {}
            values = [element.text for element in table_row.findAll('td')]
            my_keys_with_values = zip(columns, values)
            row_values = dict(my_keys_with_values)

            stats.append(row_values)
        return stats

    def _link_to_url(self, link_element, domain='baseball-reference.com'):
        """
        Link => URL
        """
        href = filter(lambda attr: attr[0] == 'href', link_element.attrs)[0][1]
        return ''.join(('http://', domain, href))

    def _player_page_links(self, players_page_url):
        """
        Get Player Page Link for Player Name & URL
        """
        f = urllib.urlopen(players_page_url)
        soup = BeautifulSoup(''.join(f))
        page_content = soup.findAll('div', id='page_content')[0]
        player_blocks = page_content.findAll('blockquote')
        link_elements = (
            player_block.findAll('a') for player_block in player_blocks
        )
        link_elements = itertools.chain(*link_elements)

        for link_element in link_elements:
            player_name = link_element.text
            player_page_url = self._link_to_url(link_element)
            yield player_name, player_page_url

    def _get_player_page_links(self, letter):
        """
        Get Player Page Links
        """
        players_page_url = self.PLAYERS_PAGE_URL % {'letter': letter}
        return self._player_page_links(players_page_url)

    def get_player_name_and_url(self, name):
        """
        Get Player Name & Base Url
        """
        _lower_name = name.lower()
        first_name, middle_name = _lower_name.split(self.PLAYERS_NAME_DELI)
        letter = middle_name[:1]
        names_w_links = self._get_player_page_links(letter)
        for player_name, player_page_url in names_w_links:
            if player_name.lower() == _lower_name:
                return player_name, player_page_url

    def url_to_beautiful_soup(self, url):
        """
        URL => SOUP Object
        """
        url = urllib.urlopen(url)
        soup = BeautifulSoup(''.join(url.readlines()))
        return soup

    def long_player_name_from_soup(self, soup):
        """
        Get Long Player Name from SOUP Object
        """
        info_box = soup.findAll('div', id='info_box')[0]
        info_table = info_box.findAll('table')
        if info_table:
            long_name_element = info_table[0].findAll('p')[1]
        else:
            long_name_element = info_box.findAll('p')[0]
        return long_name_element.text

    def stats_from_soup(self, soup, position):
        """
        Get Player Stats from SOUP Object
        """
        stats_re, columns, table_id = "", [], ""
        if position == self.POSITION_PITCHER:
            stats_re = self.PITCHING_STANDARD_RE
            columns = self.STANDARD_PITCHING_COLUMNS
            table_id = self.PITCHING_STANDARD_TABLE
        elif position == self.POSITION_BATTER:
            stats_re = self.BATTING_STANDARD_RE
            columns = self.STANDARD_BATTING_COLUMNS
            table_id = self.BATTING_STANDARD_TABLE
        else:
            print "Don't Care Position: %s " % position
            return []
        return self._stats_from_soup(soup, stats_re, columns, table_id)

    def get_player_stats(self, name, position):
        """
        Get Player Name & Stats
        """
        long_player_name, stats = "", []
        player_name, player_page_url = self.get_player_name_and_url(name)
        soup = self.url_to_beautiful_soup(player_page_url)
        long_player_name = self.long_player_name_from_soup(soup)
        stats = self.stats_from_soup(soup, position)
        return long_player_name, stats


class BaseballReferenceParsingException(Exception):
    def __init__(self, value):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)


def main(args):
    br = BaseballReferenceReader()
    name, stats = br.get_player_stats(args.name, args.position)
    print "Player Name: %s" % name
    for stat in stats:
        if stat["Year"] == str(args.year):
            for key in stat.keys():
                print "%s : %s" % (key, stat[key])


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(
        description='Baseball Reference'
    )
    parser.add_argument(
        '-n',
        '--name',
        required=True,
        help="Player Name(ex. Ichiro Suzuki)"
    )
    parser.add_argument(
        '-p',
        '--position',
        required=True,
        help="position(p:pitcher b:batter)"
    )
    parser.add_argument(
        '-y',
        '--year',
        required=True,
        help="Stats Year"
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0'
    )
    args = parser.parse_args()
    sys.exit(main(args))
