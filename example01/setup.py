from setuptools import setup, find_packages

print find_packages(where="src")
setup(name="distlib",
      version="1.0.1",
      license="Apache 2.0",
      package_dir={'': 'src'},
      packages=find_packages(where="src"),
      # py_modules=find_packages(where="src"),
      zip_safe=False
)