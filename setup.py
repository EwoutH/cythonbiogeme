import setuptools
import os
import platform

def get_ext_modules():
    from Cython.Build import cythonize
    ext_modules = [
        setuptools.Extension(
            "cythonbiogeme",
            sources=[
                "src/cythonbiogeme/cpp/cythonbiogeme.pyx",
                "src/cythonbiogeme/cpp/biogeme.cc",
                "src/cythonbiogeme/cpp/evaluateExpressions.cc",
                "src/cythonbiogeme/cpp/bioMemoryManagement.cc",
                "src/cythonbiogeme/cpp/bioNormalCdf.cc",
                "src/cythonbiogeme/cpp/bioFormula.cc",
                "src/cythonbiogeme/cpp/bioSeveralFormulas.cc",
                "src/cythonbiogeme/cpp/bioThreadMemory.cc",
                "src/cythonbiogeme/cpp/bioThreadMemoryOneExpression.cc",
                "src/cythonbiogeme/cpp/bioThreadMemorySimul.cc",
                "src/cythonbiogeme/cpp/bioString.cc",
                "src/cythonbiogeme/cpp/bioExprNormalCdf.cc",
                "src/cythonbiogeme/cpp/bioExprIntegrate.cc",
                "src/cythonbiogeme/cpp/bioExprGaussHermite.cc",
                "src/cythonbiogeme/cpp/bioExprRandomVariable.cc",
                "src/cythonbiogeme/cpp/bioExprMontecarlo.cc",
                "src/cythonbiogeme/cpp/bioExprPanelTrajectory.cc",
                "src/cythonbiogeme/cpp/bioExprDraws.cc",
                "src/cythonbiogeme/cpp/bioExprDerive.cc",
                "src/cythonbiogeme/cpp/bioExprMin.cc",
                "src/cythonbiogeme/cpp/bioExprMax.cc",
                "src/cythonbiogeme/cpp/bioExprAnd.cc",
                "src/cythonbiogeme/cpp/bioExprOr.cc",
                "src/cythonbiogeme/cpp/bioExprEqual.cc",
                "src/cythonbiogeme/cpp/bioExprNotEqual.cc",
                "src/cythonbiogeme/cpp/bioExprLessOrEqual.cc",
                "src/cythonbiogeme/cpp/bioExprLess.cc",
                "src/cythonbiogeme/cpp/bioExprGreaterOrEqual.cc",
                "src/cythonbiogeme/cpp/bioExprGreater.cc",
                "src/cythonbiogeme/cpp/bioExprElem.cc",
                "src/cythonbiogeme/cpp/bioExprMultSum.cc",
                "src/cythonbiogeme/cpp/bioExprLiteral.cc",
                "src/cythonbiogeme/cpp/bioExprFreeParameter.cc",
                "src/cythonbiogeme/cpp/bioExprFixedParameter.cc",
                "src/cythonbiogeme/cpp/bioExprVariable.cc",
                "src/cythonbiogeme/cpp/bioExprPlus.cc",
                "src/cythonbiogeme/cpp/bioExprMinus.cc",
                "src/cythonbiogeme/cpp/bioExprTimes.cc",
                "src/cythonbiogeme/cpp/bioExprDivide.cc",
                "src/cythonbiogeme/cpp/bioExprPower.cc",
                "src/cythonbiogeme/cpp/bioExprUnaryMinus.cc",
                "src/cythonbiogeme/cpp/bioExprExp.cc",
                "src/cythonbiogeme/cpp/bioExprLog.cc",
                "src/cythonbiogeme/cpp/bioExprLogzero.cc",
                "src/cythonbiogeme/cpp/bioExprNumeric.cc",
                "src/cythonbiogeme/cpp/bioExprLogLogit.cc",
                "src/cythonbiogeme/cpp/bioExprLogLogitFullChoiceSet.cc",
                "src/cythonbiogeme/cpp/bioExprLinearUtility.cc",
                "src/cythonbiogeme/cpp/bioExpression.cc",
                "src/cythonbiogeme/cpp/bioSeveralExpressions.cc",
                "src/cythonbiogeme/cpp/bioExceptions.cc",
                "src/cythonbiogeme/cpp/bioDerivatives.cc",
                "src/cythonbiogeme/cpp/bioVectorOfDerivatives.cc",
                "src/cythonbiogeme/cpp/bioGaussHermite.cc",
                "src/cythonbiogeme/cpp/bioGhFunction.cc",
            ],
            include_dirs=["src", get_numpy_include()],
            language="c++",
            extra_compile_args=["-std=c++11"],
            extra_link_args=["-std=c++11"]
        )
    ]
    if platform.system() == "Windows":
        ext_modules[0].extra_compile_args.append("-DMS_WIN64")
        ext_modules[0].extra_link_args.extend([
            "-static", "-static-libstdc++", "-static-libgcc", "-lpthread", "-mms-bitfields", "-mwindows"
        ])
    return cythonize(ext_modules)

def get_numpy_include():
    import numpy
    return numpy.get_include()

setuptools.setup(
    name="cythonbiogeme",
    version="0.1.0",  # Update with the appropriate version or use dynamic versioning
    description="C++ part of the Biogeme package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Michel Bierlaire",
    author_email="michel.bierlaire@epfl.ch",
    url="http://biogeme.epfl.ch",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "cython>=0.29.16",
        "pandas>=1.3.5"
    ],
    extras_require={
        "testing": [
            "cython>=0.29.32",
            "numpy>=1.23.4",
            "pytest>=7.2.0",
            "pytest-cov>=4.0.0",
            "tox>=3.27.1"
        ]
    },
    ext_modules=get_ext_modules(),
    include_package_data=True
)
