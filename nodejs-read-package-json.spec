%define		pkg	read-package-json
Summary:	The thing npm uses to read package.json files with semantics and defaults and validation
Name:		nodejs-%{pkg}
Version:	0.1.12
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/read-package-json
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	bfde8ac1680080fd39e03450cb4a33e9
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
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
