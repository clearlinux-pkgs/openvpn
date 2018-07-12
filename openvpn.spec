#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD72AF3448CC2B034 (security@openvpn.net)
#
Name     : openvpn
Version  : 2.4.4
Release  : 7
URL      : https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.xz
Source0  : https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.xz
Source99 : https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: openvpn-bin
Requires: openvpn-config
Requires: openvpn-lib
Requires: openvpn-license
Requires: openvpn-man
BuildRequires : Linux-PAM-dev
BuildRequires : cmake
BuildRequires : iproute2
BuildRequires : lz4-dev
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libpkcs11-helper-1)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(lzo2)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : sed

%description
OpenVPN is a robust and highly flexible VPN daemon by James Yonan.
OpenVPN supports SSL/TLS security,
ethernet bridging,
TCP or UDP tunnel transport through proxies or NAT,
support for dynamic IP addresses and DHCP,
scalability to hundreds or thousands of users,
and portability to most major OS platforms.

%package bin
Summary: bin components for the openvpn package.
Group: Binaries
Requires: openvpn-config
Requires: openvpn-license
Requires: openvpn-man

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
Requires: openvpn-lib
Requires: openvpn-bin
Provides: openvpn-devel

%description dev
dev components for the openvpn package.


%package doc
Summary: doc components for the openvpn package.
Group: Documentation
Requires: openvpn-man

%description doc
doc components for the openvpn package.


%package lib
Summary: lib components for the openvpn package.
Group: Libraries
Requires: openvpn-license

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


%prep
%setup -q -n openvpn-2.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531430833
%configure --disable-static --enable-iproute2 \
--enable-systemd \
SYSTEMD_UNIT_DIR=/usr/lib/systemd/system \
TMPFILES_DIR=/usr/lib/tmpfiles.d
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1531430833
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openvpn
cp COPYING %{buildroot}/usr/share/doc/openvpn/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openvpn

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/openvpn-client@.service
/usr/lib/systemd/system/openvpn-server@.service
/usr/lib/tmpfiles.d/openvpn.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openvpn/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so
/usr/lib64/openvpn/plugins/openvpn-plugin-down-root.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/openvpn/COPYING
/usr/share/doc/openvpn/COPYRIGHT.GPL

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/openvpn.8
