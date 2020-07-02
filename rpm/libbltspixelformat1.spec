Name: libbltspixelformat1
Summary: BLTS pixel format conversion library
Version: 0.1.6
Release: 1
License: GPLv2
URL: https://github.com/mer-qa/blts-pixelformat
Source0: %{name}-%{version}.tar.gz
BuildRequires: libbltscommon-devel

%package devel
Summary: BLTS pixel format conversion library dev package
Requires: %{name} = %{version}-%{release}
Provides: libbltspixelformat-devel

%description
Pixel format conversion functions for the BLTS test assets. Based on ffmpeg libswscale.

%description devel
This package contains libbltspixelformat1 development files

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%doc README
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
