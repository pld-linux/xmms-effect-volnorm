Summary:	XMMS - Plugin for Normalizing Volume
Summary(pl):	Wtyczka do XMMS-a normalizuj±ca poziom d¼wiêku
Name:		xmms-effect-volnorm
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.sourceforge.net/volnorm/volnorm-%{version}.tar.gz
# Source0-md5:	8f4d19b8e45d5f51c303303858f9905a
URL:		http://volnorm.sourceforge.net/
BuildRequires:	glib-devel >= 1.2.6
BuildRequires:	gtk+-devel
BuildRequires:	xmms
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This XMMS plugin changes the volume of played songs to a uniform level
such that the base volume of all songs will be the same so that you
will not need to play with the volume knob whenever a song changes.

%description -l pl
Wtyczka do XMMS-a normalizuj±ca poziom g³o¶no¶ci odgrywanych utworów.
Pozwala na odtwarzanie kazdego z plików z jednakow± g³o¶no¶ci±.

%prep
%setup -q -n volnorm-%{version}

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/local/bin/testload $RPM_BUILD_ROOT%{_bindir}
rmdir $RPM_BUILD_ROOT%{_prefix}/local/bin $RPM_BUILD_ROOT%{_prefix}/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{xmms_effect_plugindir}/*
%attr(755,root,root) %{_bindir}/*
