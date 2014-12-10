Name: hadoop
Version: 2.6.0
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

%define debug_package %{nil}
%define _unpackaged_files_terminate_build 1

%define prefix      /usr/lib
%define app_dir     %{prefix}/%{name}
%define bin_dir     %{app_dir}/bin
%define logs_dir    %{app_dir}/logs
%define conf_dir    %{app_dir}/etc/hadoop
%define include_dir %{app_dir}/include
%define lib_dir     %{app_dir}/lib
%define libexec_dir %{app_dir}/libexec
%define sbin_dir    %{app_dir}/sbin
%define share_dir   %{app_dir}/share

%define etc_profile /etc/profile.d

%define etc_hadoop /etc/hadoop
%define log_hadoop /var/log/hadoop

%define app_user              hadoop
%define app_group             hadoop
%define app_user_comment      Hadoop

%description
%{summary}

########################################
# Prepare
########################################
%prep
%setup

########################################
# Build
########################################
%build

########################################
# Install
########################################
%install
mkdir -p $RPM_BUILD_ROOT%{app_dir} $RPM_BUILD_ROOT%{etc_profile}
cp -R * $RPM_BUILD_ROOT%{app_dir}
(   echo 'export PATH=$PATH:%{bin_dir}'
    echo 'export HADOOP_HOME=%{app_dir}'
) > $RPM_BUILD_ROOT%{etc_profile}/%{name}.sh

########################################
# Preinstall
########################################
%pre
getent group %{app_group} >/dev/null || sudo groupadd -r %{app_group}
getent passwd %{app_user} >/dev/null || sudo useradd --comment "%{app_user_comment}" -g %{app_group} %{app_user}

%clean
rm -rf "$RPM_BUILD_ROOT"

########################################
# Postinstall
########################################
%post

test -d %{log_hadoop} || mkdir %{log_hadoop}
chown -R %{app_user}:%{app_group} %{log_hadoop}
ln -sf %{log_hadoop} %{logs_dir}
ln -sf %{conf_dir} %{etc_hadoop}

########################################
# List of files
########################################
%files
%defattr(-,root,root,-)
%doc %{app_dir}/LICENSE.txt
%doc %{app_dir}/NOTICE.txt
%doc %{app_dir}/README.txt
%config(noreplace) %{conf_dir}/capacity-scheduler.xml
%config(noreplace) %{conf_dir}/configuration.xsl
%config(noreplace) %{conf_dir}/container-executor.cfg
%config(noreplace) %{conf_dir}/core-site.xml
%config(noreplace) %{conf_dir}/hadoop-env.cmd
%config(noreplace) %{conf_dir}/hadoop-env.sh
%config(noreplace) %{conf_dir}/hadoop-metrics.properties
%config(noreplace) %{conf_dir}/hadoop-metrics2.properties
%config(noreplace) %{conf_dir}/hadoop-policy.xml
%config(noreplace) %{conf_dir}/hdfs-site.xml
%config(noreplace) %{conf_dir}/httpfs-env.sh
%config(noreplace) %{conf_dir}/httpfs-log4j.properties
%config(noreplace) %{conf_dir}/httpfs-signature.secret
%config(noreplace) %{conf_dir}/httpfs-site.xml
%config(noreplace) %{conf_dir}/kms-acls.xml
%config(noreplace) %{conf_dir}/kms-env.sh
%config(noreplace) %{conf_dir}/kms-log4j.properties
%config(noreplace) %{conf_dir}/kms-site.xml
%config(noreplace) %{conf_dir}/log4j.properties
%config(noreplace) %{conf_dir}/mapred-env.cmd
%config(noreplace) %{conf_dir}/mapred-env.sh
%config(noreplace) %{conf_dir}/slaves
%config(noreplace) %{conf_dir}/yarn-env.cmd
%config(noreplace) %{conf_dir}/yarn-env.sh
%config(noreplace) %{conf_dir}/yarn-site.xml
%{conf_dir}/mapred-queues.xml.template
%{conf_dir}/mapred-site.xml.template
%{conf_dir}/ssl-client.xml.example
%{conf_dir}/ssl-server.xml.example
%{bin_dir}
%{include_dir}
%{lib_dir}
%{libexec_dir}
%{sbin_dir}
%{share_dir}
%{etc_profile}/%{name}.sh