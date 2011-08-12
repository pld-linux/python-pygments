#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
#
%define module	pygments
Summary:	A generic syntax highlighter as Python 2.x module
Summary(pl.UTF-8):	Moduł Pythona 2.x do ogólnego podświetlania składni
Name:		python-%{module}
Version:	1.4
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
# Source0-md5:	d77ac8c93a7fb27545f2522abe9cc462
URL:		http://pygments.org/
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Provides:	python-Pygments
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

%build
%if %{with python2}
%{__python} setup.py build -b build-2
%endif

%if %{with python3}
%{__python3} setup.py build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build -b build-2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/pygmentize{,-2}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build -b build-3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

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
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE TODO
%attr(755,root,root) %{_bindir}/pygmentize-3
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Pygments-%{version}-py*.egg-info
%endif
