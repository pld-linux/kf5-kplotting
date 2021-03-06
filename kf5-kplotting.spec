%define		kdeframever	5.84
%define		qtver		5.9.0
%define		kfname		kplotting
#
Summary:	Data plotting
Name:		kf5-%{kfname}
Version:	5.84.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	21e30172ff36f429f21fbcede0f7f436
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KPlotWidget is a QWidget-derived class that provides a virtual base
class for easy data-plotting. The idea behind KPlotWidget is that you
only have to specify information in "data units"; i.e., the natural
units of the data being plotted. KPlotWidget automatically converts
everything to screen pixel units.

KPlotWidget draws X and Y axes with tick marks and tick labels. It
automatically determines how many tick marks to use and where they
should be, based on the data limits specified for the plot. You change
the limits by calling `setLimits(double x1, double x2, double y1,
double y2)`.

Data to be plotted are stored using the KPlotObject class. KPlotObject
consists of a QList of QPointF's, each specifying the X,Y coordinates
of a data point. KPlotObject also specifies the "type" of data to be
plotted (POINTS or CURVE or POLYGON or LABEL).

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5Plotting.so.5
%attr(755,root,root) %{_libdir}/libKF5Plotting.so.*.**
%attr(755,root,root) %{qt5dir}/plugins/designer/kplotting5widgets.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPlotting
%{_includedir}/KF5/kplotting_version.h
%{_libdir}/cmake/KF5Plotting
%{_libdir}/libKF5Plotting.so
%{qt5dir}/mkspecs/modules/qt_KPlotting.pri
