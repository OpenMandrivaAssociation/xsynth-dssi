%define name	xsynth-dssi
%define version	0.9.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Xsynth-DSSI plugin
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
Patch:		%{name}-0.9.0-uidir.patch
URL:		http://dssi.sourceforge.net
License:	GPL
Group:		Sound
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	gtk2-devel
BuildRequires:	gtk-devel

%description
Xsynth-DSSI plugin, a classic-analog (VCOs-VCF-VCA) style software synthesizer.

%prep
%setup -q
%patch -p0

%build
autoreconf
%configure2_5x
%make
								
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}/Xsynth_gtk
%{_libdir}/dssi/%{name}.la
%{_libdir}/dssi/%{name}.so
%{_datadir}/%{name}/factory_patches.Xsynth
%{_datadir}/%{name}/version_0.1_patches.Xsynth
	       
