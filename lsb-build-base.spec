%define _provides_exceptions \\(lib\\(GL\\|ICE\\|SM\\|X11\\|Xext\\|Xi\\|Xt\\|c\\|crypt\\|dl\\|gcc_s\\|m\\|ncurses\\|pam\\|pthread\\|rt\\|stdc++\\|util\\|z\\)\\|ld-lsb.*\\)\\.so    

Summary: 	LSB Build environment base package
Name: 		lsb-build-base
Version: 	3.1.1
Release: 	%mkrel 4
License: 	LGPL
Group: 		Development/C
Source: 	ftp://ftp.freestandards.org/pub/lsb/lsbdev/released-3.1.0/source/lsb-build-base-%{version}.tar.bz2
URL:    	http://www.freestandards.org/download/#lsbdev
Patch0:         %{name}-rpmlint.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes: 	lsbdev-base

%description
The LSB Build environment base package provides stub libraries and
header files. These can be used to build LSB compliant applications.
Note that the version number of the package refers to the version
of the specification that the stub libraries and header files
have been generated for.

%package        -n %{name}-devel
Summary:        LSB Build environment base package
Group:          Development/C
Provides:       %{name} lsbdev-base-devel
Obsoletes: 	lsbdev-base-devel

%description -n %{name}-devel
The LSB Build environment base package provides stub libraries and
header files. These can be used to build LSB compliant applications.
Note that the version number of the package refers to the version
of the specification that the stub libraries and header files
have been generated for.

%prep
%setup -q
%patch0 -p1 -b .rpmlint

%build
make LSBVERSION=${RPM_PACKAGE_VERSION} LSBLIBCHK_VERSION=${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}

%install
rm -rf $RPM_BUILD_ROOT
[[ "%{_lib}" != "lib" ]] && LIB64=64
%makeinstall_std INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} SUBDIR=%{name} LIB64="$LIB64"
( cd $RPM_BUILD_ROOT/%{_prefix}/include/%{name} ; ln -s curses.h ncurses.h )
( cd $RPM_BUILD_ROOT/%{_prefix}/include/%{name} ; rm -fr All IA32 IA64 PPC32 PPC64 S390 S390X x86-64 )
( cd $RPM_BUILD_ROOT/%{_prefix}/%{_lib}/%{name} ; ln -s libncurses.so libcurses.so )

%clean
rm -rf $RPM_BUILD_ROOT

#(sb) lsbdev-base has no files, only -devel
%files -n %{name}-devel
%defattr(-,root,root)
%doc README Licence
%{_libdir}/%{name}
%{_includedir}/%{name}



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.1.1-4mdv2010.0
+ Revision: 429871
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1.1-3mdv2009.0
+ Revision: 251445
- rebuild
- fix spacing at top of description

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 3.1.1-1mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jun 12 2006 Stew Benedict <sbenedict@mandriva.com> 3.1.1-1mdv2007.0
- 3.1.1

* Thu Jun 08 2006 Olivier Blin <oblin@mandriva.com> 3.0.0-2mdv2007.0
- add libXi.so and librt.so in provides_exceptions (should fix auto installs,
  and allow xsetup.d programs to start in live as a side effect)

* Wed Jun 08 2005 Stew Benedict <sbenedict@mandriva.com> 3.0.0-1mdk
- 3.0 snapshot (not final)

* Thu Sep 02 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.4-2mdk
- provides_exceptions from Gwenole

* Thu Aug 26 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.4-1mdk
- 2.0.4, 64bit fixes

* Thu Aug 26 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.3-2mdk
- fix %%install stanza

* Mon Jul 26 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.3-1mdk
- repackage for Mandrakelinux
- restructure dirs for rpmlint(patch0), split into -devel 
- use doc macro, License

* Thu Jun 10 2004 Mats Wichmann <mats@freestandards.org>
- make symlinks for curses header and library
- clean out excess directories in header tree

