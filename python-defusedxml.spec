%define module defusedxml

Name:		python-%{module}
Version:	0.7.1
Release:	3
Summary:	XML bomb protection for Python stdlib modules
Group:		Development/Python
License:	Apache License
URL:		https://github.com/tiran/defusedxml
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc CHANGES.txt README.txt
%license LICENSE
%{py_puresitedir}/*
