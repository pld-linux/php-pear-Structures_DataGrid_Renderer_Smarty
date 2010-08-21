%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_Smarty
Summary:	%{_pearname} - renderer driver using Smarty
Summary(pl.UTF-8):	%{_pearname} - sterowink renderera korzystający ze Smarty
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	4
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9d8433e6c71c187ac48c12e4b576bb39
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_Smarty/
BuildRequires:	php-pear-PEAR >= 1:1.4.9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-Structures_DataGrid_Renderer_Pager >= 0.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid using Smarty. It
adds a couple of variables to a Smarty instance.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderera do Structures_DataGrid.
korzystający ze Smarty. Dodaje on kilka zmiennych do instancji
Smarty'ego.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/Smarty.php
