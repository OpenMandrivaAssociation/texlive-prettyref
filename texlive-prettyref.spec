Name:		texlive-prettyref
Version:	15878
Release:	2
Summary:	Make label references "self-identify"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prettyref
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Prettyref provides a command \newrefformat, which specifies the
way in which a reference is typeset, according to a label
"identification". The identification is set in the \label
command, by using prefixed label names; so instead of
\label{mysection}, one uses \label{sec:mysection}, and
prettyref interprets the "sec:" part. The package is compatible
with hyperref and with other packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/prettyref/prettyref.sty
%doc %{_texmfdistdir}/doc/latex/prettyref/README
%doc %{_texmfdistdir}/doc/latex/prettyref/prettyref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/prettyref/prettyref.dtx
%doc %{_texmfdistdir}/source/latex/prettyref/prettyref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
