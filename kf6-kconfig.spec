%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6ConfigCore
%define devname %mklibname KF6ConfigCore -d
%define guilibname %mklibname KF6ConfigGui
%define qmllibname %mklibname KF6ConfigQml
#define git 20231103

Name: kf6-kconfig
Version: 5.246.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kconfig/-/archive/master/kconfig-master.tar.bz2#/kconfig-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{version}/kconfig-%{version}.tar.xz
%endif
Summary: KConfig provides an advanced configuration system.
URL: https://invent.kde.org/frameworks/kconfig
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
KConfig provides an advanced configuration system.

%package -n %{libname}
Summary: KConfig provides an advanced configuration system.
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KConfig provides an advanced configuration system.

%package -n %{guilibname}
Summary: KConfig provides an advanced configuration system, GUI parts
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{guilibname}
KConfig provides an advanced configuration system, GUI parts

%package -n %{qmllibname}
Summary: KConfig provides an advanced configuration system, Qml parts
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{qmllibname}
KConfig provides an advanced configuration system, Qml parts

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{guilibname} = %{EVRD}
Requires: %{qmllibname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KConfig provides an advanced configuration system.

%prep
%autosetup -p1 -n kconfig-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kconfig.*
%{_bindir}/kreadconfig6
%{_bindir}/kwriteconfig6
%{_libdir}/libexec/kf6/kconf_update
%{_libdir}/libexec/kf6/kconfig_compiler_kf6

%files -n %{devname}
%{_includedir}/KF6/KConfig
%{_includedir}/KF6/KConfigCore
%{_includedir}/KF6/KConfigGui
%{_includedir}/KF6/KConfigQml
%{_libdir}/cmake/KF6Config
%{_qtdir}/doc/KF6Config.*

%files -n %{libname}
%{_libdir}/libKF6ConfigCore.so*

%files -n %{guilibname}
%{_libdir}/libKF6ConfigGui.so*

%files -n %{qmllibname}
%{_libdir}/libKF6ConfigQml.so*
%{_qtdir}/qml/org/kde/config
