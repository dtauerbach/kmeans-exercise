#!/usr/bin/env python

import unittest
import kmeans

class KmeansTester(unittest.TestCase):

    def test_parse_json(self):
        res = kmeans.parse_json('testdata/test.json')
        expected = [{u'category': u'Merchandise & Supplies', u'merchant_city': u'EAST SETAUKET', u'name': u"BJ'S 011", u'merchant_phone': None, u'merchant_state': u'NY', u'coordinates': {u'lat': 40.9027901845628, u'lng': -73.0782184632683}, u'merchant_zip': u'11733', u'merchant_address': u'4000 NESCONSET HWY', u'amount': 50, u'date': u'2013-10-28', u'merchant_country': u'UNITED STATES', u'type': None}]
        self.assertEqual(res, expected)

    def test_get_features(self):
        res = kmeans.parse_json('testdata/test.json')
        self.assertEqual(kmeans.get_features(res),
                         [(40.9027901845628,
                           -73.0782184632683)])

    def test_assign_points_to_centers(self):
        a = kmeans.assign_points_to_clusters([(1,2),(1,2.1),(4,5),(4,5.1)], [(1,2), (4,5)])
        self.assertEqual(a, {0: [(1,2),(1,2.1)], 1: [(4,5),(4,5.1)]})


if __name__ == '__main__':
    unittest.main()
