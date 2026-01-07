%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg universal-indent-gui-tqt
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.2.0
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	GUI frontend for several code beautifiers
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/trinity/pkgconfig
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:  pkgconfig(tqscintilla)
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	libtool

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig


%description
UniversalIndentGui is a GUI fontend for several code beautifiers, currently
supporting:
 * Artistic Styler
 * BCPP
 * Cobol Beautify
 * CSSTidy
 * Fortran 90 PPR
 * GNU Indent
 * GreatCode
 * hindent
 * HTB
 * Javascript Decoder
 * JSPPP
 * Perl Tidy
 * PHP_Beautifier
 * PHP Code Beautifier
 * PHP Stylist
 * pindent
 * Ruby Beautify
 * Ruby Formatter
 * Shell Indent
 * (HTML) Tidy
 * Uncrustify
 * XML Indent

UniversalIndentGui allows you to tune a beautifier's configuration and see
how the changes affects a source example live. It is especially useful to
compare different C/C++ beautifiers when you have to choose one of them.


%prep -a
rm -f src/svnqt/CMakeLists.txt.orig
#rm -fr src/svnqt/cache/sqlite3/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export CMAKE_INCLUDE_PATH="%{tde_prefix}/include/tde"


%files
%defattr(-,root,root,-)
%{tde_prefix}/bin/universal-indent-gui-tqt
%{tde_prefix}/share/universal-indent-gui-tqt/

