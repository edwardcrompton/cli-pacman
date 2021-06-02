## Running the application

Build the image using the Dockerfile in the directory above this:

`docker build . -t python-app`

Change to this directory and run the pacman script in the container:

`docker run -it --rm -v `pwd`:/usr/src/app python-app python pacman.py`

