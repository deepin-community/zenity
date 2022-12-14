#!/usr/bin/env python3

import os
import subprocess

prefix = os.environ.get('MESON_INSTALL_PREFIX', '/usr/local')
datadir = os.path.join(prefix, 'share')

# Packaging tools define DESTDIR and this isn't needed for them
if 'DESTDIR' not in os.environ:
    print('Updating icon cache...')
    icon_cache_dir = os.path.join(datadir, 'icons', 'hicolor')
    if not os.path.exists(icon_cache_dir):
        os.makedirs(icon_cache_dir)
    subprocess.call(['gtk-update-icon-cache', '-qtf', icon_cache_dir])
