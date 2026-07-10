%global tl_name byo-twemojis
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Build Your Own Twemojis with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/byo-twemojis
License:	cc-by-4 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/byo-twemojis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the means to create your own emojis (the simple,
round, and mostly yellow ones) from elements of existing emojis. The
provided command creates a TikZ picture from the stated elements with
multiple possibilities to modify the result in color and position.

