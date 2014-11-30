Name: hive
Version: 0.13.1
Release: 1
Summary: Hive is a data warehouse infrastructure built on top of Hadoop
License: ASL 2.0
URL: http://hive.apache.org
Source: http://apache.uib.no/hive/hive-0.13.1/apache-hive-%{version}-bin.tar.gz
Group: Development/Libraries
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}/

%define debug_package %{nil}

%define _unpackaged_files_terminate_build 1

%define _prefix      /usr/local/hive
%define _bin_dir     %{_prefix}/bin
%define _conf_dir    %{_prefix}/conf
%define _examples    %{_prefix}/examples
%define _hcatalog    %{_prefix}/hcatalog
%define _lib_dir     %{_prefix}/lib
%define _scripts     %{_prefix}/scripts


%description
%{summary}

%prep
%setup -q -n apache-%{name}-%{version}-bin

%build

%install
mkdir -p "$RPM_BUILD_ROOT%{_prefix}"
cp -R * "$RPM_BUILD_ROOT%{_prefix}"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%doc %{_prefix}/LICENSE
%doc %{_prefix}/NOTICE
%doc %{_prefix}/README.txt
%doc %{_prefix}/RELEASE_NOTES.txt
%config %{_conf_dir}/hive-default.xml.template
%config %{_conf_dir}/hive-env.sh.template
%config %{_conf_dir}/hive-exec-log4j.properties.template
%config %{_conf_dir}/hive-log4j.properties.template

%{_bin_dir}
%{_examples}
%{_hcatalog}
%{_lib_dir}
%{_scripts}

