Name:       ansible-role-dci-retrieve-component
Version:    0.1.VERS
Release:    2%{?dist}
Summary:    ansible-role-dci-retrieve-component
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-retrieve-component
Source0:    ansible-role-dci-retrieve-component-%{version}.tar.gz

BuildArch:  noarch
Requires:   createrepo
Requires:   python-lxml
Requires:   yum-utils
Requires:   dci-ansible
Requires:   dci-downloader
BuildRequires:    /usr/bin/pathfix.py

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
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component

%if 0%{?rhel} && 0%{?rhel} < 8
pathfix.py -pni "%{__python2}" %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component/files/cleanup_repo.py
%else
pathfix.py -pni "%{__python3}" %{buildroot}%{_datadir}/dci/roles/dci-retrieve-component/files/cleanup_repo.py
%endif

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-retrieve-component


%changelog
* Thu Jun 04 2020 Bill Peck <bpeck@rehdat.com> - 0.1.1-2
- Rebuild for RHEL-8
* Tue Nov 26 2019 Francois Charlier <fcharlie@rehdat.com> - 0.1.1-1
- Introduce using dci-downloader for Compose type components
* Wed Jun 20 2018 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
