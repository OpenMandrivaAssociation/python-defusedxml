%define modulename defusedxml

Name:		python-%{modulename}
Version:	0.6.0
Release:	1
Summary:	XML bomb protection for Python stdlib modules
Group:		Development/Python
License:	Apache License
URL:		https://bitbucket.org/tiran/defusedxml
Source0:	https://files.pythonhosted.org/packages/source/d/defusedxml/defusedxml-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-devel
#BuildRequires:	twill

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%prep
%autosetup -n %{modulename}-%{version} -p1

%build
%py_build

%check
#python admin/runtests

%install
python setup.py install \
	--skip-build --root %{buildroot} --record=INSTALLED_FILES

%files
%doc CHANGES.txt LICENSE README.txt
%{py_puresitedir}/*
