%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Indexing
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML Indexing support
Summary(pl):	%{_pearname} - wsparcie dla indeksowania XML
Name:		php-pear-%{_pearname}
Version:	0.3.5
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6e1ba9d15b5480df3a8c38a3d8ccf958
URL:		http://pear.php.net/package/XML_Indexing/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3
Requires:	php-pear
Requires:	php-pear-File >= 1.0.3
Requires:	php-pear-PEAR-core >= 1:1.2
Requires:	php-pear-XML_XPath >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Console/Table.*)' 'pear(Benchmark.*)'

%description
This package provides support for indexing XML files. It assists you
in creating and using such indexes in order to reduce access-time to
local XML files.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza wsparcia dla indeksowania plików XML. Wspomaga
tworzenie i u¿ywanie tego typu indeksów w celu zmniejszenia czasu
dostêpu do lokalnych plików XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
