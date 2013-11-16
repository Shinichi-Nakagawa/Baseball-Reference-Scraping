#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Baseball Reference Reader Unit Test
"""

import unittest
from baseball_reference_reader import BaseballReferenceReader
from baseball_reference_reader import SABRmetrics


class TestBaseballReferenceReader(unittest.TestCase):

    def setUp(self):
        self.br = BaseballReferenceReader()

    def tearDown(self):
        self.br = None

    def test_batter_pujols_2010(self):
        """
        プホルス2010
        """
        query_name = "Albert Pujols"
        position = "b"
        year = "2010"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Jose Alberto Pujols(Prince Albert, Phat Albert or The Machine)\n (twitter:@PujolsFive)")
        self.assertEqual(stats["Year"], "2010")
        self.assertEqual(stats["Age"], "30")
        self.assertEqual(stats["Team"], "STL")
        self.assertEqual(stats["League"], "NL")
        self.assertEqual(stats["G"], "159")
        self.assertEqual(stats["PA"], "700")
        self.assertEqual(stats["AB"], "587")
        self.assertEqual(stats["R"], "115")
        self.assertEqual(stats["H"], "183")
        self.assertEqual(stats["2B"], "39")
        self.assertEqual(stats["3B"], "1")
        self.assertEqual(stats["HR"], "42")
        self.assertEqual(stats["RBI"], "118")
        self.assertEqual(stats["SB"], "14")
        self.assertEqual(stats["CS"], "4")
        self.assertEqual(stats["BB"], "103")
        self.assertEqual(stats["SO"], "76")
        self.assertEqual(stats["BA"], ".312")
        self.assertEqual(stats["OBP"], ".414")
        self.assertEqual(stats["SLG"], ".596")
        self.assertEqual(stats["OPS"], "1.011")
        self.assertEqual(stats["OPS+"], "173")
        self.assertEqual(stats["TB"], "350")
        self.assertEqual(stats["GDP"], "23")
        self.assertEqual(stats["HBP"], "4")
        self.assertEqual(stats["SH"], "0")
        self.assertEqual(stats["SF"], "6")
        self.assertEqual(stats["IBB"], "38")
        self.assertEqual(stats["Pos"], "*3")
        self.assertEqual(stats["Awards"], "AS,MVP-2,GG,SS")

    def test_batter_ichiro_2001(self):
        """
        イチローの2001年成績
        """
        query_name = "Ichiro Suzuki"
        position = "b"
        year = "2001"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Ichiro Suzuki(Wizard)")
        self.assertEqual(stats["Year"], "2001")
        self.assertEqual(stats["Age"], "27")
        self.assertEqual(stats["Team"], "SEA")
        self.assertEqual(stats["League"], "AL")
        self.assertEqual(stats["G"], "157")
        self.assertEqual(stats["PA"], "738")
        self.assertEqual(stats["AB"], "692")
        self.assertEqual(stats["R"], "127")
        self.assertEqual(stats["H"], "242")
        self.assertEqual(stats["2B"], "34")
        self.assertEqual(stats["3B"], "8")
        self.assertEqual(stats["HR"], "8")
        self.assertEqual(stats["RBI"], "69")
        self.assertEqual(stats["SB"], "56")
        self.assertEqual(stats["CS"], "14")
        self.assertEqual(stats["BB"], "30")
        self.assertEqual(stats["SO"], "53")
        self.assertEqual(stats["BA"], ".350")
        self.assertEqual(stats["OBP"], ".381")
        self.assertEqual(stats["SLG"], ".457")
        self.assertEqual(stats["OPS"], ".838")
        self.assertEqual(stats["OPS+"], "126")
        self.assertEqual(stats["TB"], "316")
        self.assertEqual(stats["GDP"], "3")
        self.assertEqual(stats["HBP"], "8")
        self.assertEqual(stats["SH"], "4")
        self.assertEqual(stats["SF"], "4")
        self.assertEqual(stats["IBB"], "10")
        self.assertEqual(stats["Pos"], "*9/D")
        self.assertEqual(stats["Awards"], "AS,MVP-1,RoY-1,GG,SS")

    def test_pitcher_darvish_2012(self):
        """
        ダルビッシュ有2012
        """
        query_name = "Yu Darvish"
        position = "p"
        year = "2012"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Sefat Farid Yu Darvish(twitter:@faridyu)")
        self.assertEqual(stats["Year"], "2012")
        self.assertEqual(stats["Age"], "25")
        self.assertEqual(stats["Team"], "TEX")
        self.assertEqual(stats["League"], "AL")
        self.assertEqual(stats["W"], "16")
        self.assertEqual(stats["L"], "9")
        self.assertEqual(stats["W-L%"], ".640")
        self.assertEqual(stats["ERA"], "3.90")
        self.assertEqual(stats["G"], "29")
        self.assertEqual(stats["GS"], "29")
        self.assertEqual(stats["GF"], "0")
        self.assertEqual(stats["CG"], "0")
        self.assertEqual(stats["SHO"], "0")
        self.assertEqual(stats["SV"], "0")
        self.assertEqual(stats["IP"], "191.1")
        self.assertEqual(stats["H"], "156")
        self.assertEqual(stats["R"], "89")
        self.assertEqual(stats["ER"], "83")
        self.assertEqual(stats["HR"], "14")
        self.assertEqual(stats["BB"], "89")
        self.assertEqual(stats["IBB"], "1")
        self.assertEqual(stats["SO"], "221")
        self.assertEqual(stats["HBP"], "10")
        self.assertEqual(stats["BK"], "0")
        self.assertEqual(stats["WP"], "8")
        self.assertEqual(stats["BF"], "816")
        self.assertEqual(stats["ERA+"], "112")
        self.assertEqual(stats["WHIP"], "1.280")
        self.assertEqual(stats["H9"], "7.3")
        self.assertEqual(stats["HR9"], "0.7")
        self.assertEqual(stats["BB9"], "4.2")
        self.assertEqual(stats["SO9"], "10.4")
        self.assertEqual(stats["SOBB"], "2.48")
        self.assertEqual(stats["Awards"], "AS,CYA-9,RoY-3")

    def test_pitcher_balfour_2011(self):
        """
        グラント・バルフォア2011
        """
        query_name = "grant balfour"
        position = "p"
        year = "2011"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Grant Robert Balfour")
        self.assertEqual(stats["Year"], "2011")
        self.assertEqual(stats["Age"], "33")
        self.assertEqual(stats["Team"], "OAK")
        self.assertEqual(stats["League"], "AL")
        self.assertEqual(stats["W"], "5")
        self.assertEqual(stats["L"], "2")
        self.assertEqual(stats["W-L%"], ".714")
        self.assertEqual(stats["ERA"], "2.47")
        self.assertEqual(stats["G"], "62")
        self.assertEqual(stats["GS"], "0")
        self.assertEqual(stats["GF"], "15")
        self.assertEqual(stats["CG"], "0")
        self.assertEqual(stats["SHO"], "0")
        self.assertEqual(stats["SV"], "2")
        self.assertEqual(stats["IP"], "62.0")
        self.assertEqual(stats["H"], "44")
        self.assertEqual(stats["R"], "17")
        self.assertEqual(stats["ER"], "17")
        self.assertEqual(stats["HR"], "8")
        self.assertEqual(stats["BB"], "20")
        self.assertEqual(stats["IBB"], "1")
        self.assertEqual(stats["SO"], "59")
        self.assertEqual(stats["HBP"], "0")
        self.assertEqual(stats["BK"], "0")
        self.assertEqual(stats["WP"], "0")
        self.assertEqual(stats["BF"], "242")
        self.assertEqual(stats["ERA+"], "163")
        self.assertEqual(stats["WHIP"], "1.032")
        self.assertEqual(stats["H9"], "6.4")
        self.assertEqual(stats["HR9"], "1.2")
        self.assertEqual(stats["BB9"], "2.9")
        self.assertEqual(stats["SO9"], "8.6")
        self.assertEqual(stats["SOBB"], "2.95")
        self.assertEqual(stats["Awards"], "")

    def test_pitcher_kimbrel_2012(self):
        """
        クレイグ・キンブレル2012
        """
        query_name = "CRAIG KIMBREL"
        position = "p"
        year = "2012"
        name, stats = self.br.get_player_stats(query_name, position, year)
        self.assertEqual(name, "Craig Michael Kimbrel(twitter:@kimbrel46)")
        self.assertEqual(stats["Year"], "2012")
        self.assertEqual(stats["Age"], "24")
        self.assertEqual(stats["Team"], "ATL")
        self.assertEqual(stats["League"], "NL")
        self.assertEqual(stats["W"], "3")
        self.assertEqual(stats["L"], "1")
        self.assertEqual(stats["W-L%"], ".750")
        self.assertEqual(stats["ERA"], "1.01")
        self.assertEqual(stats["G"], "63")
        self.assertEqual(stats["GS"], "0")
        self.assertEqual(stats["GF"], "56")
        self.assertEqual(stats["CG"], "0")
        self.assertEqual(stats["SHO"], "0")
        self.assertEqual(stats["SV"], "42")
        self.assertEqual(stats["IP"], "62.2")
        self.assertEqual(stats["H"], "27")
        self.assertEqual(stats["R"], "7")
        self.assertEqual(stats["ER"], "7")
        self.assertEqual(stats["HR"], "3")
        self.assertEqual(stats["BB"], "14")
        self.assertEqual(stats["IBB"], "0")
        self.assertEqual(stats["SO"], "116")
        self.assertEqual(stats["HBP"], "2")
        self.assertEqual(stats["BK"], "0")
        self.assertEqual(stats["WP"], "5")
        self.assertEqual(stats["BF"], "231")
        self.assertEqual(stats["ERA+"], "399")
        self.assertEqual(stats["WHIP"], "0.654")
        self.assertEqual(stats["H9"], "3.9")
        self.assertEqual(stats["HR9"], "0.4")
        self.assertEqual(stats["BB9"], "2.0")
        self.assertEqual(stats["SO9"], "16.7")
        self.assertEqual(stats["SOBB"], "8.29")
        self.assertEqual(stats["Awards"], "AS,CYA-5,MVP-8")

    def test_batter_adam_dunn_2012(self):
        """
        アダム・ダンのアダム・ダン率2012シーズン
        """
        query_name = "Adam Dunn"
        position = "b"
        year = "2012"
        name, stats = self.br.get_player_stats(query_name, position, year)
        dunn = SABRmetrics.calc_adam_dunn_percent(stats)
        self.assertEqual(dunn, 56.7)

    def test_pitcher_adam_dunn_2013(self):
        """
        岩隈久志のアダム・ダン率2013シーズン
        """
        query_name = "Hisashi Iwakuma"
        position = "p"
        year = "2013"
        name, stats = self.br.get_player_stats(query_name, position, year)
        dunn = SABRmetrics.calc_adam_dunn_percent_pitcher(stats)
        self.assertEqual(dunn, 29.3)


if __name__ == '__main__':
    unittest.main()
