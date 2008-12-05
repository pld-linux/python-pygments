
%define module pygments
Summary:	Generic syntax highlighter
Name:		python-%{module}
Version:	1.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
# Source0-md5:	70c40ff5331460cabfcb24f86a8d451d
URL:		http://pygments.org/
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pygments is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need to
prettify source code. Highlights are
- a wide range of common languages and markup formats is supported
- special attention is paid to details that increase highlighting quality
- support for new languages and formats are added easily; most languages
  use a simple regex-based lexing mechanism
- a number of output formats is available, among them HTML, RTF, LaTeX and
  ANSI sequences
- it is usable as a command-line tool and as a library
- ... and it highlights even Brainf*ck!

%prep
%setup -q -n Pygments-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*Pygments*.egg*
