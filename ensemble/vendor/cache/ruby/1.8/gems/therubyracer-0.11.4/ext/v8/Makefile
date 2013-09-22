
SHELL = /bin/sh

#### Start of system configuration section. ####

srcdir = .
topdir = /usr/lib/ruby/1.8/x86_64-linux
hdrdir = $(topdir)
VPATH = $(srcdir):$(topdir):$(hdrdir)
prefix = $(DESTDIR)/usr
exec_prefix = $(prefix)
htmldir = $(docdir)
vendorlibdir = $(vendordir)/$(ruby_version)
rubylibdir = $(libdir)/ruby/$(ruby_version)
oldincludedir = $(DESTDIR)/usr/include
infodir = $(prefix)/share/info
includedir = $(prefix)/include
bindir = $(exec_prefix)/bin
libexecdir = $(prefix)/lib/ruby1.8
datadir = $(datarootdir)
libdir = $(exec_prefix)/lib
localedir = $(datarootdir)/locale
archdir = $(rubylibdir)/$(arch)
docdir = $(datarootdir)/doc/$(PACKAGE)
sbindir = $(exec_prefix)/sbin
sitedir = $(DESTDIR)/usr/local/lib/site_ruby
sysconfdir = $(DESTDIR)/etc
localstatedir = $(DESTDIR)/var
sitelibdir = $(sitedir)/$(ruby_version)
vendordir = $(libdir)/ruby/vendor_ruby
vendorarchdir = $(vendorlibdir)/$(sitearch)
pdfdir = $(docdir)
psdir = $(docdir)
sharedstatedir = $(prefix)/com
sitearchdir = $(sitelibdir)/$(sitearch)
datarootdir = $(prefix)/share
mandir = $(prefix)/share/man
dvidir = $(docdir)

CC = gcc
LIBRUBY = $(LIBRUBY_SO)
LIBRUBY_A = lib$(RUBY_SO_NAME)-static.a
LIBRUBYARG_SHARED = -l$(RUBY_SO_NAME)
LIBRUBYARG_STATIC = -l$(RUBY_SO_NAME)-static

RUBY_EXTCONF_H = 
CFLAGS   =  -fPIC -fno-strict-aliasing -g -g -O2  -fPIC $(cflags) 
INCFLAGS = -I. -I/home/christopher/MHacks/MHacks/ensemble/vendor/cache/ruby/1.8/gems/libv8-3.11.8.17-x86_64-linux/vendor/v8/include -I. -I/usr/lib/ruby/1.8/x86_64-linux -I.
DEFS     = 
CPPFLAGS =  -D_FORTIFY_SOURCE=2  -D_FORTIFY_SOURCE=2 -Wall -g -rdynamic
CXXFLAGS = $(CFLAGS) 
ldflags  = /home/christopher/MHacks/MHacks/ensemble/vendor/cache/ruby/1.8/gems/libv8-3.11.8.17-x86_64-linux/vendor/v8/out/x64.release/obj.target/tools/gyp/libv8_base.a /home/christopher/MHacks/MHacks/ensemble/vendor/cache/ruby/1.8/gems/libv8-3.11.8.17-x86_64-linux/vendor/v8/out/x64.release/obj.target/tools/gyp/libv8_snapshot.a -L. -Wl,-Bsymbolic-functions -Wl,-z,relro -rdynamic -Wl,-export-dynamic
dldflags = 
archflag = 
DLDFLAGS = $(ldflags) $(dldflags) $(archflag)
LDSHARED = $(CXX) -shared
AR = ar
EXEEXT = 

RUBY_INSTALL_NAME = ruby1.8
RUBY_SO_NAME = ruby1.8
arch = x86_64-linux
sitearch = x86_64-linux
ruby_version = 1.8
ruby = /usr/bin/ruby1.8
RUBY = $(ruby)
RM = rm -f
MAKEDIRS = mkdir -p
INSTALL = /usr/bin/install -c
INSTALL_PROG = $(INSTALL) -m 0755
INSTALL_DATA = $(INSTALL) -m 644
COPY = cp

#### End of system configuration section. ####

preload = 

libpath = . $(libdir)
LIBPATH =  -L. -L$(libdir)
DEFFILE = 

CLEANFILES = mkmf.log
DISTCLEANFILES = 

extout = 
extout_prefix = 
target_prefix = /v8
LOCAL_LIBS = 
LIBS = $(LIBRUBYARG_SHARED) -lpthread  -lpthread -lrt -ldl -lcrypt -lm   -lc
SRCS = date.cc accessor.cc v8.cc script.cc locker.cc constants.cc stack.cc init.cc primitive.cc message.cc handles.cc function.cc signature.cc context.cc heap.cc gc.cc array.cc exception.cc trycatch.cc object.cc invocation.cc string.cc constraints.cc rr.cc external.cc value.cc backref.cc template.cc
OBJS = date.o accessor.o v8.o script.o locker.o constants.o stack.o init.o primitive.o message.o handles.o function.o signature.o context.o heap.o gc.o array.o exception.o trycatch.o object.o invocation.o string.o constraints.o rr.o external.o value.o backref.o template.o
TARGET = init
DLLIB = $(TARGET).so
EXTSTATIC = 
STATIC_LIB = 

BINDIR        = $(bindir)
RUBYCOMMONDIR = $(sitedir)$(target_prefix)
RUBYLIBDIR = /home/christopher/MHacks/MHacks/ensemble/vendor/cache/ruby/1.8/gems/therubyracer-0.11.4/lib$(target_prefix)
RUBYARCHDIR = /home/christopher/MHacks/MHacks/ensemble/vendor/cache/ruby/1.8/gems/therubyracer-0.11.4/lib$(target_prefix)

TARGET_SO     = $(DLLIB)
CLEANLIBS     = $(TARGET).so $(TARGET).il? $(TARGET).tds $(TARGET).map
CLEANOBJS     = *.o *.a *.s[ol] *.pdb *.exp *.bak

all:		$(DLLIB)
static:		$(STATIC_LIB)

clean:
		@-$(RM) $(CLEANLIBS) $(CLEANOBJS) $(CLEANFILES)

distclean:	clean
		@-$(RM) Makefile $(RUBY_EXTCONF_H) conftest.* mkmf.log
		@-$(RM) core ruby$(EXEEXT) *~ $(DISTCLEANFILES)

realclean:	distclean
install: install-so install-rb

install-so: $(RUBYARCHDIR)
install-so: $(RUBYARCHDIR)/$(DLLIB)
$(RUBYARCHDIR)/$(DLLIB): $(DLLIB)
	$(INSTALL_PROG) $(DLLIB) $(RUBYARCHDIR)
install-rb: pre-install-rb install-rb-default
install-rb-default: pre-install-rb-default
pre-install-rb: Makefile
pre-install-rb-default: Makefile
$(RUBYARCHDIR):
	$(MAKEDIRS) $@

site-install: site-install-so site-install-rb
site-install-so: install-so
site-install-rb: install-rb

.SUFFIXES: .c .m .cc .cxx .cpp .C .o

.cc.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.cxx.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.cpp.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.C.o:
	$(CXX) $(INCFLAGS) $(CPPFLAGS) $(CXXFLAGS) -c $<

.c.o:
	$(CC) $(INCFLAGS) $(CPPFLAGS) $(CFLAGS) -c $<

$(DLLIB): $(OBJS) Makefile
	@-$(RM) $@
	$(LDSHARED) -o $@ $(OBJS) $(LIBPATH) $(DLDFLAGS) $(LOCAL_LIBS) $(LIBS)



$(OBJS): ruby.h defines.h
