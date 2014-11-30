Name: hadoop
Version: 2.5.1
Release: 1
Summary: The Apache Hadoop project develops open-source software for reliable, scalable, distributed computing
License: Apache License, Version 2.0
URL: http://hadoop.apache.org/core/
Source: http://apache.uib.no/hadoop/common/stable/hadoop-%{version}.tar.gz
#Source0: %{name}-%{version}.tar.gz
Vendor: Apache Software Foundation
Group: Development/Libraries
Requires: sh-utils, textutils, /usr/sbin/useradd, /usr/sbin/usermod, /sbin/chkconfig, /sbin/service
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}/
#Prefix: /usr/local/${name}

%define debug_package %{nil}

%define _unpackaged_files_terminate_build 1

%define _prefix      /usr/local/hadoop
%define _bin_dir     %{_prefix}/bin
%define _conf_dir    %{_prefix}/etc/hadoop
%define _include_dir %{_prefix}/include
%define _lib_dir     %{_prefix}/lib
%define _libexec_dir %{_prefix}/libexec
%define _sbin_dir    %{_prefix}/sbin
%define _share_dir   %{_prefix}/share

%description
%{summary}

%prep
%setup
getent group hadoop >/dev/null || groupadd -r hadoop
getent passwd hadoop >/dev/null || /usr/sbin/useradd --comment "Hadoop" --shell /bin/bash -M -r -g hdfs -G hadoop

%build

%install
mkdir -p "$RPM_BUILD_ROOT%{_prefix}"
cp -R * "$RPM_BUILD_ROOT%{_prefix}"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%doc %{_prefix}/LICENSE.txt
%doc %{_prefix}/NOTICE.txt
%doc %{_prefix}/README.txt
%config(noreplace) %{_conf_dir}/capacity-scheduler.xml
%config(noreplace) %{_conf_dir}/configuration.xsl
%config(noreplace) %{_conf_dir}/container-executor.cfg
%config(noreplace) %{_conf_dir}/core-site.xml
%config(noreplace) %{_conf_dir}/hadoop-env.cmd
%config(noreplace) %{_conf_dir}/hadoop-env.sh
%config(noreplace) %{_conf_dir}/hadoop-metrics.properties
%config(noreplace) %{_conf_dir}/hadoop-metrics2.properties
%config(noreplace) %{_conf_dir}/hadoop-policy.xml
%config(noreplace) %{_conf_dir}/hdfs-site.xml
%config(noreplace) %{_conf_dir}/httpfs-env.sh
%config(noreplace) %{_conf_dir}/httpfs-log4j.properties
%config(noreplace) %{_conf_dir}/httpfs-signature.secret
%config(noreplace) %{_conf_dir}/httpfs-site.xml
%config(noreplace) %{_conf_dir}/log4j.properties
%config(noreplace) %{_conf_dir}/mapred-env.cmd
%config(noreplace) %{_conf_dir}/mapred-env.sh
%config(noreplace) %{_conf_dir}/slaves
%config(noreplace) %{_conf_dir}/yarn-env.cmd
%config(noreplace) %{_conf_dir}/yarn-env.sh
%config(noreplace) %{_conf_dir}/yarn-site.xml
%{_conf_dir}/mapred-queues.xml.template
%{_conf_dir}/mapred-site.xml.template
%{_conf_dir}/ssl-client.xml.example
%{_conf_dir}/ssl-server.xml.example
%{_bin_dir}
%{_include_dir}
%{_lib_dir}
%{_libexec_dir}
%{_sbin_dir}
%{_share_dir}
