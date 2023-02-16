import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    try:
        install("Tkinter")
    except Exception as e:
        print("Module failed to install:\n%s" % e)