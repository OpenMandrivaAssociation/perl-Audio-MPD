%define upstream_name	 Audio-MPD
%define upstream_version 1.102260

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Class for talking to MPD (Music Player Daemon) servers 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl(Audio::MPD::Common::Item)
Buildrequires:	perl(Getopt::Euclid)
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Moose)
Buildrequires:	perl(Moose::Util::TypeConstraints)
Buildrequires:  perl(MooseX::Has::Sugar)
Buildrequires:	perl(MooseX::SemiAffordanceAccessor)
Buildrequires:	perl(Proc::Daemon)
Buildrequires:	perl(Readonly)
Buildrequires:	perl(Test::Corpus::Audio::MPD)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Audio::MPD gives a clear object-oriented interface for talking to and
controlling MPD (Music Player Daemon) servers. A connection to the MPD server
is established as soon as a new Audio::MPD object is created. Commands are then
send to the server as the class's methods are called.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
%{__rm} -rf %{buildroot} 
./Build install destdir=%{buildroot}

%clean 
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README TODO Changes
%{_bindir}/*
%{perl_vendorlib}/Audio
%{_mandir}/man3/*
%{_mandir}/man1/*
