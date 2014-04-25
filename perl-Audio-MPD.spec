%define upstream_name	 Audio-MPD
%define upstream_version 1.120610

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Class for talking to MPD (Music Player Daemon) servers 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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


