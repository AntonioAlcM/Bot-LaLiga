from setuptools import setup

setup(name='bot_LaLiga',
      version='0.1',
      description='bot de telegram de la liga española de futbol',
      url='https://github.com/manuelalonsobraojos/proyectoIV',
      author='manuelalonsobraojos',
      author_email='manuelalonsobraojos93@correo.ugr.es',
      license='GNU',
      packages=['bot_LaLiga'],
      install_requires=[
          'PyMySQL',
          'pyTelegramBotAPI',
          'beautifulsoup4',
          'Paste',
          'requests'
      ],
      zip_safe=False)
