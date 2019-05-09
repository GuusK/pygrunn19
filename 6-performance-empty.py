# $ python -X importtime 6-performance-empty.py
# import time: self [us] | cumulative | imported package
# import time:       152 |        152 | zipimport
# import time:       605 |        605 | _frozen_importlib_external
# import time:        94 |         94 |     _codecs
# import time:      3600 |       3694 |   codecs
# import time:      1399 |       1399 |   encodings.aliases
# import time:      5445 |      10537 | encodings
# import time:       500 |        500 | encodings.utf_8
# import time:        87 |         87 | _signal
# import time:       650 |        650 | encodings.latin_1
# import time:        64 |         64 |     _abc
# import time:      3110 |       3174 |   abc
# import time:      1512 |       4686 | io
# import time:       180 |        180 |       _stat
# import time:      1686 |       1865 |     stat
# import time:       573 |        573 |       genericpath
# import time:      2970 |       3542 |     ntpath
# import time:      1567 |       1567 |     _collections_abc
# import time:      5055 |      12028 |   os
# import time:       622 |        622 |   _sitebuiltins
# import time:       106 |        106 |   _winapi
# import time:      1330 |       1330 |   sitecustomize
# import time:      6733 |      20817 | site