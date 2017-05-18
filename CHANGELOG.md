# Changelog

## Unreleased


## 1.3.0 (2017-05-18)


### New

- Test. [rachmadaniHaryono]


- Add Gitter badge (#110) [The Gitter Badger]

### Changes

- Travis settings. [rachmadaniHaryono]

- Remove unused init file. [rachmadaniHaryono]

- Check if video choice is valid. [Mihai Olteanu]

  Check if the video choice is a valid digit or if it's in the range of available choices.
  Notify the user otherwise.

- Added a Bitdeli badge to README. [Bitdeli Chef]

- Added .gitattributes to vendor installer files. [Avi Aryan]

- Added Windows related (install instructions, script). [Avi Aryan, Yask Srivastava]

- Added best quality parameter. [Yask Srivastava]

- Added command-line support for input list and file input. [Larissa Feng]

- Added flag for quiet mode. [Larissa Feng]

- Added install.bat. [aviaryan]

- Added missing requests. [Avi Aryan]

- Added option for calling from command-line. [Larissa Feng]

- Added pyreadline in requirements. [Avi Aryan]

- Added pyreadline to `install_requires` fixing #80. [Yask Srivastava]

- Added some comments. [aviaryan]

- Added valid prompts. [Vinayak Mehta]

- Added youtube-dl arg. [Vinayak Mehta]

- Added a better installer script and changing the music downloader script. [Nishant Arora]

- Changed default format to MP3. [Yask Srivastava]

- Create .travis.yml. [Yask Srivastava]

- Create `music_downloader.py`, requirements.txt, `super_installer.py`. [Yask Srivastava]

- Made Y the default input. [Yask Srivastava]

- Made mp3 default. [Yask Srivastava]

- Made `raw_input=input` in case of Py3 as suggested by @yask123.  [aviaryan]

- Made script Python 2 + 3 compatible. [Yask Srivastava]

- Made script executable. [Aaron Ouellette]

- Remove Python 2 from requirements. [aviaryan]

- Remove extra title. [aouelete]

- Remove trailing whitespace. [Robin Schroer]

- Remove unnecessary whitespace. [Kyrylo Romanenko]

- Remove unused urlopen. [Liam Bowen]

- Remove debug print. [Larissa Feng]

- Refactor. [Liam Bowen, Omar Abou Mrad]

- Update files [Bhavya Goyal, Nishant Arora, Yann Vaillant, Yask Srivastava]

  - README.md
  - gitignore
  - `music_downloader.py`
  - requirements.txt
  - setup.py.
  - `super_installer.py`
  - install method
  - install.sh

### Fix

- Remove tags from lyrics (#109) (prevent tags from being printed) [Ritiek Malhotra]

- Index out of bound if - is not present in the name of the song.  [atuljangra]

- Fix ID3 tagging error. [Jay Bosamiya]

  When any of the artist, `track_name`, or `album_name` do not have a '[' in them,
  and if they don't end with a whitespace, then last character used to get removed.

- Fix issue when printing unicode results (closes #30). [Yask Srivastava, Asad Dhamani]

- Fix line editing when prompting.[Yask Srivastava]

- Fix the youtube-dl quiet parameter (`--q` to `-q`) [Robin Schroer]

- Fix major path bug. [Yask Srivastava]

- Fix merge conflicts; fixed flag argument handling. [Larissa Feng]

- Fix some command line parsing edge cases. [Larissa Feng]

### Other

- use the more recent updates in the package. [Robin Schroer]

- Command-line parameters and small fixes. [Yask Srivastava]

- Define unicode for Python 3 and improve variable names. [Yask Srivastava]

- Dont add to PATH if already exists. [aviaryan]

- General url encoding. [so4pmaker]

- Getting lyrics in case https url is not there. Using http instead.  [atuljangra]

- Git ignore `*.webm`. [aviaryan]

- Give warning if path length going to exceed 1024. [aviaryan]

- Ignore downloaded songs. [Aaron Ouellette]

- Import readline. [Yann Vaillant, Yask Srivastava]

- Indicate failure in quiet mode using the exit code. [Robin Schroer]

- Missing commit. [Nishant Arora]

- Modifying requests to work with proxy. [atuljangra]

- Package created. [Yask Srivastava]

- Print song and video title and prompt for download . [Yask Srivastava, Aaron Ouellette]

- Python 3's str can be used as Python 2's unicode. [Liam Bowen]

- Smart github. [Avi Aryan]

- Some cleanup, formatting and mention python2. [Aaron Ouellette]

- Update to use BeautifulSoup, Bug fixes. [Yask Srivastava]

- Initial commit. [Yask Srivastava]
