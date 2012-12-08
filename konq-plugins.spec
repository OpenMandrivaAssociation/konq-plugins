Summary:	Konqueror Plugins
Name:		konq-plugins
Version: 	4.6.1
Release: 	%mkrel 2
Epoch:      1
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdebase4-devel >= 1:4.2.0
BuildRequires:	tidy-devel
Obsoletes:	kdeaddons-akregator < 1:3.5.10-2
Obsoletes:	kdeaddons-konq-plugins < 1:3.5.10-2
Obsoletes:	kdeaddons-konqimagegallery < 1:3.5.10-2
%if %mdkversion >= 201000
Obsoletes:  kdeaddons-kfile-plugins < 1:3.5.10-2
Obsoletes:  kdeaddons-kicker-applets < 1:3.5.10-2
Obsoletes:  kdeaddons-knewsticker < 1:3.5.10-2
Obsoletes:  kdeaddons-metabar < 1:3.5.10-2
Obsoletes:  kdeaddons-renamedlg < 1:3.5.10-2
Obsoletes:  kdeaddons-searchbar < 1:3.5.10-2
%endif
Conflicts:	kde-l10n < 3.5.9-5

%description 
This module contains plugins that interact with Konqueror.

%files
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/kde4/*.so
%_kde_services/ServiceMenus/*.desktop
%_kde_services/*.desktop
%_kde_appsdir/*
%_kde_configdir/*
%_kde_datadir/config.kcfg/*
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:4.6.1-2mdv2011.0
+ Revision: 666039
- mass rebuild

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 1:4.6.1-1
+ Revision: 643940
- new version 4.6.1

* Tue Dec 07 2010 Funda Wang <fwang@mandriva.org> 1:4.4.0-2mdv2011.0
+ Revision: 613572
- fix build with qt 4.7.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sat Feb 13 2010 Funda Wang <fwang@mandriva.org> 1:4.4.0-1mdv2010.1
+ Revision: 505218
- new version 4.4.0

* Thu Feb 04 2010 Christophe Fergeau <cfergeau@mandriva.com> 1:4.3.3-4mdv2010.1
+ Revision: 500748
- rebuild for new kdewebkit

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.3-3mdv2010.1
+ Revision: 465243
- Rebuild against new Qt

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 1:4.3.3-2mdv2010.1
+ Revision: 463380
- New version 4.3.3

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 444783
- Add some obsoletes

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 1:4.3.0-1mdv2010.0
+ Revision: 411066
- new version 4.3.0

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.4-2mdv2010.0
+ Revision: 389812
- Rebuild against new kde
- Sync with updates

* Thu Jun 04 2009 Funda Wang <fwang@mandriva.org> 4.2.4-1mdv2010.0
+ Revision: 382645
- New version 4.2.4

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 4.2.3-1mdv2010.0
+ Revision: 379789
- versioned kdebase4
- New version 4.2.3

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 4.2.2-1mdv2010.0
+ Revision: 370575
- New version 4.2.2

* Tue Jan 27 2009 Funda Wang <fwang@mandriva.org> 4.2.0-1mdv2009.1
+ Revision: 334270
- New version 4.2.0

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 4.1.96-1mdv2009.1
+ Revision: 330883
- New version 4.1.96

  + Anssi Hannula <anssi@mandriva.org>
    - obsoletes kdeaddons-akregator

* Wed Nov 26 2008 Funda Wang <fwang@mandriva.org> 4.1.3-3mdv2009.1
+ Revision: 306920
- obsolete konqimagegallery

* Wed Nov 26 2008 Funda Wang <fwang@mandriva.org> 4.1.3-2mdv2009.1
+ Revision: 306896
- obsoletes old kdeaddons package

* Wed Nov 19 2008 Funda Wang <fwang@mandriva.org> 4.1.3-1mdv2009.1
+ Revision: 304399
- new version 4.1.3

* Mon Oct 13 2008 Funda Wang <fwang@mandriva.org> 4.1.2-1mdv2009.1
+ Revision: 293080
- New version 4.1.2

* Thu Sep 04 2008 Funda Wang <fwang@mandriva.org> 4.1.1-1mdv2009.0
+ Revision: 280248
- import konq-plugins


