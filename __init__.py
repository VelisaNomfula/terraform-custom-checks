from checkov.terraform.checks.resource.github import *

from os.path import dirname, baseline, isfile, join
import glob
module = glob.glob(join(dirname(__file__), "*.py"))
__all__= [ baseline(f)[:-3] for f in modules if isfile(f) and not f.endswitch('__init__.py')]