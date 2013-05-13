%define	gem_name	ruby-vnc
Summary:	Ruby VNC library
Name:		ruby-vnc
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://ruby-vnc.googlecode.com/files/%{name}-%{version}.tgz
# Source0-md5:	f8219f408880a9df41683935bcfd2d05
Patch0:		veewee.patch
URL:		http://code.google.com/p/ruby-vnc
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Provides:	ruby-ruby-vnc = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library which implements the client VNC protocol to control VNC
servers.

%prep
%setup -q -n %{gem_name}-%{version}
%undos -f rb
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog COPYING
%dir %{ruby_vendorlibdir}/cipher
%{ruby_vendorlibdir}/cipher/des.rb
%{ruby_vendorlibdir}/net/vnc.rb
%{ruby_vendorlibdir}/net/vnc
