#!/usr/bin/python

import tarfile
import time

# List of directories and files to backup
bk_src = ['C:/temp/src/']

# Directory where the backup will be stored
bk_dest = 'C:/temp/dest/'

bk_fn = bk_dest + time.strftime('%Y%m%d%H%M%S') + '.tgz'
zip_cmd = "zip -qr '%s' %s" % (bk_fn, ' '.join(bk_src))

tar_file = tarfile.open(bk_fn, 'w:gz')
for file in bk_src:
    tar_file.add(file)
tar_file.close()
