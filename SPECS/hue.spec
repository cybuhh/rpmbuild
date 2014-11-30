Name: hue
Version: 3.7.1
Release: 1
Summary: The hue metapackage
License: ASL 2.0
URL: http://github.com/cloudera/hue
Source: https://github.com/cloudera/hue/archive/release-%{version}.tar.gz
Group: Applications/Engineering
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}/
AutoProv: no
AutoReqProv: no
%define _use_internal_dependency_generator 0

# Disable post hooks (brp-repack-jars, etc) that just take forever and sometimes cause issues
%define __os_install_post \
    %{!?__debug_package:/usr/lib/rpm/brp-strip %{__strip}} \
%{nil}
%define __jar_repack %{nil}
%define __prelink_undo_cmd %{nil}

# Disable debuginfo package, since we never need to gdb
# our own .sos anyway
%define debug_package %{nil}

# there are some file by-products we don't want to actually package
%define _unpackaged_files_terminate_build 0

%define debug_package %{nil}

%define _python_bytecompile_errors_terminate_build 0

%define _prefix      /usr/local/hue
%define _apps_dir    %{_prefix}/apps
%define _build_dir   %{_prefix}/build
%define _data_dir    %{_prefix}/data
%define _dist_dir    %{_prefix}/dist
%define _desktop_dir %{_prefix}/desktop
%define _docs_dir    %{_prefix}/docs
%define _ext_dir     %{_prefix}/ext
%define _log_dir     %{_prefix}/logs
%define _maven_dir   %{_prefix}/maven
%define _tools_dir   %{_prefix}/tools

%define _sys_lib_dir /var/lib/hue
%define _sys_log_dir /var/log/hue

%define username hue

%description
%{summary}

########################################
# Prepare
########################################
%prep
%setup -q -n hue-release-%{version}

########################################
# Build
########################################
%build
make apps
bash tools/relocatable.sh

########################################
# Preinstall
########################################
%pre
getent group %{username} 2>/dev/null >/dev/null || /usr/sbin/groupadd -r %{username}
getent passwd %{username} 2>&1 > /dev/null || /usr/sbin/useradd -c "Hue" -s /sbin/nologin -g %{username} -r -d %{_prefix} %{username} 2> /dev/null || :

########################################
# Install
########################################
%install
mkdir -p "$RPM_BUILD_ROOT%{_prefix}"
cp -R * "$RPM_BUILD_ROOT%{_prefix}"

echo "SYS_PYTHON=`python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))'`" > "$RPM_BUILD_ROOT%{_prefix}/Makefile.buildvars"
echo "SKIP_PYTHONDEV_CHECK=1" >> "$RPM_BUILD_ROOT%{_prefix}/Makefile.buildvars"

########################################
# Clean
########################################
%clean
rm -rf "$RPM_BUILD_ROOT"

########################################
# Postinstall
########################################
# If there is an old DB in place, make a backup.
%post

if [ -e %{_prefix}/desktop/desktop.db ]; then
  echo "Backing up previous version of Hue database..."
  cp -a %{_prefix}/desktop/desktop.db %{_prefix}/desktop/desktop.db.rpmsave.$(date +'%Y%m%d.%H%M%S')
fi

test -d %{_sys_lib_dir} || mkdir %{_sys_lib_dir}
test -d %{_sys_log_dir} || mkdir %{_sys_log_dir}
chown -R hue:hue %{_sys_log_dir} %{_sys_lib_dir} %{_desktop_dir}
ln -s "%{_sys_log_dir}" "%{_log_dir}"

########################################
# List of files
########################################
%files
%defattr(-,root,root,-)
%doc %{_prefix}/NOTICE.txt
%doc %{_prefix}/LICENSE.txt
%doc %{_prefix}/README.rst
%doc %{_prefix}/VERSION

%{_prefix}/Makefile
%{_prefix}/Makefile.buildvars
%{_prefix}/Makefile.sdk
%{_prefix}/Makefile.tarball
%{_prefix}/Makefile.vars
%{_prefix}/Makefile.vars.priv
%{_prefix}/app.reg

%{_apps_dir}
%{_build_dir}
%{_data_dir}
%{_desktop_dir}
%{_dist_dir}
%{_docs_dir}
%{_ext_dir}
%{_maven_dir}
%{_tools_dir}

