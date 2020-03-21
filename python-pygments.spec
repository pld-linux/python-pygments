#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define module	pygments
Summary:	A generic syntax highlighter as Python 2.x module
Summary(pl.UTF-8):	Moduł Pythona 2.x do ogólnego podświetlania składni
Name:		python-%{module}
Version:	2.5.2
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/pygments/
Source0:	https://files.pythonhosted.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
# Source0-md5:	465a35559863089d959d783a69f79b9f
Patch0:		rpmspec.patch
URL:		http://pygments.org/
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
Requires:	python-setuptools
Provides:	python-Pygments = %{version}-%{release}
Obsoletes:	python-Pygments
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pygments is a generic syntax highlighter for general use in all kinds
of software such as forum systems, wikis or other applications that
need to prettify source code. Highlights are:
- a wide range of common languages and markup formats is supported
- special attention is paid to details that increase highlighting
  quality
- support for new languages and formats are added easily; most
  languages use a simple regex-based lexing mechanism
- a number of output formats is available, among them HTML, RTF, LaTeX
  and ANSI sequences
- it is usable as a command-line tool and as a library
- ... and it highlights even Brainf*ck!

%description -l pl.UTF-8
Pygments to moduł Pythona do podświetlania składni ogólnego
przeznaczenia we wszelkiego rodzaju programach, takich jaka systemy
forów, wiki i inne plikacje wymagające ładnego wyświetlania kodu
źródłowego. Zalety Pygments to:
- obsługiwany szeroki zakres popularnych języków i formatów znaczników
- zwrócenie szczególnej uwagi na szczegóły zwiększające jakość
  podświetlania
- łatwa obsługa nowych języków i formatów; większość języków
  wykorzystuje prosty mechanizm analizy leksykalnej oparty o wyrażenia
  regularne
- dostępność wielu formatów wyjściowych, m.in. HTML, RTF, LaTeX i
  sekwencje ANSI
- możliwość używania z linii poleceń oraz jako biblioteki
- ...a także - podświetla nawet Brainf*cka!

%package -n python3-%{module}
Summary:	Generic syntax highlighter as Python 3.x module
Summary(pl.UTF-8):	Moduł Pythona 3.x do ogólnego podświetlania składni
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5
Requires:	python3-setuptools
Conflicts:	python-pygments < 2.5.2

%description -n python3-%{module}
Pygments is a generic syntax highlighter for general use in all kinds
of software such as forum systems, wikis or other applications that
need to prettify source code. Highlights are
- a wide range of common languages and markup formats is supported
- special attention is paid to details that increase highlighting
  quality
- support for new languages and formats are added easily; most
  languages use a simple regex-based lexing mechanism
- a number of output formats is available, among them HTML, RTF, LaTeX
  and ANSI sequences
- it is usable as a command-line tool and as a library
- ... and it highlights even Brainf*ck!

%description -n python3-%{module} -l pl.UTF-8
Pygments to moduł Pythona do podświetlania składni ogólnego
przeznaczenia we wszelkiego rodzaju programach, takich jaka systemy
forów, wiki i inne plikacje wymagające ładnego wyświetlania kodu
źródłowego. Zalety Pygments to:
- obsługiwany szeroki zakres popularnych języków i formatów znaczników
- zwrócenie szczególnej uwagi na szczegóły zwiększające jakość
  podświetlania
- łatwa obsługa nowych języków i formatów; większość języków
  wykorzystuje prosty mechanizm analizy leksykalnej oparty o wyrażenia
  regularne
- dostępność wielu formatów wyjściowych, m.in. HTML, RTF, LaTeX i
  sekwencje ANSI
- możliwość używania z linii poleceń oraz jako biblioteki
- ...a także - podświetla nawet Brainf*cka!

%package apidocs
Summary:	API documentation for Python Pygments module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Pygments
Group:		Documentation

%description apidocs
API documentation for Python Pygments module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Pygments.

%prep
%setup -q -n Pygments-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pygmentize{,-2}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pygmentize{,-3}
%endif

%if %{with python3}
ln -sf pygmentize-3 $RPM_BUILD_ROOT%{_bindir}/pygmentize
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%attr(755,root,root) %{_bindir}/pygmentize-2
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%attr(755,root,root) %{_bindir}/pygmentize
%attr(755,root,root) %{_bindir}/pygmentize-3
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,docs,*.html,*.js}
%endif
