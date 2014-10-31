# Avoid unnecessary debug-information (native code)
%define	debug_package %{nil}
# Avoid jar repack (brp-java-repack-jars)
%define __jar_repack 0
%define __os_install_post %{nil}
%define __portsed sed -i
%define _binaries_in_noarch_packages_terminate_build 0
%define appname         activemq
%define appusername     activemq
%define appuserid       92
%define appgroupid      92
%define appdir          /opt/%{appname}
%define appdirwv        /opt/%{appname}-%{version}
%define applogdir       %{_var}/log/%{appname}
%define appconfdir      %{_sysconfdir}/%{appname}
%define _initrddir       %{_sysconfdir}/init.d

Name: activemq
Version: 5.9.0 
Release: 1
Summary: Apache ActiveMQ is the most popular and powerful open source messaging and Integration Patterns server. 
Group: System Environment/Daemons
URL: http://activemq.apache.org
License: Apache-2.0
BuildArch: noarch
Source0: apache-activemq-%{version}-bin.tar.gz
Source1: activemq.sysconfig
BuildRoot: %{_tmppath}/build-%{name}-%{version}-%{release}
Requires: java >= 1:1.6.0
Vendor: Mohan Balasundaram

Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%description
Apache ActiveMQ ™ is the most popular and powerful open source messaging and Integration Patterns server.

Apache ActiveMQ is fast, supports many Cross Language Clients and Protocols, 
comes with easy to use Enterprise Integration Patterns and many advanced features
while fully supporting JMS 1.1 and J2EE 1.4. Apache ActiveMQ is released under the Apache 2.0 License

%prep
%setup -q -c

%build

%install
# Prep the install location.
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{appconfdir}
mkdir -p %{buildroot}%{appdirwv}
mkdir -p %{buildroot}%{applogdir}

# Copy activemq files
mv apache-activemq-%{version}/* %{buildroot}%{appdirwv}/

#Create symlinks
cd %{buildroot}/opt
ln -s %{appdirwv} %{appname}
cd %{buildroot}%{appconfdir}
ln -s %{appdir}/conf conf
cd %{buildroot}%{_initrddir}
ln -s %{appdir}/bin/%{appname} %{appname}

%clean
rm -rf %{buildroot}

%pre
# First install time, add user and group
if [ "$1" == "1" ]; then
  %{_sbindir}/groupadd -r -g %{appgroupid} %{appusername} 2>/dev/null || :
  %{_sbindir}/useradd -s /sbin/nologin -c "%{appname} user" -g %{appusername} -r -d %{appdatadir} -u %{appuserid} %{appusername} 2>/dev/null || :
else
# Update time, stop service if running
  #stop service logic to be written
fi

%post

%preun

%postun

%files
%defattr(-,%{appusername},%{appusername})
%dir %{appdirwv}
%doc %{appdirwv}/NOTICE
%doc %{appdirwv}/README.txt
%doc %{appdirwv}/LICENSE
%attr(0755,%{appusername},%{appusername}) %dir %{applogdir}
#%attr(0755, root,root) %{_initrddir}/%{appname}
%defattr(-,root,root)
%dir %{_sysconfdir}/sysconfig
#%config(noreplace) %{_sysconfdir}/sysconfig/%{appname}
%{appconfdir}
%{_initrddir}/%{appname}
%{appdirwv}
%{appdir}
%{applogdir}


%changelog
* Wed Oct 29 2014 mohan@nerdplanet.co.uk 5.9.0
- Initial RPM
