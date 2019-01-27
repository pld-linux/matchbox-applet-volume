Summary:	Matchbox applet to control volume
Summary(pl.UTF-8):	Aplet środowiska Matchbox do sterowania głośnością
Name:		matchbox-applet-volume
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.yoctoproject.org/releases/matchbox/mb-applet-volume/%{version}/mb-applet-volume-%{version}.tar.bz2
# Source0-md5:	5e814f149cf785bcaa6a0c919e87a9d7
Patch0:		%{name}-desktop.patch
URL:		https://www.yoctoproject.org/software-item/matchbox/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libmatchbox-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox applet to control volume.

%description -l pl.UTF-8
Aplet środowiska Matchbox do sterowania głośnością.

%prep
%setup -q -n mb-applet-volume-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/mb-applet-volume
%{_desktopdir}/mb-applet-volume.desktop
%{_pixmapsdir}/mbvol-*.png
