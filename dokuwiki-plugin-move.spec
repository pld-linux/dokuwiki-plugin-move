%define		subver	2015-10-17
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		move
Summary:	Move pages, media files and namespaces while maintaining the link structure
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/michitux/dokuwiki-plugin-move/archive/%{subver}/%{plugin}-%{version}.tar.gz
# Source0-md5:	4583d7081f21c3aa2dbd860557134ecd
URL:		https://www.dokuwiki.org/plugin:move
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	dokuwiki >= 20131208
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
mv dokuwiki-plugin-move-*/* .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.js
%{plugindir}/*.less
%{plugindir}/*.txt
%{plugindir}/action
%{plugindir}/admin
%{plugindir}/conf
%{plugindir}/helper
%{plugindir}/images
%{plugindir}/script

%dir %{plugindir}/lang
%{plugindir}/lang/en
%lang(cs) %{plugindir}/lang/cs
%lang(de) %{plugindir}/lang/de
%lang(es) %{plugindir}/lang/es
%lang(fr) %{plugindir}/lang/fr
%lang(it) %{plugindir}/lang/it
%lang(ja) %{plugindir}/lang/ja
%lang(ko) %{plugindir}/lang/ko
%lang(lv) %{plugindir}/lang/lv
%lang(nl) %{plugindir}/lang/nl
%lang(no) %{plugindir}/lang/no
%lang(pl) %{plugindir}/lang/pl
%lang(ru) %{plugindir}/lang/ru
%lang(sl) %{plugindir}/lang/sl
%lang(sv) %{plugindir}/lang/sv
%lang(zh_CN) %{plugindir}/lang/zh
