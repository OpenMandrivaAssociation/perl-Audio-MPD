%define module	Audio-MPD
%define name	perl-%{module}
%define version 0.18.3
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Class for talking to MPD (Music Player Daemon) servers 
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Audio/%{module}-%{version}.tar.bz2
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Class::Accessor::Fast)
Buildrequires:	perl(Readonly)
Buildrequires:	perl(Audio::MPD::Common::Item)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Audio::MPD gives a clear object-oriented interface for talking to and
controlling MPD (Music Player Daemon) servers. A connection to the MPD server
is established as soon as a new Audio::MPD object is created. Commands are then
send to the server as the class's methods are called.

%prep
%setup -q -n %{module}-%{version} 

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
