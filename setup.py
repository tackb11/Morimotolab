from setuptools import setup, find_packages

setup(
    name             = 'MorimotoLab',
    version          = '1.0',
    description      = 'Data-preprocessing',
    long_description = open('README.md').read(),
    author           = 'CHAE TACBYOUNG',
    author_email     = 'tackb11@gmail.com',
    url              = 'https://github.com/tackb11/Morimotolab.git',
    download_url     = 'https://github.com/tackb11/Morimotolab.git',
    install_requires = ['numpy',
                        'pandas'],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['bot', 'study', 'api'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
