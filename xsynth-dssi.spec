%define name	xsynth-dssi
%define version	0.9.2
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Xsynth-DSSI plugin
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
URL:		http://dssi.sourceforge.net
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	gtk2-devel
BuildRequires:	gtk-devel

%description
Xsynth-DSSI plugin, a classic-analog (VCOs-VCF-VCA) style software synthesizer.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make
								
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}/Xsynth_gtk
%{_libdir}/dssi/%{name}.la
%{_libdir}/dssi/%{name}.so
%{_datadir}/%{name}/factory_patches.Xsynth
%{_datadir}/%{name}/version_0.1_patches.Xsynth
	       
