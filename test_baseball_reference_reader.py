#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Baseball Reference Reader Unit Test
"""

import unittest
from baseball_reference_reader import BaseballReferenceReader


class TestBaseballReferenceReader(unittest.TestCase):

    def setUp(self):
        self.br = BaseballReferenceReader()

    def tearDown(self):
        self.br = None

    def test_batter_ichiro_2001(self):
        """
        イチローの2001年成績
        """
        query_name = "Ichiro Suzuki"
        position = "b"
        year = "2001"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Ichiro Suzuki(Wizard)")
        stats_2001 = stats
        self.assertEqual(stats_2001["Year"], "2001")
        self.assertEqual(stats_2001["Age"], "27")
        self.assertEqual(stats_2001["Team"], "SEA")
        self.assertEqual(stats_2001["League"], "AL")
        self.assertEqual(stats_2001["G"], "157")
        self.assertEqual(stats_2001["PA"], "738")
        self.assertEqual(stats_2001["AB"], "692")
        self.assertEqual(stats_2001["R"], "127")
        self.assertEqual(stats_2001["H"], "242")
        self.assertEqual(stats_2001["2B"], "34")
        self.assertEqual(stats_2001["3B"], "8")
        self.assertEqual(stats_2001["HR"], "8")
        self.assertEqual(stats_2001["RBI"], "69")
        self.assertEqual(stats_2001["SB"], "56")
        self.assertEqual(stats_2001["CS"], "14")
        self.assertEqual(stats_2001["BB"], "30")
        self.assertEqual(stats_2001["SO"], "53")
        self.assertEqual(stats_2001["BA"], ".350")
        self.assertEqual(stats_2001["OBP"], ".381")
        self.assertEqual(stats_2001["SLG"], ".457")
        self.assertEqual(stats_2001["OPS"], ".838")
        self.assertEqual(stats_2001["OPS+"], "126")
        self.assertEqual(stats_2001["TB"], "316")
        self.assertEqual(stats_2001["GDP"], "3")
        self.assertEqual(stats_2001["HBP"], "8")
        self.assertEqual(stats_2001["SH"], "4")
        self.assertEqual(stats_2001["SF"], "4")
        self.assertEqual(stats_2001["IBB"], "10")
        self.assertEqual(stats_2001["Pos"], "*9/D")
        self.assertEqual(stats_2001["Awards"], "AS,MVP-1,RoY-1,GG,SS")

    def test_pitcher_darvish_2012(self):
        """
        ダルビッシュ有2012
        """
        query_name = "Yu Darvish"
        position = "p"
        year = "2012"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Sefat Farid Yu Darvish(twitter:@faridyu)")
        stats_2012 = stats
        self.assertEqual(stats_2012["Year"], "2012")
        self.assertEqual(stats_2012["Age"], "25")
        self.assertEqual(stats_2012["Team"], "TEX")
        self.assertEqual(stats_2012["League"], "AL")
        self.assertEqual(stats_2012["W"], "16")
        self.assertEqual(stats_2012["L"], "9")
        self.assertEqual(stats_2012["W-L%"], ".640")
        self.assertEqual(stats_2012["ERA"], "3.90")
        self.assertEqual(stats_2012["G"], "29")
        self.assertEqual(stats_2012["GS"], "29")
        self.assertEqual(stats_2012["GF"], "0")
        self.assertEqual(stats_2012["CG"], "0")
        self.assertEqual(stats_2012["SHO"], "0")
        self.assertEqual(stats_2012["SV"], "0")
        self.assertEqual(stats_2012["IP"], "191.1")
        self.assertEqual(stats_2012["H"], "156")
        self.assertEqual(stats_2012["R"], "89")
        self.assertEqual(stats_2012["ER"], "83")
        self.assertEqual(stats_2012["HR"], "14")
        self.assertEqual(stats_2012["BB"], "89")
        self.assertEqual(stats_2012["IBB"], "1")
        self.assertEqual(stats_2012["SO"], "221")
        self.assertEqual(stats_2012["HBP"], "10")
        self.assertEqual(stats_2012["BK"], "0")
        self.assertEqual(stats_2012["WP"], "8")
        self.assertEqual(stats_2012["BF"], "816")
        self.assertEqual(stats_2012["ERA+"], "112")
        self.assertEqual(stats_2012["WHIP"], "1.280")
        self.assertEqual(stats_2012["H9"], "7.3")
        self.assertEqual(stats_2012["HR9"], "0.7")
        self.assertEqual(stats_2012["BB9"], "4.2")
        self.assertEqual(stats_2012["SO9"], "10.4")
        self.assertEqual(stats_2012["SOBB"], "2.48")
        self.assertEqual(stats_2012["Awards"], "AS,CYA-9,RoY-3")

if __name__ == '__main__':
    unittest.main()
