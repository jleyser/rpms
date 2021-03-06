# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scalar-List-Utils

Summary: Common Scalar and List utility subroutines
Name: perl-Scalar-List-Utils
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scalar-List-Utils/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Scalar-List-Utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004
Requires: perl >= 0:5.004

%description
Common Scalar and List utility subroutines.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Scalar::Util.3pm*
%doc %{_mandir}/man3/List::Util.3pm*
%doc %{_mandir}/man3/List::Util::XS.3pm*
%dir %{perl_vendorarch}/auto/List/
%{perl_vendorarch}/auto/List/Util/
%dir %{perl_vendorarch}/List/
%{perl_vendorarch}/List/Util.pm
%{perl_vendorarch}/List/Util/PP.pm
%{perl_vendorarch}/List/Util/XS.pm
%dir %{perl_vendorarch}/Scalar/
%{perl_vendorarch}/Scalar/Util.pm
%{perl_vendorarch}/Scalar/Util/PP.pm

%changelog
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Mon Aug  3 2009 Christoph Maser <cmr@financial.com> - 1.21-1
- Updated to version 1.21.

* Fri Jan 02 2009 Dag Wieers <dag@wieers.com> - 1.19-1
- Initial package. (using DAR)
