%define		pkg	read-package-json
Summary:	The thing npm uses to read package.json files with semantics and defaults and validation
Name:		nodejs-%{pkg}
Version:	0.2.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/read-package-json
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	b162c2ee99f7e60bc4a565322dd07505
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:   nodejs-glob >= 3.1.9
Requires:   nodejs-lru-cache >= 2.0.0
Requires:   nodejs-semver >= 1.0
Requires:   nodejs-slide >= 1.1.3
Requires:   nodejs-npmlog
Requires:   nodejs-graceful-fs >= 1.1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The thing npm uses to read package.json files with semantics and defaults and validation.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json read-json.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
