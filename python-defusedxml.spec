%define modulename defusedxml

Name:		python-%{modulename}
Version:	0.7.1
Release:	2
Summary:	XML bomb protection for Python stdlib modules
Group:		Development/Python
License:	Apache License
URL:		https://bitbucket.org/tiran/defusedxml
Source0:	https://files.pythonhosted.org/packages/0f/d5/c66da9b79e5bdb124974bfe172b4daf3c984ebd9c2a06e2b8a4dc7331c72/defusedxml-0.7.1.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
BuildRequires:  python3dist(setuptools)	 
 
#BuildRequires:	twill

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%package -n python2-%{modulename}	 
Summary:        XML bomb protection for Python stdlib modules	 
%{?python_provide:%python_provide python2-%{pypi_name}}	 
	 
%description -n python2-%{modulename}
The defusedxml package contains several Python-only workarounds and fixes for	 
denial of service and other vulnerabilities in Python's XML libraries. In order	 
to benefit from the protection you just have to import and use the listed	 
functions / classes from the right defusedxml module instead of the original	 
module. This is the Python 2 build.

%prep
%autosetup -n %{modulename}-%{version} -p1

%build
%py_build
%py2_build

%check
#python admin/runtests

%install
%py_install
%py2_install

%files
%doc CHANGES.txt LICENSE README.txt
%{py_puresitedir}/*

%files -n python2-%{modulename} 
%doc README.txt README.html CHANGES.txt	 
%license LICENSE
%{py2_puresitedir}/*
