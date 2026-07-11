%global tl_name prettyref
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Make label references self-identify
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prettyref
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prettyref provides a command \newrefformat, which specifies the way in
which a reference is typeset, according to a label "identification". The
identification is set in the \label command, by using prefixed label
names; so instead of \label{mysection}, one uses \label{sec:mysection},
and prettyref interprets the "sec:" part. The package is compatible with
hyperref and with other packages.

