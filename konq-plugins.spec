Summary:	Konqueror Plugins
Name:		konq-plugins
Version: 	4.2.4
Release: 	%mkrel 1
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdebase4-devel >= 1:4.2.0
BuildRequires:	webkitkde-devel webkitkde
BuildRequires:	tidy-devel
Obsoletes:	kdeaddons-akregator < 1:3.5.10-2
Obsoletes:	kdeaddons-konq-plugins < 1:3.5.10-2
Obsoletes:	kdeaddons-konqimagegallery < 1:3.5.10-2
Conflicts:	kde-l10n < 3.5.9-5

%description 
This module contains plugins that interact with Konqueror.

%files -f %name.lang
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

%find_lang %name --with-html --all-name

%clean
rm -rf %{buildroot}
