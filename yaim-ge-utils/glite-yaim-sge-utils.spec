%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-sge-utils module configure SGE utils. 
Name: glite-yaim-sge-utils
Version: x
Vendor: EGEE
Release: x
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt/glite
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the yaim functions necessary to configure SGE utils.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(0644,root,root)
%{prefix}/yaim/functions/*
%{prefix}/yaim/defaults/*
%{prefix}/yaim/etc/versions/%{name}
%config(noreplace) %{prefix}/yaim/node-info.d/glite*
%{prefix}/yaim/examples/siteinfo/services/glite-* 
%{prefix}/share/man/man1/yaim-sge-utils.1
%doc LICENSE

%clean
rm -rf %{buildroot}
