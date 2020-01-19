
Name:           sblim-cmpi-devel
Version:        2.0.3
Release:        5%{?dist}
Summary:        SBLIM CMPI Provider Development Support

Group:          Development/Libraries
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for
C++ provider development it is also necessary to have
tog-pegasus-devel installed.

%package -n libcmpiCppImpl0
License:        EPL
Summary:        CMPI C++ wrapper library
Group:          Development/Libraries
Conflicts:      tog-pegasus-libs

%description -n libcmpiCppImpl0
This packages provides the C++ wrapper library for CMPI development

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libcmpiCppImpl0 -p /sbin/ldconfig

%postun -n libcmpiCppImpl0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}
%{_includedir}/cmpi

%files -n libcmpiCppImpl0
%defattr(-,root,root,-)
%{_libdir}/libcmpiCppImpl.so*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.0.3-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0.3-4
- Mass rebuild 2013-12-27

* Thu Jul 25 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.3-3
- Fix libcmpiCppImpl0 Conflicts
  Resolves: #980252

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.3-1
- Update to sblim-cmpi-devel-2.0.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 28 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.1-3
- Enable -debuginfo package

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 20 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.1-1
- Update to sblim-cmpi-devel-2.0.1
- Ship libcmpiCppImpl library in libcmpiCppImpl0 package

* Wed Nov  4 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.0-2
- Fix conversion between CMPIData and String

* Thu Aug 27 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.5-2
- Fix License
- Spec file cleanup, rpmlint check

* Fri Oct 24 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.5-1
- Update to 1.0.5
  Resolves: #468326

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-6
- Autorebuild for GCC 4.3

* Mon Dec 18 2006 Mark Hamzy <hamzy@us.ibm.com> - 1.0.4-5
- Removed -debuginfo package.
- Removed ldconfig from post/postun

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.0.4-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Feb 09 2006 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.0.4-1
- Initial RH/Fedora version
