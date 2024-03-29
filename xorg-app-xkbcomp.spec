Summary:	xkbcomp application - compiling XKB keyboard description
Summary(pl.UTF-8):	Aplikacja xkbcomp do kompilacji opisów klawiatury XKB
Name:		xorg-app-xkbcomp
Version:	1.4.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xkbcomp-%{version}.tar.xz
# Source0-md5:	83d711948de9ccac550d2f4af50e94c3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.70
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xkbcomp keymap compiler converts a description of an XKB keymap
into one of several output formats. The most common use for xkbcomp is
to create a compiled keymap file (.xkm extension) which can be read
directly by XKB-capable X servers or utilities. The keymap compiler
can also produce C header files or XKB source files. The C header
files produced by xkbcomp can be included by X servers or utilities
that need a built-in default keymap.

%description -l pl.UTF-8
xkbcomp jest kompilatorem map klawiatury przekształcającym opisy map
klawiatury na jeden z kilku formatów wyjściowych. Najbardziej
powszechnym zastosowaniem xkbcomp jest tworzenie plików skompilowanych
map klawiatury (z rozszerzeniem .xkm), które można mogą być czytane
bezpośrednio przez serwery X lub narzędzia obsługujące rozszerzenie
XKB. Kompilator może także utworzyć pliki nagłówkowe C lub pliki
źródłowe XKB. Pliki nagłówkowe C mogą być włączane przez serwery X lub
narzędzia wymagające wbudowanej domyślnej mapy klawiatury.

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
%{_mandir}/man1/xkbcomp.1*
%{_pkgconfigdir}/xkbcomp.pc
