# -*- encoding: utf-8
# yapf: disable


checkname = 'ceph_df'


info = [[u'GLOBAL:'],
        [u'SIZE', u'AVAIL', u'RAW', u'USED', u'%RAW', u'USED', u'OBJECTS'],
        [u'253', u'GiB', u'245', u'GiB', u'7.8', u'GiB', u'3.10', u'839'],
        [u'POOLS:'],
        [u'NAME',
         u'ID',
         u'QUOTA',
         u'OBJECTS',
         u'QUOTA',
         u'BYTES',
         u'USED',
         u'%USED',
         u'MAX',
         u'AVAIL',
         u'OBJECTS',
         u'DIRTY',
         u'READ',
         u'WRITE',
         u'RAW',
         u'USED'],
        [u'cephfs_data',
         u'1',
         u'N/A',
         u'N/A',
         u'1.6',
         u'GiB',
         u'1.97',
         u'77',
         u'GiB',
         u'809',
         u'809',
         u'33',
         u'B',
         u'177',
         u'KiB',
         u'4.7',
         u'GiB'],
        [u'cephfs_metadata',
         u'2',
         u'N/A',
         u'N/A',
         u'32',
         u'MiB',
         u'0.04',
         u'77',
         u'GiB',
         u'30',
         u'30',
         u'407',
         u'B',
         u'14',
         u'KiB',
         u'95',
         u'MiB']]


discovery = {'': [('SUMMARY', {}), (u'cephfs_data', {}), (u'cephfs_metadata', {})]}


checks = {'': [('SUMMARY',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '3.16% used (8 of 253 GB), trend: 0 B / 24 hours',
                  [('SUMMARY', 8192.0, 207257.6, 233164.8, 0, 259072.0),
                   ('fs_size', 259072.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10794.666666666666)])]),
               (u'cephfs_data',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '2.04% used (1.6 of 78.6 GB), trend: 0 B / 24 hours',
                  [(u'cephfs_data',
                    1638.3999999999942,
                    64389.12,
                    72437.76,
                    0,
                    80486.4),
                   ('fs_size', 80486.4, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 3353.6)])]),
               (u'cephfs_metadata',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.04% used (32 MB of 77.03 GB), trend: 0 B / 24 hours',
                  [(u'cephfs_metadata', 32.0, 63104.0, 70992.0, 0, 78880.0),
                   ('fs_size', 78880.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 3286.6666666666665)])])]}
