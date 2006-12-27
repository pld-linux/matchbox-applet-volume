Summary:	Matchbox applet to control volume
Summary(pl):	Aplet ¶rodowiska Matchbox do sterowania g³o¶no¶ci±
Name:		matchbox-applet-volume
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/mb-applet-volume/%{version}/mb-applet-volume-%{version}.tar.bz2
# Source0-md5:	5e814f149cf785bcaa6a0c919e87a9d7
Patch0:		%{name}-desktop.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libmatchbox-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox applet to control volume.

%description -l pl
Aplet ¶rodowiska Matchbox do sterowania g³o¶no¶ci±.

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
%{_pixmapsdir}/*.png
