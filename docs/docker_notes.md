docker image name = test
docker image tag = pandas

build the docker file using the name and tag test:pandas

if you use the same tag when building a new docker image with the same name, the new name:tag will go to the new docker image

and leave the previous one untagged, untagged docker image is known as dangling images

use "docker image prune" to remove dangling (untagged) images

tags in docker image is used for organisation purposes

properly organised docker images and removing untagged images helps save cost and space

*this does not affect other teammates because the docker image we are currently doing is local to each Docker installation*


### Scenario 2: 
    - shared image registry 
    - you and your team uses a registery Docker Hub or private registry
    - images are shared by pushing and pulling, not by building 
    - Computer A: build docker image mycompany/test:pandas 
    - Computer B: docker pull mycompany/test:pandas
    - Computer B: runs the docker image, this is the exact docker image that Computer A created 
    - dangling images still exists if either Computer A or B creates a new docker image with the same tag and name

### by using uv (VM) with docker 
    - solve OS environment issues
    - solves python version, and system libraries issues 
    - have same runtime everywhere 
    - while uv solves fast dependency installation, dependency resolution and lockfile-based reproducibility
    - uv build speed, conssitency of dependency versions and caching efficiency 


### Why use the Docker container as the PostgreSQL server
#### Use cases of UV
    - uv is designed to be a fast Python package and project manager
    - Download packages much faster (parallel downloads and an efficient implementation)
    - Resolve dependencies faster 
    - Create virtual environments quickly
    - Reuse a global package caache so the same package isn't downloaded repeatedly

#### Advantage of using uv with Docker 
    - Faster image builds because dependency installation is quicker
    - Reproducible builds because uv.lock pins exact versions
    - The same dependency management workflow locally and in Docker
