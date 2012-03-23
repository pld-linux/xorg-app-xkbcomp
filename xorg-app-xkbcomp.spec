Summary:	xkbcomp application - compiling XKB keyboard description
Summary(pl.UTF-8):	Aplikacja xkbcomp do kompilacji opisów klawiatury XKB
Name:		xorg-app-xkbcomp
Version:	1.2.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbcomp-%{version}.tar.bz2
# Source0-md5:	a0fc1ac3fc4fe479ade09674347c5aa0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
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
%{_mandir}/man1/xkbcomp.1x*
%{_pkgconfigdir}/xkbcomp.pc
