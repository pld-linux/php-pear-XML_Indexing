%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Indexing
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML Indexing support
Summary(pl):	%{_pearname} - wsparcie dla indeksowania XML
Name:		php-pear-%{_pearname}
Version:	0.3.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ac0601e4c5eb650c7619d12263b73e82
URL:		http://pear.php.net/package/XML_Indexing/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Builder

install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Builder/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Builder

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}
