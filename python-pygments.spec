#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define module	pygments
Summary:	A generic syntax highlighter as Python 2.x module
Summary(pl.UTF-8):	Moduł Pythona 2.x do ogólnego podświetlania składni
Name:		python-%{module}
Version:	2.0.2
Release:	6
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/pypi/Pygments
Source0:	http://pypi.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
# Source0-md5:	238587a1370d62405edabd0794b3ec4a
Patch0:		rpmspec.patch
URL:		http://pygments.org/
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
Requires:	python-modules
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
Requires:	python3-modules
Requires:	python3-setuptools

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

%prep
%setup -q -n Pygments-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

mv $RPM_BUILD_ROOT%{_bindir}/pygmentize{,-2}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%if %{with python3}
%py3_install

mv $RPM_BUILD_ROOT%{_bindir}/pygmentize{,-3}
%endif

%if %{with python2}
ln -sf pygmentize-2 $RPM_BUILD_ROOT%{_bindir}/pygmentize
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE TODO
%attr(755,root,root) %{_bindir}/pygmentize
%attr(755,root,root) %{_bindir}/pygmentize-2
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE TODO
%attr(755,root,root) %{_bindir}/pygmentize-3
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif
