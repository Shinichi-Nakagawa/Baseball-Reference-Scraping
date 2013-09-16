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

    def test_batter(self):
        """
        イチローの2001年成績
        """
        query_name = "Ichiro Suzuki"
        position = "b"
        name, stats = self.br.get_player_stats(query_name, position)
        self.assertEqual(name, "Ichiro Suzuki(Wizard)")
        #self.assertEqual(len(stats), 15)
        #print name
        stats_2001 = stats[0]
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


if __name__ == '__main__':
    unittest.main()
