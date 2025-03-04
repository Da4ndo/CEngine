# Maintainer: Da4ndo <contact@da4ndo.com>

# This PKGBUILD is not a full PKGBUILD
# pkgver, source, and sha256sums are to be generated

pkgname=cengine
pkgver=0.1.0
pkgrel=1
arch=(x86_64)
license=(MIT)
url="https://github.com/Da4ndo/CEngine"
source=("https://github.com/Da4ndo/CEngine/releases/download/v${pkgver}/cengine-linux-x64")
sha256sums=('SKIP')  # Replace SKIP with actual checksum when available

package() {
  install -Dm755 "cengine-linux-x64" "$pkgdir/usr/bin/cengine"
}