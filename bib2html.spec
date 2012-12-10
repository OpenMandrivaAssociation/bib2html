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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 6.5-2mdv2011.0
+ Revision: 616752
- the mass rebuild of 2010.0 packages

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.5-1mdv2010.0
+ Revision: 397013
- update

* Sun Mar 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.4-1mdv2009.1
+ Revision: 355514
- update to new version 6.4

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.3-1mdv2009.1
+ Revision: 354935
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 6.1-3mdv2009.0
+ Revision: 243215
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 6.1-1mdv2008.1
+ Revision: 135829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Funda Wang <fwang@mandriva.org> 6.1-1mdv2008.0
+ Revision: 46361
- New version


* Sun Jan 07 2007 Pascal Terjan <pterjan@mandriva.org> 5.1-1mdv2007.0
+ Revision: 105171
- 5.1
- Install the pod files so thet -h/--man work
- Install to standard perl dir
- Ship the new bib2sql

  + Lenny Cartier <lenny@mandriva.com>
    - Import bib2html

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.3-2mdv2007.0
- fix perms

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.3-1mdv2007.0
- New release 4.3
- %%mkrel
- FHS setup

* Mon Feb 21 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.3-1mdk
- 3.3

* Fri Feb 04 2005 Abel Cheung <deaddog@mandrake.org> 3.2-1mdk
- First version adopted into Mandrakelinux, thx to Stephane's work

* Mon Dec 06 2004 Stephane <galland@arakhne.org> 3.1-1mdk
- Joao has added the Portuguese language support.
- Bug fix: the name of the language passed by '--lang' is
  now case-insensitive.

* Fri Dec 03 2004 Stephane <galland@arakhne.org> 3.0-1mdk
- More TeX commands are added by Dimitris:
  \epsilon, \Epsilon, \mathbf, \mathit, \mathrm,
  \mathsf, \mathtt, \mathnormal, \sqrt
- Create a XML generator which respect the DTD from
  BibTeXML.
- Add an XML output inside the HTML generator.
- Bug fix: the character '+' is not allowed inside the entry keys.

* Fri Nov 26 2004 Stephane <galland@arakhne.org> 2.0-1mdk
- FIRST RELEASE FOR MANDRAKE
- Spanish is included into the generators.
- Links to the author's list of publication was
  added for each other inside the entry's field
  list.
- The option '--checknames' permits to check if
  some author's names are duplicated or contain
  mistakes.
- Bug fixes.

* Fri Nov 12 2004 Stephane <galland@arakhne.org> 1.5-1
- sometimes the carriage return characters was
  not supported by the BibTeX parser.
- Generation of the BibTeX short labels (eg. [ABC04])
  produces too long labels in case a lot of
  names was proposed to the function.
- The names of the authors are not well upper-cased
  for each first letter of the words.
- if an error occurs during the copy of a pdf file,
  bib2html will not failed but only warm the user.

* Thu Sep 23 2004 Stephane <galland@arakhne.org> 1.4-1
- Fix the bug that copy the electronical file when
  the Extended generator's parameter "targt-url"
  was specified.

* Tue Aug 24 2004 Stephane <galland@arakhne.org> 1.3-1
- Lot of bug fixes
- Add the BibTeX's entry types 'proceedings' and 'unpublished'
- Add a documentation

* Fri Aug 20 2004 Stephane <galland@arakhne.org> 1.2-2
- Fix the file's permissions in this package.
- Add a UNIX manual page

* Wed Aug 18 2004 Stephane <galland@arakhne.org> 1.2-1
- Fix a bug in the BibTeX parser which prevents to
  properly scan the @comment
- Allow a comment line to finish the BibTeX file
  without any carriage return character.

* Tue Mar 30 2004 Stephane <galland@arakhne.org> 1.1-1
- add verbatim generation of BibTeX code
- Many bug fixes

* Fri Mar 19 2004 Stephane <galland@arakhne.org> 1.0-1
- First stable release

* Wed Feb 25 2004 Stephane <galland@arakhne.org> 0.11-1
- add an index of authors and of author's publications inside
  the two left frames
- add the class AbstractGenerator.pm
- add ExtendedGen.pm which permits to generate HTML page with:
  a) isbn, issn, and readers
  b) abstract and keywords
  c) the support for downloading an electronic
     document ('localfile')
- add the support of LaTeX environments (\begin,\end)
- add the generator Domain which permits to support domain
  for documents (domain,nddomain,rddomain,domains)
- Bug fixes

