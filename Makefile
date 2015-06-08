#
# Copyright (c) SAS Institute Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

SUBDIRS = rpath_models\
          xsd

export PRODUCT = rpath-models
export VERSION = 1.0.3
export SHORTVER = $(VERSION)
export TOPDIR =     $(shell pwd)
export DISTNAME =   $(PRODUCT)-$(SHORTVER)
export DISTDIR =    $(TOPDIR)/$(DISTNAME)
export PREFIX =     /usr
export lib =        $(shell uname -m | sed -r '/x86_64|ppc64|s390x|sparc64/{s/.*/lib64/;q};s/.*/lib/')
export LIBDIR =     $(PREFIX)/$(lib)
export PYVER =      "`python -c 'import sys; print sys.version[0:3]'`"
export PYTHON = /usr/bin/python$(PYVER)
export PYDIR = $(LIBDIR)/python$(PYVER)/site-packages
export DATADIR = $(PREFIX)/share

dist_files = Makefile
GENERATE_DS=generateDS.py
XSD_DIR=xsd
MODELS_DIR=rpath_models

.PHONY: clean install generate

all: $(generated_files) default-all

install: default-install

clean: default-clean

generate: $(patsubst $(XSD_DIR)/%.xsd,rule-%,$(wildcard $(XSD_DIR)/*.xsd))

rule-%:
	$(GENERATE_DS) -f --silence \
                --no-dates \
                --no-versions \
                --member-specs=list \
                --external-encoding=utf-8 \
                --search-path=$(XSD_DIR) \
                -o $(MODELS_DIR)/generateds_$(subst .,_,$(subst -,_,$(patsubst rule-%,%,$@))).py \
                $(XSD_DIR)/$(patsubst rule-%,%,$@).xsd

install-generate: $(addprefix install-rule-,$(wildcard xml_*))

install-rule-%: %
	install -d $(DESTDIR)$(pydir)$<
	install $</*.py $(DESTDIR)$(pydir)$</

tag:
	hg tag -f $(DISTNAME)

archive:
	if (hg stat | grep "^[ARM]" > /dev/null); then \
		echo "Repository has uncommitted changes"; exit 1; fi
	rm -rf $(DISTDIR)
	mkdir $(DISTDIR)
	hg archive -t tbz2 -r $(DISTNAME) $(DISTNAME).tar.bz2

include Make.rules
