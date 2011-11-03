Name:		texlive-prettyref
Version:	3.0
Release:	1
Summary:	Make label references "self-identify"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prettyref
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prettyref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Prettyref provides a command \newrefformat, which specifies the
way in which a reference is typeset, according to a label
"identification". The identification is set in the \label
command, by using prefixed label names; so instead of
\label{mysection}, one uses \label{sec:mysection}, and
prettyref interprets the "sec:" part. The package is compatible
with hyperref and with other packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
