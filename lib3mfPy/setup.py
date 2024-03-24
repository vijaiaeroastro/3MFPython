from setuptools import setup, find_packages
import os

# Function to find the real path of the shared library
def find_real_lib_path():
    lib_folder = os.path.join('Lib3MF')  # Adjust the path to where your libraries are
    for item in os.listdir(lib_folder):
        if item.startswith('lib3mf') and item.endswith('.so'):
            full_path = os.path.join(lib_folder, item)
            if os.path.islink(full_path):
                # Resolve the real path
                return os.path.realpath(full_path)
            return full_path  # Return the direct file if it's not a symlink
    return None

# Use the resolved real path in package_data
real_lib_path = find_real_lib_path()
if real_lib_path:
    print("Choosing ", real_lib_path)
    lib_name = os.path.basename(real_lib_path)
else:
    raise FileNotFoundError("The lib3mf shared library could not be found.")

setup(
    name='Lib3MF',
    version='2.3.0',
    packages=find_packages(),
    package_data={
        'Lib3MF': ["lib3mf.so", "lib3mf.dylib, lib3mf.dll"],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2.3.0-prelease',  # Update the status as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Update the license as appropriate
        'Programming Language :: Python :: 3',  # Specify the Python version compatibility
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

# setup(
#     name='Lib3MF',
#     version='2.3.0',  # Adjust version as needed
#     packages=find_packages(),
#     ext_modules=[
#         Extension(
#             'Lib3MF.lib3mf',  # This should match the name of your .so file without the extension
#             sources=[],  # No sources needed, as we are using a pre-built .so file
#         )
#     ],
#     package_data={
#         'Lib3MF': ['*.so'],  # Include the .so file in the package
#     },
#     include_package_data=True,
#     zip_safe=False,
#     classifiers=[
#         'Development Status :: 2.3.0-prelease',  # Update the status as appropriate
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: MIT License',  # Update the license as appropriate
#         'Programming Language :: Python :: 3',  # Specify the Python version compatibility
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#     ],
# )
