Name:           odlcli
Version:        1.1.0
Release:        1%{?dist}
Summary:        OpenDaylight SDN Controller operational CLI interface

License:        EPL
URL:            https://www.cowdrey.net/
BuildRoot:      ~/rpmbuild/

BuildArch:      noarch
Requires:       bash
Requires:       bash-completion
Requires:       curl
Requires:       sed
Requires:       bc
Requires:       jq
Requires:       openssl
Requires:	libxml-xpath-perl

%description
OpenDaylight SDN Controller operational CLI interface

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 0555 ./%{name}%{_bindir}%{name} %{buildroot}%{_bindir}/
install -m 0555 './%{name}%{_sharedstatedir}/%{name}/?' %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/aaa %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/about %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/akka %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0444 ./%{name}%{_sharedstatedir}/%{name}/banner.%{name} %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/common %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0444 ./%{name}%{_sharedstatedir}/%{name}/config.template %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/delete %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/help %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/nodes %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/query %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/schema %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/set %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/show %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/sites %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/streams %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0555 ./%{name}%{_sharedstatedir}/%{name}/stats %{buildroot}%{_sharedstatedir}/%{name}/
install -m 0444 ./%{name}%{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/
install -m 0444 ./%{name}%{_sysconfdir}/bash_completion.d/%{name}.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/

%clean

%files
%defattr (-, root, bin)
%dir %{_sharedstatedir}/%{name}
%{_bindir}/%{name}
'%{_sharedstatedir}/%{name}/?'
%{_sharedstatedir}/%{name}/aaa
%{_sharedstatedir}/%{name}/about
%{_sharedstatedir}/%{name}/akka
%{_sharedstatedir}/%{name}/banner.%{name}
%{_sharedstatedir}/%{name}/common
%{_sharedstatedir}/%{name}/config.template
%{_sharedstatedir}/%{name}/delete
%{_sharedstatedir}/%{name}/help
%{_sharedstatedir}/%{name}/nodes
%{_sharedstatedir}/%{name}/query
%{_sharedstatedir}/%{name}/schema
%{_sharedstatedir}/%{name}/set
%{_sharedstatedir}/%{name}/show
%{_sharedstatedir}/%{name}/sites
%{_sharedstatedir}/%{name}/stats
%{_sharedstatedir}/%{name}/streams
%{_mandir}/man1/%{name}.1.gz
%{_sysconfdir}/bash_completion.d/%{name}.bash_completion

%changelog
*  Fri Sep 25 2020 Lee Cowdrey <lee@cowdrey.net> 1.0.0
- initial RHEL packaging release
*  Tue Jun 14 2022 Lee Cowdrey <lee@cowdrey.net> 1.1.0
- additional functionality including AKKA cluster queries
