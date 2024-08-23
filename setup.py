from setuptools import setup, find_packages

setup(
  name='streamlit_push_notifications',
  version='0.1',
  packages=find_packages(),
  description='A Streamlit library for sending browser notifications and alerts',
  author='Yunis Guliyev',
  author_email='yunisguliyev@gmail.com',
  url='https://github.com/yunisguliyev/streamlit-push-notifications.git', 
  classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
  ],
  install_requires=[
      'streamlit>=1.0.0', 
  ],
  python_requires='>=3.8',
)
