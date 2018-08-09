Name:       ansible-role-dci-retrieve-component
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    ansible-role-dci-retrieve-component
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-retrieve-component
Source0:    ansible-role-dci-retrieve-component-%{version}.tar.gz

BuildArch:  noarch
Requires:   yum-utils
Requires:   dci-ansible

%description
An Ansible role that retrieve DCI component

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component

cp -r defaults %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component
cp -r files %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component
cp -r handlers %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-retrieve-component


%changelog
* Wed Jun 20 2018 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
