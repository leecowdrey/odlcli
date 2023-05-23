#!/bin/bash
VERSION=$(grep CLI_VERSION odlcli/usr/bin/odlcli|cut -d'"' -f2)
git tag ${VERSION}
git push origin --tags
#git pull
dpkg-deb --nocheck --build odlcli
[[ ! -d dists/debian/amd64 ]] && mkdir -p dists/debian/amd64
[[ ! -d dists/rhel/noarch ]] && mkdir -p dists/rhel/noarch
mv -f odlcli.deb dists/debian/amd64/odlcli-${VERSION}_amd64.deb
sudo alien --to-rpm dists/debian/amd64/odlcli-${VERSION}_amd64.deb
mv -f odlcli-${VERSION}-?.noarch.rpm dists/rhel/noarch/
git add dists/debian/amd64/odlcli-${VERSION}_amd64.deb
git add dists/rhel/noarch/odlcli-${VERSION}-?.noarch.rpm
git commit -m "lee@cowdrey.net: "
git push
