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

