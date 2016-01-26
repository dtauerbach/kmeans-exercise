#!/usr/bin/env python

import unittest
import kmeans

class KmeansTester(unittest.TestCase):

    def setUp(self):
        self.test_data_expected = [{u'category': u'Merchandise & Supplies',
                                    u'merchant_city': u'EAST SETAUKET',
                                    u'name': u"BJ'S 011",
                                    u'merchant_phone': None,
                                    u'merchant_state': u'NY',
                                    u'coordinates':  {u'lat': 40.9027901845628, u'lng': -73.0782184632683},
                                    u'merchant_zip': u'11733',
                                    u'merchant_address': u'4000 NESCONSET HWY',
                                    u'amount': 50,
                                    u'date': u'2013-10-28',
                                    u'merchant_country': u'UNITED STATES',
                                    u'type': None}]

        self.test_points = [(1,2),(1,2.1),(4,5),(4,5.1)]
        self.three_cluster_test_points = [(1,2),(1,2.1),(77,1.1), (1,2.2),(4,5),
                                          (4,5.1),(4,5.2),(77,1), (69,4)]
        self.test_cluster = [(1,2),(1,2.1)]
        self.test_centers = [(1,2),(4,5)]

    def test_parse_json(self):
        res = kmeans.parse_json('testdata/test.json')
        expected = self.test_data_expected
        self.assertEqual(res, expected)

    def test_get_features(self):
        res = kmeans.parse_json('testdata/test.json')
        self.assertEqual(kmeans.get_features(res),
                         [(40.9027901845628,
                           -73.0782184632683)])

    def test_assign_points_to_centers(self):
        a = kmeans.assign_points_to_clusters(self.test_points,
                                             self.test_centers)
        self.assertEqual(a, {0: [(1,2),(1,2.1)], 1: [(4,5),(4,5.1)]})

    def test_update_center(self):
        a = kmeans.update_center(self.test_cluster)
        self.assertEqual(a, (1,2.05))


    def test_apply_lloyd_two(self):
        a = kmeans.apply_lloyd(self.test_points, 2)
        self.assertIn([(1,2),(1,2.1)], a.values())
        self.assertIn([(4,5),(4,5.1)], a.values())

    def test_apply_lloyd_three(self):
        a = kmeans.apply_lloyd(self.three_cluster_test_points, 3)
        self.assertIn([(1,2),(1,2.1),(1,2.2)], a.values())


if __name__ == '__main__':
    unittest.main()
