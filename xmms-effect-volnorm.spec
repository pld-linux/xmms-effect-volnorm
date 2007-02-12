Summary:	XMMS - Plugin for Normalizing Volume
Summary(pl.UTF-8):   Wtyczka do XMMS-a normalizująca poziom dźwięku
Name:		xmms-effect-volnorm
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.sourceforge.net/volnorm/volnorm-%{version}.tar.gz
# Source0-md5:	8f4d19b8e45d5f51c303303858f9905a
Patch0:		%{name}-dont_check_gtk+extra.patch
URL:		http://volnorm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.6
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{xmms_effect_plugindir}

%description
This XMMS plugin changes the volume of played songs to a uniform level
such that the base volume of all songs will be the same so that you
will not need to play with the volume knob whenever a song changes.

%description -l pl.UTF-8
Wtyczka do XMMS-a normalizująca poziom głośności odgrywanych utworów.
Pozwala na odtwarzanie kazdego z plików z jednakową głośnością.

%prep
%setup -q -n volnorm-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	XMMS_PATH="/usr/bin/xmms"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{_libdir}/libnormvol.la,%{_bindir}/testload}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
