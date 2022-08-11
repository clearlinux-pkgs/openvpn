#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openvpn
Version  : 2.5.7
Release  : 25
URL      : https://github.com/OpenVPN/openvpn/archive/v2.5.7/openvpn-2.5.7.tar.gz
Source0  : https://github.com/OpenVPN/openvpn/archive/v2.5.7/openvpn-2.5.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: openvpn-bin = %{version}-%{release}
Requires: openvpn-config = %{version}-%{release}
Requires: openvpn-filemap = %{version}-%{release}
Requires: openvpn-lib = %{version}-%{release}
Requires: openvpn-license = %{version}-%{release}
Requires: openvpn-man = %{version}-%{release}
Requires: openvpn-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : iproute2
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libpkcs11-helper-1)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(lzo2)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : pypi-docutils
BuildRequires : sed

%description
OpenVPN -- A Secure tunneling daemon
you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2
as published by the Free Software Foundation.

%package bin
Summary: bin components for the openvpn package.
Group: Binaries
Requires: openvpn-config = %{version}-%{release}
Requires: openvpn-license = %{version}-%{release}
Requires: openvpn-services = %{version}-%{release}
Requires: openvpn-filemap = %{version}-%{release}

%description bin
bin components for the openvpn package.


%package config
Summary: config components for the openvpn package.
Group: Default

%description config
config components for the openvpn package.


%package dev
Summary: dev components for the openvpn package.
Group: Development
Requires: openvpn-lib = %{version}-%{release}
Requires: openvpn-bin = %{version}-%{release}
Provides: openvpn-devel = %{version}-%{release}
Requires: openvpn = %{version}-%{release}

%description dev
dev components for the openvpn package.


%package doc
Summary: doc components for the openvpn package.
Group: Documentation
Requires: openvpn-man = %{version}-%{release}

%description doc
doc components for the openvpn package.


%package filemap
Summary: filemap components for the openvpn package.
Group: Default

%description filemap
filemap components for the openvpn package.


%package lib
Summary: lib components for the openvpn package.
Group: Libraries
Requires: openvpn-license = %{version}-%{release}
Requires: openvpn-filemap = %{version}-%{release}

%description lib
lib components for the openvpn package.


%package license
Summary: license components for the openvpn package.
Group: Default

%description license
license components for the openvpn package.


%package man
Summary: man components for the openvpn package.
Group: Default

%description man
man components for the openvpn package.


%package services
Summary: services components for the openvpn package.
Group: Systemd services

%description services
services components for the openvpn package.


%prep
%setup -q -n openvpn-2.5.7
cd %{_builddir}/openvpn-2.5.7
pushd ..
cp -a openvpn-2.5.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656700429
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static --enable-iproute2 \
--enable-systemd \
SYSTEMD_UNIT_DIR=/usr/lib/systemd/system \
TMPFILES_DIR=/usr/lib/tmpfiles.d
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static --enable-iproute2 \
--enable-systemd \
SYSTEMD_UNIT_DIR=/usr/lib/systemd/system \
TMPFILES_DIR=/usr/lib/tmpfiles.d
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656700429
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openvpn
cp %{_builddir}/openvpn-2.5.7/COPYING %{buildroot}/usr/share/package-licenses/openvpn/6206f5c60a740675eeccce5d17b0533563b13dcb
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openvpn
/usr/share/clear/optimized-elf/bin*

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/openvpn.conf

%files dev
%defattr(-,root,root,-)
/usr/include/openvpn-msg.h
/usr/include/openvpn-plugin.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openvpn/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-openvpn

%files lib
%defattr(-,root,root,-)
/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so
/usr/lib64/openvpn/plugins/openvpn-plugin-down-root.so
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openvpn/6206f5c60a740675eeccce5d17b0533563b13dcb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/openvpn-examples.5
/usr/share/man/man8/openvpn.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/openvpn-client@.service
/usr/lib/systemd/system/openvpn-server@.service
