from tempfile import TemporaryDirectory
with TemporaryDirectory(prefix='oni_download', dir='.') as tempdir:
    print('Temp Directory: ', tempdir)