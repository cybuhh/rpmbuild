%define major 2
%define minor 2
%define patchlevel 0

Name: ruby22
Version: %{major}.%{minor}.%{patchlevel}
Release: 1
Summary: An interpreter of object-oriented scripting language
License: Ruby License/GPL - see COPYING
URL: http://www.ruby-lang.org/
Source: http://cache.ruby-lang.org/pub/ruby/2.2/ruby-%{version}.tar.gz
#Source0: %{name}-%{version}.tar.gz
Vendor: Ruby community
Group: Development/Languages
Requires: gcc glibc libyaml openssl libffi
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}/
Provides: ruby(abi) = 2.2
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
#Obsoletes: ruby
#Obsoletes: ruby-libs
#Obsoletes: ruby-irb
#Obsoletes: ruby-rdoc
#Obsoletes: ruby-devel
#Obsoletes: rubygems

%define debug_package %{nil}
%define _unpackaged_files_terminate_build 1

%define prefix      /opt/ruby
%define app_dir     %{prefix}/%{major}.%{minor}
%define bin_dir     %{app_dir}/bin
%define lib_dir     %{app_dir}/share/ruby
%define include_dir %{app_dir}/include/ruby

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

########################################
# Prepare
########################################
%prep
%setup -n ruby-%{version}

########################################
# Build
########################################
%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure --prefix=%{app_dir} --with-destdir=%{app_dir} --enable-load-relative

make

########################################
# Install
########################################
%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

########################################
# List of files
########################################
%files
%defattr(-,root,root,-)
%{app_dir}
