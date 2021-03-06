#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	BFD
Summary:	BFD - Impromptu dumping of data structures for debugging purposes
Summary(pl.UTF-8):	BFD - improwizowane zrzucanie struktur danych w celach diagnostycznych
Name:		perl-BFD
Version:	0.31
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RB/RBS/%{pdir}-%{version}.tar.gz
# Source0-md5:	7715ecf4133b9ab1ddabf9221663d576
URL:		http://search.cpan.org/dist/BFD/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for impromptu dumping of output to STDERR. Useful when you want
to take a peek at a nest Perl data structure by emitting (relatively)
nicely formatted output with filename and line number prefixed to each
line.

%description -l pl.UTF-8
Ten moduł pozwala na improwizowane zrzucanie struktur danych na
STDERR. Jest przydatny aby podejrzeć zagnieżdżoną perlową strukturę
danych dając ładnie sformatowane wyjście z nazwą pliki i numerem linii
przed każdą linią.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
