Name:           interception-tools
Version:        0.6.8
Release:        %autorelease
Summary:        A minimal and composable infrastructure on top of libudev and libevdev
License:        GPL-3.0-or-later
URL:            https://gitlab.com/interception/linux/tools
Source0:        https://gitlab.com/interception/linux/tools/-/archive/v%{version}/tools-v%{version}.tar.bz2
Source1:        udevmon.service
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libudev-devel
BuildRequires:  libevdev-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  boost-devel

%description
Interception Tools is a small set of utilities for operating on input
events of evdev devices.

%prep
%autosetup -n tools-v%{version}


%build
%cmake
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system


%check


%files
%license
%doc README.md
%{_bindir}/intercept
%{_bindir}/mux
%{_bindir}/udevmon
%{_bindir}/uinput
%{_prefix}/lib/systemd/system/udevmon.service


%changelog
* Sat Apr 19 2025 bri rec <copr@ibeep.com> 0.6.8-2
- bump everything.
* Thu Oct 03 2024 Severen Redwood <sev@severen.dev> 0.6.8-1
- New package built.
