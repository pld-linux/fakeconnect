Summary:	FakeConnect is a application/network "stress-test" program
Summary(pl):	FakeConnect jest aplikacj± s³u¿±c± testowaniu sieci
Name:		fakeconnect
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.hostname.org/fake_connect/%{name}-%{version}.tar.gz
# Source0-md5:	55220ebadef5f541d705b72fe222b5b1
URL:		http://www.hostname.org/index.php/FakeConnect
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FakeConnect is a application/network "stress-test" program. It can
simulate a real TCP connection (with SYN, ACK, and ACK_SEQ), opening
up to 65000 connections without overloading the local machine.

%description -l pl
FakeConnect jest aplikacj± s³u¿±c± do testowania sieci. Mo¿e symulowaæ
prawdziwe po³±czenia TCP (z SYN, ACK i ACK_SEQ), otwiera do 65000
po³±czeñ bez przeci±¿ania lokalnej maszyny.

%prep
%setup -q

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
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
