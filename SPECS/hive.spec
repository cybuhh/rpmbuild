Name: hive
Version: 0.14.0
Release: 1
Summary: Hive is a data warehouse infrastructure built on top of Hadoop
License: ASL 2.0
URL: http://hive.apache.org
Source: http://apache.uib.no/hive/hive-%{version}/apache-hive-%{version}-bin.tar.gz
Group: Development/Libraries
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}/

%define debug_package %{nil}

%define _unpackaged_files_terminate_build 1

%define prefix      /usr/lib
%define app_dir     %{prefix}/%{name}
%define bin_dir     %{app_dir}/bin
%define conf_dir    %{app_dir}/conf
%define examples    %{app_dir}/examples
%define hcatalog    %{app_dir}/hcatalog
%define lib_dir     %{app_dir}/lib
%define scripts     %{app_dir}/scripts

%description
%{summary}

%prep
%setup -q -n apache-%{name}-%{version}-bin

%build

%install
mkdir -p "$RPM_BUILD_ROOT%{app_dir}"
cp -R * "$RPM_BUILD_ROOT%{app_dir}"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%doc %{app_dir}/LICENSE
%doc %{app_dir}/NOTICE
%doc %{app_dir}/README.txt
%doc %{app_dir}/RELEASE_NOTES.txt
%config %{conf_dir}/beeline-log4j.properties.template
%config %{conf_dir}/hive-default.xml.template
%config %{conf_dir}/hive-env.sh.template
%config %{conf_dir}/hive-exec-log4j.properties.template
%config %{conf_dir}/hive-log4j.properties.template

%{bin_dir}
%{examples}
%{hcatalog}
%{lib_dir}
%{scripts}

