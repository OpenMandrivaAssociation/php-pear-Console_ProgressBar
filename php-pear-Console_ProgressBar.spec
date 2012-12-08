%define		_class		Console
%define		_subclass	ProgressBar
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.5.2beta
Release:	%mkrel 7
Summary:	Provides an easy-to-use interface to progress bars
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Console_ProgressBar/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The class allows you to display progress bars in your terminal. You can
use this for displaying the status of downloads or other tasks that take
some time.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.2beta-5mdv2011.0
+ Revision: 667488
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2beta-4mdv2011.0
+ Revision: 607092
- rebuild

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2beta-3mdv2010.1
+ Revision: 478293
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.2beta-2mdv2010.0
+ Revision: 426605
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.5.2beta-1mdv2009.1
+ Revision: 368255
- Update php pear Console_ProgressBar to version 0.5.2beta

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-11mdv2009.1
+ Revision: 321801
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2-10mdv2009.0
+ Revision: 224689
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-9mdv2008.1
+ Revision: 178502
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.2-8mdv2008.0
+ Revision: 64197
- rebuild


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdv2007.0
+ Revision: 81080
- Import php-pear-Console_ProgressBar

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package (PLD import)

