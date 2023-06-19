# Run Application on Linux

## Errors

```bash
Installing initially failed dependencies...
[pipenv.exceptions.InstallError]: Collecting asgiref==3.6.0 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 1))
[pipenv.exceptions.InstallError]:   Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
[pipenv.exceptions.InstallError]: Collecting coverage==7.2.5 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 2))
[pipenv.exceptions.InstallError]:   Using cached coverage-7.2.5-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (232 kB)
[pipenv.exceptions.InstallError]: Collecting django==4.1.9 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 3))
[pipenv.exceptions.InstallError]:   Using cached Django-4.1.9-py3-none-any.whl (8.1 MB)
[pipenv.exceptions.InstallError]: Collecting docutils==0.19 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 4))
[pipenv.exceptions.InstallError]:   Using cached docutils-0.19-py3-none-any.whl (570 kB)
[pipenv.exceptions.InstallError]: Collecting gunicorn==20.1.0 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 5))
[pipenv.exceptions.InstallError]:   Using cached gunicorn-20.1.0-py3-none-any.whl (79 kB)
[pipenv.exceptions.InstallError]: Collecting pillow==9.5.0 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 6))
[pipenv.exceptions.InstallError]:   Using cached Pillow-9.5.0-cp311-cp311-manylinux_2_28_x86_64.whl (3.4 MB)
[pipenv.exceptions.InstallError]: Collecting psycopg2==2.9.5 (from -r /tmp/pipenv-wyv9vku2-requirements/pipenv-3jxypdsi-hashed-reqs.txt (line 7))
[pipenv.exceptions.InstallError]:   Using cached psycopg2-2.9.5.tar.gz (384 kB)
[pipenv.exceptions.InstallError]:   Preparing metadata (setup.py): started
[pipenv.exceptions.InstallError]:   Preparing metadata (setup.py): finished with status 'error'
[pipenv.exceptions.InstallError]: error: subprocess-exited-with-error
[pipenv.exceptions.InstallError]:   
[pipenv.exceptions.InstallError]:   × python setup.py egg_info did not run successfully.
[pipenv.exceptions.InstallError]:   │ exit code: 1
[pipenv.exceptions.InstallError]:   ╰─> [37 lines of output]
[pipenv.exceptions.InstallError]:       /home/flynnt/.local/share/virtualenvs/blog-and-portfolio-cobJGnth/lib/python3.11/site-packages/setuptools/config/setupcfg.py:293: _DeprecatedConfig: Deprecated config in `setup.cfg`
[pipenv.exceptions.InstallError]:       !!
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:               ********************************************************************************
[pipenv.exceptions.InstallError]:               The license_file parameter is deprecated, use license_files instead.
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:               By 2023-Oct-30, you need to update your project and remove deprecated calls
[pipenv.exceptions.InstallError]:               or your builds will no longer be supported.
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:               See https://setuptools.pypa.io/en/latest/userguide/declarative_config.html for details.
[pipenv.exceptions.InstallError]:               ********************************************************************************
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       !!
[pipenv.exceptions.InstallError]:         parsed = self.parsers.get(option_name, lambda x: x)(value)
[pipenv.exceptions.InstallError]:       running egg_info
[pipenv.exceptions.InstallError]:       creating /tmp/pip-pip-egg-info-z27xu84l/psycopg2.egg-info
[pipenv.exceptions.InstallError]:       writing /tmp/pip-pip-egg-info-z27xu84l/psycopg2.egg-info/PKG-INFO
[pipenv.exceptions.InstallError]:       writing dependency_links to /tmp/pip-pip-egg-info-z27xu84l/psycopg2.egg-info/dependency_links.txt
[pipenv.exceptions.InstallError]:       writing top-level names to /tmp/pip-pip-egg-info-z27xu84l/psycopg2.egg-info/top_level.txt
[pipenv.exceptions.InstallError]:       writing manifest file '/tmp/pip-pip-egg-info-z27xu84l/psycopg2.egg-info/SOURCES.txt'
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       Error: pg_config executable not found.
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       pg_config is required to build psycopg2 from source.  Please add the directory
[pipenv.exceptions.InstallError]:       containing pg_config to the $PATH or specify the full executable path with the
[pipenv.exceptions.InstallError]:       option:
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:           python setup.py build_ext --pg-config /path/to/pg_config build ...
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       or with the pg_config option in 'setup.cfg'.
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       If you prefer to avoid building psycopg2 from source, please install the PyPI
[pipenv.exceptions.InstallError]:       'psycopg2-binary' package instead.
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       For further information please check the 'doc/src/install.rst' file (also at
[pipenv.exceptions.InstallError]:       <https://www.psycopg.org/docs/install.html>).
[pipenv.exceptions.InstallError]:       
[pipenv.exceptions.InstallError]:       [end of output]
[pipenv.exceptions.InstallError]:   
[pipenv.exceptions.InstallError]:   note: This error originates from a subprocess, and is likely not a problem with pip.
[pipenv.exceptions.InstallError]: error: metadata-generation-failed
[pipenv.exceptions.InstallError]: 
[pipenv.exceptions.InstallError]: × Encountered error while generating package metadata.
[pipenv.exceptions.InstallError]: ╰─> See above for output.
[pipenv.exceptions.InstallError]: 
[pipenv.exceptions.InstallError]: note: This is an issue with the package mentioned above, not pip.
[pipenv.exceptions.InstallError]: hint: See above for details.
```
