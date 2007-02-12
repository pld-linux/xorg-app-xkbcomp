Summary:	xkbcomp application
Summary(pl.UTF-8):	Aplikacja xkbcomp
Name:		xorg-app-xkbcomp
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbcomp-%{version}.tar.bz2
# Source0-md5:	2fbcae1323c266edf5b6c61751f2e343
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbcomp application.

%description -l pl.UTF-8
Aplikacja xkbcomp.

%prep
%setup -q -n xkbcomp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc COPYING ChangeLog README*
%attr(755,root,root) %{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1x*
