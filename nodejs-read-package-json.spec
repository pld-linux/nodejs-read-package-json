%define		pkg	read-package-json
Summary:	The thing npm uses to read package.json files with semantics and defaults and validation
Name:		nodejs-%{pkg}
Version:	1.2.4
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	b34c94cc5e8f4902293618af162d0d6d
URL:		https://github.com/isaacs/read-package-json
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-glob < 5
Requires:	nodejs-glob >= 4.0.2
Requires:	nodejs-lru-cache < 3
Requires:	nodejs-lru-cache >= 2
Requires:	nodejs-normalize-package-data < 0.5
Requires:	nodejs-normalize-package-data >= 0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The thing npm uses to read package.json files with semantics and
defaults and validation.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json read-json.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
