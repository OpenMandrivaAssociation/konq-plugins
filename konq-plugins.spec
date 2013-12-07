Summary:	Konqueror Plugins
Name:		konq-plugins
Epoch:		1
Version:	4.6.1
Release:	6
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.tar.bz2
BuildRequires:	kdebase4-devel >= 1:4.2.0
BuildRequires:	tidy-devel

%description 
This module contains plugins that interact with Konqueror.

%files
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_services}/*.desktop
%{_kde_appsdir}/*
%{_kde_configdir}/*
%{_kde_datadir}/config.kcfg/*
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

