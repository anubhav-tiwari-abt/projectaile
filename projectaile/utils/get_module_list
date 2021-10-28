import sys
import types
import pkg_resources


def get_version(module):
    version = ''
    try:
        version = module.__version__
    except:
        try:
            if type(module.version) is str:
                version = module.version
            else:
                version = module.version()
        except:
            try:
                version = module.VERSION
            except:
                pass
    return version


def get_alias(global_modules, module):
    alias = ''
    original_name = module.__name__

    for modules in global_modules:
        if isinstance(global_modules[modules], types.ModuleType):
            if global_modules[modules].__name__ == original_name:
                print('Found : ', modules, original_name)
                alias = modules
                return alias

    return alias


def get_modules(only_imported=False):
    global_modules = globals()
    if only_imported:
        imported_modules = sys.modules
        imported = {}
        for module in imported_modules:
            version = get_version(imported_modules[module])
            alias = get_alias(global_modules, imported_modules[module])
            imported[module] = {'version': version, 'alias': alias}
        return imported

    installed = pkg_resources.working_set

    available_modules = {i.key: i.version for i in installed}

    return available_modules
