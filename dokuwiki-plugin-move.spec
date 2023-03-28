%define		subver	2022-01-23
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		move
%define		php_min_version 5.3.0
Summary:	Move pages, media files and namespaces while maintaining the link structure
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/michitux/dokuwiki-plugin-move/archive/%{subver}/%{plugin}-%{subver}.tar.gz
# Source0-md5:	b6ac00200df22eb9b76376ef240fb7b7
URL:		https://www.dokuwiki.org/plugin:move
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(find_lang) >= 1.41
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin allows to move pages and namespaces including media files
and automatically adjusts all links and media references that point to
these pages. Unlike the old pagemove plugin this plugin uses the
DokuWiki parser which allows it to correctly identify all links and
nothing else.

Parts of this plugin like some of the translated strings, some parts
of the structure of the code and parts of the user interface have been
taken from the old pagemove plugin by Gary Owen, Arno Puschmann and
Christoph Jähnigen.

Warning: This plugin does not update ACL rules. For example if you had
an ACL rule that read-protected a certain wiki page this rule won't
have any effect anymore after moving that page.

%prep
%setup -qc
mv *-%{plugin}-*/{.??*,*} .

rm .github/workflows/phpTestLinux.yml
rm deleted.files

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%{__rm} $RPM_BUILD_ROOT%{plugindir}/README
%{__rm} -r $RPM_BUILD_ROOT%{plugindir}/_test

%find_lang %{name}.lang --with-dokuwiki

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.js
%{plugindir}/*.less
%{plugindir}/*.php
%{plugindir}/*.svg
%{plugindir}/*.txt
%{plugindir}/action
%{plugindir}/admin
%{plugindir}/conf
%{plugindir}/helper
%{plugindir}/images
%{plugindir}/script
