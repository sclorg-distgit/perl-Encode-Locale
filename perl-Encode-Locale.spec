%{?scl:%scl_package perl-Encode-Locale}

Name:           %{?scl_prefix}perl-Encode-Locale
Version:        1.05
Release:        6%{?dist}
Summary:        Determine the locale encoding
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Encode-Locale/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Encode-Locale-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Encode) >= 2
BuildRequires:  %{?scl_prefix}perl(Encode::Alias)
# Encode::HanExtra not used at tests, not yet packaged
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Win32 not used on Linux
# Win32::API not used on Linux
# Win32::Console not used on Linux
# Recommended:
BuildRequires:  %{?scl_prefix}perl(I18N::Langinfo)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(utf8)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Encode) >= 2
# Encode::HanExtra not yet packaged
# Recommended:
Requires:       %{?scl_prefix}perl(I18N::Langinfo)
Requires:       %{?scl_prefix}perl(warnings)

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Encode)/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Encode\\)$
%endif

%description
In many applications it's wise to let Perl use Unicode for the strings
it processes.  Most of the interfaces Perl has to the outside world is
still byte based.  Programs therefore needs to decode byte strings
that enter the program from the outside and encode them again on the
way out.

%prep
%setup -q -n Encode-Locale-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/Encode/
%{_mandir}/man3/Encode::Locale.3*

%changelog
* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 1.05-6
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-2
- Perl 5.22 rebuild

* Fri Jan 23 2015 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.03-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-4
- Filter duplicated requires.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.16 rebuild

* Mon Feb 13 2012 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Petr Pisar <ppisar@redhat.com> - 1.02-4
- BuildRequire perl(base)

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-3
- Perl mass rebuild

* Thu May 26 2011 Petr Pisar <ppisar@redhat.com> - 1.02-2
- Remove explicit defattr

* Thu May 26 2011 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Wed Mar 16 2011 Petr Pisar <ppisar@redhat.com> - 1.01-1
- Spec file provided by Ville Skyttä
- BuildRoot stuff removed
- Dependencies adjusted
