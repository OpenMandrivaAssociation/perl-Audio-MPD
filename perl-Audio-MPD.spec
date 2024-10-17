%define upstream_name	 Audio-MPD
%define upstream_version 1.111200

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Class for talking to MPD (Music Player Daemon) servers 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Audio::MPD::Common::Item)
BuildRequires:	perl(Getopt::Euclid)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl(Proc::Daemon)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Corpus::Audio::MPD)

BuildArch:	noarch

%description
Audio::MPD gives a clear object-oriented interface for talking to and
controlling MPD (Music Player Daemon) servers. A connection to the MPD server
is established as soon as a new Audio::MPD object is created. Commands are then
send to the server as the class's methods are called.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc AUTHORS LICENSE README TODO Changes
%{_bindir}/*
%{perl_vendorlib}/Audio
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Sat Apr 30 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.111.200-1mdv2011.0
+ Revision: 661027
- update to new version 1.111200

* Wed Mar 09 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.110.560-1
+ Revision: 643027
- new version

* Sun Sep 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.260-2mdv2011.0
+ Revision: 579841
- rebuild

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.260-1mdv2011.0
+ Revision: 570316
- update to 1.102260

* Fri Aug 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.430-2mdv2011.0
+ Revision: 566866
- rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.430-1mdv2011.0
+ Revision: 505264
- update to 1.100430
- adding missing buildrequires

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.170-1mdv2010.1
+ Revision: 466006
- adding missing buildrequires:
- update to 1.093170

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.92.950-1mdv2010.1
+ Revision: 461253
- adding missing buildrequires:
- adding missing buildrequires:
- update to 1.092950

* Thu Oct 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.19.7-1mdv2010.0
+ Revision: 451996
- update to v0.19.7

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.19.6-2mdv2010.0
+ Revision: 435533
- rebuild using %%perl_convert_version

* Sun Feb 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.6-1mdv2009.1
+ Revision: 340535
- update to new version 0.19.6

* Tue Jan 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.5-1mdv2009.1
+ Revision: 325505
- update to new version 0.19.5

* Sun Aug 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.4-1mdv2009.0
+ Revision: 272878
- update to new version 0.19.4

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.3-1mdv2009.0
+ Revision: 271752
- update to new version 0.19.3

* Wed Jun 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.2-1mdv2009.0
+ Revision: 224895
- update to new version 0.19.2

* Fri Jan 18 2008 Jérôme Quelin <jquelin@mandriva.org> 0.19.1-2mdv2008.1
+ Revision: 154597
- force rebuild for 5.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.1-1mdv2008.1
+ Revision: 114705
- update to new version 0.19.1

* Fri Nov 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.0-1mdv2008.1
+ Revision: 114012
- update to new version 0.19.0

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18.3-1mdv2008.1
+ Revision: 113405
- update to new version 0.18.3

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18.2-1mdv2008.1
+ Revision: 109470
- update to new version 0.18.2

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18.1-1mdv2008.0
+ Revision: 46869
+ rebuild (emptylog)

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.2-1mdv2008.0
+ Revision: 17454
- new version


* Mon Mar 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13.5-1mdv2007.1
+ Revision: 141686
- new version

* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13.3-1mdv2007.1
+ Revision: 134286
- fix build dependencies
- new version

* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12.4-1mdv2007.1
+ Revision: 120852
- new version

* Fri Dec 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12.3-1mdv2007.1
+ Revision: 93653
- Import perl-Audio-MPD

* Fri Dec 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12.3-1mdv2007.1
- first mdv release

