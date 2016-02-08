#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-designateclient
Version  : 2.0.0
Release  : 14
URL      : http://tarballs.openstack.org/python-designateclient/python-designateclient-2.0.0.tar.gz
Source0  : http://tarballs.openstack.org/python-designateclient/python-designateclient-2.0.0.tar.gz
Summary  : OpenStack DNS as a Service - Client
Group    : Development/Tools
License  : Apache-2.0
Requires: python-designateclient-bin
Requires: python-designateclient-python
BuildRequires : Babel
BuildRequires : Jinja2-python
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : cffi
BuildRequires : coverage-python
BuildRequires : cryptography
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : enum34
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking-python
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : iso8601
BuildRequires : jsonpatch
BuildRequires : jsonpointer
BuildRequires : jsonschema
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests
BuildRequires : requests-mock
BuildRequires : setuptools
BuildRequires : six
BuildRequires : stevedore
BuildRequires : testrepository
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : warlock
Patch1: 0001-run-tests.patch

%description
Python bindings to the Designate API
=====================================
.. image:: https://img.shields.io/pypi/v/python-designateclient.svg
:target: https://pypi.python.org/pypi/python-designateclient/
:alt: Latest Version

%package bin
Summary: bin components for the python-designateclient package.
Group: Binaries

%description bin
bin components for the python-designateclient package.


%package python
Summary: python components for the python-designateclient package.
Group: Default
Requires: debtcollector-python
Requires: stevedore

%description python
python components for the python-designateclient package.


%prep
%setup -q -n python-designateclient-2.0.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/designate

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
