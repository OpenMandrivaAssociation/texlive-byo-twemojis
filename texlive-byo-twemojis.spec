Name:		texlive-byo-twemojis
Version:	58917
Release:	2
Summary:	"Build Your Own Twemojis" with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/byo-twemojis
License:	cc-by-4 lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the means to create your own emojis (the
simple, round, and mostly yellow ones) from elements of
existing emojis. The provided command creates a TikZ picture
from the stated elements with multiple possibilities to modify
the result in color and position.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/byo-twemojis
%{_texmfdistdir}/tex/latex/byo-twemojis
%doc %{_texmfdistdir}/doc/latex/byo-twemojis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
