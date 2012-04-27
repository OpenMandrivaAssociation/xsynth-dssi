Name:       xsynth-dssi
Summary:    Xsynth-DSSI plugin
Version:    0.9.4
Release:    2

Source:     http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
URL:        http://dssi.sourceforge.net
License:    GPLv2+
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Xsynth-DSSI plugin, a classic-analog (VCOs-VCF-VCA) style software synthesizer.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}/Xsynth_gtk
%{_libdir}/dssi/%{name}.so
%{_datadir}/%{name}/factory_patches.Xsynth
%{_datadir}/%{name}/version_0.1_patches.Xsynth

