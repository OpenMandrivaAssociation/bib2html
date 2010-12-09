%define name	bib2html
%define version	6.5
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	BibTeX to HTML translator
URL:		http://www.arakhne.org/bib2ml/
Source:		http://download.tuxfamily.org/arakhne/pool/b/bib2ml/bib2ml_%{version}-0arakhne2.tar.gz
License:	GPL
Group:		Publishing
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
bib2html is a script which permits to generate a set of HTML pages from a 
BibTeX database.

%prep
%setup -q -n bib2ml-%{version}

find . -type d | xargs chmod 755
find . -type f | xargs chmod 644

%build
# Build the manual pages

pod2man --section=1 --release="%{version}" --center=Bib2HTML --name=Bib2HTML man/bib2html_en.pod man/bib2html.1
pod2man --section=1 --release="%{version}" --center=Bib2HTML --name=Bib2HTML man/bib2html_fr.pod man/bib2html.fr.1
pod2man --section=1 --release="%{version}" --center=Bib2XML --name=Bib2XML man/bib2xml_en.pod man/bib2xml.1
pod2man --section=1 --release="%{version}" --center=Bib2XML --name=Bib2XML man/bib2xml_fr.pod man/bib2xml.fr.1
pod2man --section=1 --release="%{version}" --center=Bib2XML --name=Bib2XML man/bib2sql_en.pod man/bib2sql.1
pod2man --section=1 --release="%{version}" --center=Bib2XML --name=Bib2XML man/bib2sql_fr.pod man/bib2sql.fr.1

# Give the correct path to the pod files
perl -p -i -e 's/"\$basename"/"%name-%version"/' src/Bib2HTML/Main.pm

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 src/bib2html.pl %{buildroot}%{_bindir}/bib2html
install -m 755 src/bib2xml.pl %{buildroot}%{_bindir}/bib2xml
install -m 755 src/bib2sql.pl %{buildroot}%{_bindir}/bib2sql

install -d -m 755 %{buildroot}%{perl_vendorlib}
cp -pr ./src/Bib2HTML %{buildroot}%{perl_vendorlib}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/fr/man1
install -m 644 man/bib2html.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m 644 man/bib2xml.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m 644 man/bib2html.fr.1 %{buildroot}%{_mandir}/fr/man1/%{name}.1
install -m 644 man/bib2xml.fr.1 %{buildroot}%{_mandir}/fr/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog COPYING AUTHORS README doc/* man/*.pod
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*
