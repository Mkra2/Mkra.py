

foo = False
if foo:
    pass
import os
import sys
PSH_TEAM_KEY = '''بخ 👀'''
EXECUTE_FILE = '''.PY_PRIVATE/20230930024824612'''
PREFIX = sys.prefix
EXPORT_PYTHONHOME = '''export PYTHONHOME=''' + PREFIX
EXPORT_PYTHON_EXECUTABLE = '''export PYTHON_EXECUTABLE=''' + sys.executable
RUN = '''./''' + EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME + ''' && ''' + EXPORT_PYTHON_EXECUTABLE + ''' && ''' + RUN)
    exit(0)
C_FILE = '''.py_private.c'''
PYTHON_VERSION = '''.'''.join(sys.version.split(''' ''')[0].split('''.''')[:-1])
COMPILE_FILE = '''gcc -I''' + PREFIX + '''/include/python''' + PYTHON_VERSION + ''' -o ''' + EXECUTE_FILE + ''' ''' + C_FILE + ''' -L''' + PREFIX + '''/lib -lpython''' + PYTHON_VERSION
with open(C_FILE, '''w''') as f:
    f.write(C_SOURCE)
    None(None, None, None)
if not None:
    pass
os.makedirs(os.path.dirname(EXECUTE_FILE), True, **('exist_ok',))
os.system(EXPORT_PYTHONHOME + ''' && ''' + EXPORT_PYTHON_EXECUTABLE + ''' && ''' + COMPILE_FILE + ''' && ''' + RUN)
os.remove(C_FILE)