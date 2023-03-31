# check disabled to prevent circular dependency (quickcheck)
%bcond_with check
%global debug_package %{nil}

%global crate regex

Name:           rust-%{crate}
Version:        1.4.5
Release:        2
Summary:        Implementation of regular expressions for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of regular expressions for Rust. This implementation uses finite
automata and guarantees linear time matching on all inputs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md HACKING.md PERFORMANCE.md UNICODE.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+aho-corasick-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+aho-corasick-devel %{_description}

This package contains library source intended for building other packages
which use "aho-corasick" feature of "%{crate}" crate.

%files       -n %{name}+aho-corasick-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages
which use "memchr" feature of "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pattern-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pattern-devel %{_description}

This package contains library source intended for building other packages
which use "pattern" feature of "%{crate}" crate.

%files       -n %{name}+pattern-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-devel %{_description}

This package contains library source intended for building other packages
which use "perf" feature of "%{crate}" crate.

%files       -n %{name}+perf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-cache-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-cache-devel %{_description}

This package contains library source intended for building other packages
which use "perf-cache" feature of "%{crate}" crate.

%files       -n %{name}+perf-cache-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-dfa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-dfa-devel %{_description}

This package contains library source intended for building other packages
which use "perf-dfa" feature of "%{crate}" crate.

%files       -n %{name}+perf-dfa-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-inline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-inline-devel %{_description}

This package contains library source intended for building other packages
which use "perf-inline" feature of "%{crate}" crate.

%files       -n %{name}+perf-inline-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-literal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-literal-devel %{_description}

This package contains library source intended for building other packages
which use "perf-literal" feature of "%{crate}" crate.

%files       -n %{name}+perf-literal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+thread_local-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+thread_local-devel %{_description}

This package contains library source intended for building other packages
which use "thread_local" feature of "%{crate}" crate.

%files       -n %{name}+thread_local-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages
which use "unicode" feature of "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-age-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-age-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-age" feature of "%{crate}" crate.

%files       -n %{name}+unicode-age-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-bool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-bool-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-bool" feature of "%{crate}" crate.

%files       -n %{name}+unicode-bool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-case-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-case-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-case" feature of "%{crate}" crate.

%files       -n %{name}+unicode-case-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-gencat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-gencat-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-gencat" feature of "%{crate}" crate.

%files       -n %{name}+unicode-gencat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-perl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-perl-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-perl" feature of "%{crate}" crate.

%files       -n %{name}+unicode-perl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-script-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-script-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-script" feature of "%{crate}" crate.

%files       -n %{name}+unicode-script-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-segment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segment-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-segment" feature of "%{crate}" crate.

%files       -n %{name}+unicode-segment-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
