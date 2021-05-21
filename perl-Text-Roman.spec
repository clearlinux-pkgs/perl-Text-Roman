#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Roman
Version  : 3.5
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/S/SY/SYP/Text-Roman-3.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SY/SYP/Text-Roman-3.5.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-roman-perl/libtext-roman-perl_3.5-2.debian.tar.xz
Summary  : 'Allows conversion between Roman and Arabic algarisms.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Roman-license = %{version}-%{release}
Requires: perl-Text-Roman-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Text::Roman - Allows conversion between Roman and Arabic algarisms.
VERSION
version 3.5

%package dev
Summary: dev components for the perl-Text-Roman package.
Group: Development
Provides: perl-Text-Roman-devel = %{version}-%{release}
Requires: perl-Text-Roman = %{version}-%{release}

%description dev
dev components for the perl-Text-Roman package.


%package license
Summary: license components for the perl-Text-Roman package.
Group: Default

%description license
license components for the perl-Text-Roman package.


%package perl
Summary: perl components for the perl-Text-Roman package.
Group: Default
Requires: perl-Text-Roman = %{version}-%{release}

%description perl
perl components for the perl-Text-Roman package.


%prep
%setup -q -n Text-Roman-3.5
cd %{_builddir}
tar xf %{_sourcedir}/libtext-roman-perl_3.5-2.debian.tar.xz
cd %{_builddir}/Text-Roman-3.5
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Roman-3.5/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Roman
cp %{_builddir}/Text-Roman-3.5/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Roman/740710d72b8fe7d7735f0b125d9d65910661418f
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Roman/cf72d41e68ef0666d41e292285f7de6c512bc6a7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Roman.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Roman/740710d72b8fe7d7735f0b125d9d65910661418f
/usr/share/package-licenses/perl-Text-Roman/cf72d41e68ef0666d41e292285f7de6c512bc6a7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Text/Roman.pm
