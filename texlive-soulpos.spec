Name:		texlive-soulpos
Version:	60772
Release:	2
Summary:	A fancy means of underlining
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/soulpos
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soulpos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soulpos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package combines the use of soul with the savepos mechanism
of current pdfTeX so that the user can create (almost)
arbitrary underlining and similar "decorations", including
rules, leaders and even pictures (pgf, pstricks, etc.). Unlike
soul underlines, which are built by repeating small elements,
here each chunk of text to be underlined is a single element.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/soulpos
%doc %{_texmfdistdir}/doc/latex/soulpos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
