#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : python-designateclient
Version  : 3.1.0
Release  : 39
URL      : http://tarballs.openstack.org/python-designateclient/python-designateclient-3.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-designateclient/python-designateclient-3.1.0.tar.gz
Source1  : http://tarballs.openstack.org/python-designateclient/python-designateclient-3.1.0.tar.gz.asc
Summary  : Python client library for Designate
Group    : Development/Tools
License  : Apache-2.0
Requires: python-designateclient-license = %{version}-%{release}
Requires: python-designateclient-python = %{version}-%{release}
Requires: python-designateclient-python3 = %{version}-%{release}
Requires: cliff
Requires: debtcollector
Requires: jsonschema
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : debtcollector
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : osc-lib
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-designateclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

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
%setup -q -n python-designateclient-3.1.0
cd %{_builddir}/python-designateclient-3.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581992937
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-designateclient
cp %{_builddir}/python-designateclient-3.1.0/LICENSE %{buildroot}/usr/share/package-licenses/python-designateclient/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-designateclient/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
