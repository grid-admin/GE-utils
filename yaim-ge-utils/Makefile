prefix=/opt/glite
package=glite-yaim-sge-utils
name=$Name: glite-yaim-sge-utils_EMI2_branch $
tag:=$(shell echo $(name) | sed 's/^[^:]*: //' )
version:=$(shell echo "$(tag)" | sed 's/^.*R_//' | sed 's/_/\./g')
release:=$(shell echo "$(version)" | sed 's/.*\.//')
version:=$(shell echo "$(version)" | sed 's/\(.*\)\.[0-9]*/\1/')

.PHONY: configure install clean rpm

all: configure

install: 
	@echo installing ...
	@mkdir -p $(prefix)/yaim/functions/
	@mkdir -p $(prefix)/yaim/defaults/
	@mkdir -p $(prefix)/yaim/node-info.d/
	@mkdir -p $(prefix)/yaim/examples/
	@mkdir -p $(prefix)/yaim/examples/siteinfo/
	@mkdir -p $(prefix)/yaim/examples/siteinfo/services/
	@mkdir -p $(prefix)/share/man/man1
	@mkdir -p $(prefix)/yaim/etc/versions

	@install -m 0644 config/functions/config* $(prefix)/yaim/functions/
	@install -m 0644 config/defaults/glite* $(prefix)/yaim/defaults/
	@install -m 0644 config/node-info.d/glite* $(prefix)/yaim/node-info.d/
	@install -m 0644 config/services/glite* $(prefix)/yaim/examples/siteinfo/services/
	@install -m 0644 config/man/yaim-sge-utils.1 $(prefix)/share/man/man1/

	@echo "$(package) $(version)-$(release)" > $(prefix)/yaim/etc/versions/$(package)
clean:
	rm -f *~ test/*~ etc/*~ doc/*~ src/*~  
	rm -rf rpmbuild 
	rm -rf RPMS
rpm:
	@mkdir -p  RPMS
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/
ifneq ("$(tag)","ame:")
	@sed -i 's/^Version:.*/Version: $(version)/' $(package).spec
	@sed -i 's/^Release:.*/Release: $(release)/' $(package).spec
endif
	@tar --gzip --exclude='*CVS*' -cf rpmbuild/SOURCES/${package}.src.tgz *
	rpmbuild -ba ${package}.spec
	cp rpmbuild/RPMS/noarch/*.rpm rpmbuild/SRPMS/*.rpm RPMS/.




