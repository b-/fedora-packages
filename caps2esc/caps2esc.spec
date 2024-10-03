Name:           caps2esc
Version:        0.3.2
Release:        %autorelease
Summary:        Transform the most useless key ever into the most useful one
License:        GPL-3.0-or-later
URL:            https://gitlab.com/interception/linux/plugins/caps2esc
Source:         https://gitlab.com/interception/linux/plugins/caps2esc/-/archive/v%{version}/caps2esc-v%{version}.tar.bz2 
BuildRequires:  gcc-c++
BuildRequires:  cmake


%description
caps2esc is an Interception Tools plugin that turns the Caps Lock key into the
Escape key when pressed alone and the Ctrl key when pressed in combination with
another key.


%prep
%autosetup -n caps2esc-v%{version}


%build
%cmake
%cmake_build


%install
%cmake_install


%check


%files
%license
%doc README.md
%{_bindir}/caps2esc


%changelog
* Thu Oct 03 2024 Severen Redwood <sev@severen.dev> 0.3.2-1
- New package built.

