def options(opt):
    opt.add_option('--release', action='store_true', dest='release',
                   help='configure release build')
    opt.load('compiler_c')


def configure(conf):
    conf.load('compiler_c')
    print('is_release:', conf.options.release)
    configure_cc(conf, conf.options.release)


def add_cflags(env, flags):
    env.CFLAGS = env.CFLAGS[:]
    env.append_unique('CFLAGS', flags)


def configure_cc(conf, release=False):
    if release:
        add_cflags(conf.env, ['-O2', '-DNDEBUG'])
    else:
        add_cflags(conf.env, ['-O0', '-g'])


def build(bld):
    bld(export_includes='./include',
        name='apue_includes')

    # TODO(hayato): Update std/wscript and add 'std' to subdirs
    bld.recurse('lib sockets advio call calld daemons datafiles db environ exercises'
                ' file ipc ipp lock mycat open opend opend.fe open.fe proc pty'
                ' sess signals stdio streams termios threadctl threads'
                ' mytest'
                )
