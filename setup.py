from setuptools import setup, find_packages

install_requires = [
    "django ~= 3.2.1",
    "django-crispy-forms ~=1.14.0",
    "jadecore3",
    "jadestream",
    "rdcore3",
    "rdcore3.install",
    "rdcore3.qronos",
]

tests_require = [
    "pytest",
]

setup(name='debugging_cake_portal',
      version='0.1.7',
      description="Luminess debugging forum.",
      author="Python Intern Team Luminess",
      install_requires=install_requires,
      package_dir={"debugging_cake_portal": "src"},
      packages=find_packages(),
      #packages=["debugging_cake_portal", "debugging_cake_portal.cake_user", "debugging_cake_portal.posts"],
      test_suite="tests",
      tests_require=tests_require,
      extras_require={
          "test": tests_require,
      },
)
