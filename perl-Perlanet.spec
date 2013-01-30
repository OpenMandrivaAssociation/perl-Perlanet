%define upstream_name    Perlanet
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Render the feed via a Template Toolkit
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Duration)
BuildRequires:	perl(Encode)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(HTML::Scrubber)
BuildRequires:	perl(HTML::Tidy)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Traits)
BuildRequires:	perl(MooseX::ConfigFromFile)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(TryCatch)
BuildRequires:	perl(URI::Fetch)
BuildRequires:	perl(XML::Feed)
BuildRequires:	perl(XML::OPML::SimpleGen)
BuildRequires:	perl(YAML)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Perlanet is a program for creating programs that aggregate web feeds (both
RSS and Atom). Web pages like this are often called "Planets" after the
Python software which originally popularised them. Perlanet is a planet
builder written in Perl - hence "Perlanet".

You are probably interested in the Perlanet::Simple manpage to get started
straight out of the box, batteries included style.

Perlanet itself is the driving force behind everything, however. Perlanet
reads a series of web feeds (filtering only those that are valid), sorts
and selects entries from these web feeds, and then creates a new aggregate
feed and renders this aggregate feed. Perlanet allows the user to customize
all of these steps through subclassing and roles.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_bindir}/perlanet
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.530.0-4mdv2011.0
+ Revision: 657824
- rebuild for updated spec-helper

* Fri Dec 17 2010 Shlomi Fish <shlomif@mandriva.org> 0.530.0-3mdv2011.0
+ Revision: 622515
- Bump the release to depend on the new OPML module
- Added deps and bumped the rel number
- import perl-Perlanet


* Fri Dec 03 2010 cpan2dist 0.53-1mdv
- initial mdv release, generated with cpan2dist
