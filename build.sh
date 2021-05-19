#!/bin/bash
#git pull
dpkg-deb --nocheck --build odlcli
mv -f odlcli.deb dists/debian/amd64/odlcli-1.0.4_amd64.deb
sudo alien --to-rpm dists/debian/amd64/odlcli-1.0.4_amd64.deb
mv -f odlcli-1.0.?-?.noarch.rpm dists/rhel/noarch/
git add dists/debian/amd64/odlcli-1.0.4_amd64.deb
git add dists/rhel/noarch/odlcli-1.0.?-?.noarch.rpm
git commit -m "lee@cowdrey.co.uk: "
git push
