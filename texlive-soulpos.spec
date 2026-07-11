%global tl_name soulpos
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A fancy means of underlining
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/soulpos
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soulpos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soulpos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(oberdiek)
Requires:	texlive(soul)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package combines the use of soul with the savepos mechanism of
current pdfTeX so that the user can create (almost) arbitrary
underlining and similar "decorations", including rules, leaders and even
pictures (pgf, pstricks, etc.). Unlike soul underlines, which are built
by repeating small elements, here each chunk of text to be underlined is
a single element.

