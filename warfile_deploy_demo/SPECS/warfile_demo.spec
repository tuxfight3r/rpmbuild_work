# Avoid unnecessary debug-information (native code)¬                                                                    
%define▸debug_package %{nil}
# Avoid jar repack (brp-java-repack-jars)
%define __jar_repack 0
%define __os_install_post %{nil}
%define __portsed sed -i
%define _binaries_in_noarch_packages_terminate_build 0
%define webappdir /opt/tomcat/webapps
%define appuser tomcat

Name: warfile_demo
Version: 1.0
Release: 1
Summary: Deploying WAR files via rpm demo.
Group: System Environment/Daemons
URL: http://www.primoitsolutions.uk
License: Apache-2.0
BuildArch: noarch
Source0: app1.war
Source1: app2.war
BuildRoot: %{_tmppath}/build-%{name}-%{version}-%{release}¬
Requires: java >= 1:1.6.0
Requires: tomcat
Vendor: Mohan Balasundaram

%description
To deploy multiple warfiles via one rpm package

%prep
%setup -q -T -c

%install
install -m 0755 -d %{buildroot}/%{webappdir}
install -m 0644 %{SOURCE0} %{buildroot}%{webappdir}/
install -m 0644 %{SOURCE1} %{buildroot}%{webappdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644, %{appuser}, %{appuser}, 0755)
%{webappdir}/app1.war
%{webappdir}/app2.war

%doc

%pre

%post

%changelog
* Fri Feb 06 2015 mohan@primoitsolutions.uk
- Updated spec file with dependencies
* Wed Oct 29 2014 mohan@primoitsolutions.uk 
- Initial RPM
