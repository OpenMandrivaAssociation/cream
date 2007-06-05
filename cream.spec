%define name	cream
%define version	0.39
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	User-friendly face for Vim
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://cream.sourceforge.net/
License:	GPL
Group:		Editors

BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:  desktop-file-utils
Requires:	vim-X11
BuildArch:	noarch
Requires(post): desktop-file-utils 
Requires(postun): desktop-file-utils 

%description
Cream is a modeless GUIification of Vim.  Cream includes all the features of
Vim plus many custom utilities. A short list of features includes syntax
highlighting, spell check, multi-file find/replace, bookmarking, function
prototype popups, macros, auto-wrapping, reformatting, justification,
time/date stamps, file explorer, completion, sorting, calendar, tag
navigation, block commenting, Microsoft, Unix and Apple format text editing,
virtually unlimited file sizes, 38 varieties of 8-bit, 2-byte, and Unicode
support, single/multiple document modes, unlimited undo/redo, show invisible
characters, word count, and more.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_datadir/vim/cream/{addons,bitmaps,docs,docs-html,filetypes,help,spelldicts}
cp creamrc %buildroot/%_datadir/vim/cream/
cp *.vim %buildroot/%_datadir/vim/cream/
cp addons/*.vim %buildroot/%_datadir/vim/cream/addons/
cp bitmaps/*.bmp %buildroot/%_datadir/vim/cream/bitmaps/
cp bitmaps/*.xpm %buildroot/%_datadir/vim/cream/bitmaps/
cp docs/*.txt %buildroot/%_datadir/vim/cream/docs/
cp docs-html/*.html %buildroot/%_datadir/vim/cream/docs-html/
##cp docs-html/*.css %buildroot/%_datadir/vim/cream/docs-html/
cp docs-html/*.png %buildroot/%_datadir/vim/cream/docs-html/
cp filetypes/*.vim %buildroot/%_datadir/vim/cream/filetypes/
cp help/*.txt %buildroot/%_datadir/vim/cream/help/  
cp spelldicts/cream-spell-dict-eng-s*.vim %buildroot/%_datadir/vim/cream/spelldicts/
cp spelldicts/cream-spell-dict.vim %buildroot/%_datadir/vim/cream/spelldicts/

mkdir -p %buildroot/%_bindir
cp cream %buildroot/%_bindir/

mkdir -p %buildroot/%_datadir/applications
cp cream.desktop %buildroot/%_datadir/applications/

#mkdir -p %buildroot/
#cp cream.svg %buildroot/%_iconsdir/

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Cream" longtitle="Simplified graphical Vim" section="More Applications/Editors" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="TextEditor" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%{_bindir}/%name
%{_datadir}/vim/%name
%{_datadir}/applications/%name.desktop
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


