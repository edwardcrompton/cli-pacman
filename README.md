## Running the application

Build the image using the Dockerfile in this directory:

`docker build . -t python-app`

Run the pacman.py script in the container:

```
docker run -it --rm -v `pwd`:/usr/src/app python-app python pacman.py`
```

