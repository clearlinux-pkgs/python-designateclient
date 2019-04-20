#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-designateclient
Version  : 2.11.0
Release  : 33
URL      : http://tarballs.openstack.org/python-designateclient/python-designateclient-2.11.0.tar.gz
Source0  : http://tarballs.openstack.org/python-designateclient/python-designateclient-2.11.0.tar.gz
Source99 : http://tarballs.openstack.org/python-designateclient/python-designateclient-2.11.0.tar.gz.asc
Summary  : Python client library for Designate
Group    : Development/Tools
License  : Apache-2.0
Requires: python-designateclient-bin = %{version}-%{release}
Requires: python-designateclient-license = %{version}-%{release}
Requires: python-designateclient-python = %{version}-%{release}
Requires: python-designateclient-python3 = %{version}-%{release}
Requires: cliff
Requires: debtcollector
Requires: jsonschema
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-designateclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the python-designateclient package.
Group: Binaries
Requires: python-designateclient-license = %{version}-%{release}

%description bin
bin components for the python-designateclient package.


%package license
Summary: license components for the python-designateclient package.
Group: Default

%description license
license components for the python-designateclient package.


%package python
Summary: python components for the python-designateclient package.
Group: Default
Requires: python-designateclient-python3 = %{version}-%{release}

%description python
python components for the python-designateclient package.


%package python3
Summary: python3 components for the python-designateclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-designateclient package.


%prep
%setup -q -n python-designateclient-2.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551030093
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-designateclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-designateclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/designate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-designateclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
