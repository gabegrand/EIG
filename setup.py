from distutils.core import setup
from Cython.Build import cythonize
from setuptools import Extension
import numpy
import os

cwd = os.getcwd()
compile_args = {
    "include_dirs": [numpy.get_include(), cwd + "/eig/battleship/executor", cwd + "/eig/battleship"],
    "extra_compile_args": ["-std=c++11", "-stdlib=libc++"],
    "extra_link_args": ["-std=c++11", "-stdlib=libc++"]
}

extensions = [
    Extension("eig.battleship.question.executor",
            ["eig/battleship/question/executor.pyx"],
            include_dirs=[numpy.get_include(), cwd + "/eig/battleship/cpp"],
            extra_compile_args=["-std=c++11", "-stdlib=libc++"],
            extra_link_args=["-std=c++11", "-stdlib=libc++"]
            ),
    Extension('eig.battleship.hypothesis_cy',
            ["eig/battleship/hypothesis_cy.pyx"],
            include_dirs=[numpy.get_include(), cwd + "/eig/battleship/cpp"],
            extra_compile_args=["-std=c++11", "-stdlib=libc++"],
            extra_link_args=["-std=c++11", "-stdlib=libc++"])
]

setup(
    test_suite="test",
    ext_modules=cythonize(extensions)
)
