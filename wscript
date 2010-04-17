from my.wafutil import *

includes = ['.', '../include']

@featured
def set_options(opt):
  opt.tool_options('compiler_cc')

@featured
def configure(conf):
  conf.check_tool('compiler_cc')
  conf.env.CPPPATH += includes
  conf.env.CCFLAGS += ['-DMACOS']

def shutdown():
  pass

@featured
def build(bld):
  # bld.use_the_magic() # so that generated xxx.c files can be found.

  dirs = ('lib sockets advio call calld daemons datafiles db environ exercises'
          ' file ipc ipp lock mycat open opend opend.fe open.fe proc pty'
          ' sess signals std stdio streams termios threadctl threads'
          ' mytest'
          )

  for d in dirs.split():
    bld.recurse(d)
