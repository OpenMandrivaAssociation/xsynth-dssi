Name:       xsynth-dssi
Summary:    Xsynth-DSSI plugin
Version:    0.9.4
Release:    3

Source:     http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
URL:        https://dssi.sourceforge.net
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



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.9.4-2
+ Revision: 793825
- rebuild, spec cleanup

* Sat Sep 25 2010 Frank Kober <emuse@mandriva.org> 0.9.4-1mdv2011.0
+ Revision: 581020
- new version 0.9.4

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 471359
- new version 0.9.2
- drop uidir patch (merged upstream)
- fix license tag
- $RPM_BUILD_ROOT -> %%{buildroot}

* Sun Aug 02 2009 Funda Wang <fwang@mandriva.org> 0.9.0-3mdv2010.0
+ Revision: 407547
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Helio Chissini de Castro <helio@mandriva.com>
    - import xsynth-dssi-0.9.0-2mdk


* Sun Apr 02 2006 Pedro Lopez-Cabanillas <plcl@users.sf.net> 0.9.0-2mdk
- patch for installing the GUI at the proper location

* Sat Apr 01 2006 Austin Acton <austin@mandriva.org> 0.9.0-1mdk
- spec from Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>
- initial package

