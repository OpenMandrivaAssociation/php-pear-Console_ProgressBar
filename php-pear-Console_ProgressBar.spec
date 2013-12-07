%define		_class		Console
%define		_subclass	ProgressBar
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Provides an easy-to-use interface to progress bars
Name:		php-pear-%{upstream_name}
Version:	0.5.2beta
Release:	12
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Console_ProgressBar/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
The class allows you to display progress bars in your terminal. You can
use this for displaying the status of downloads or other tasks that take
some time.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

