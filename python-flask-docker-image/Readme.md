A simple Web App build using Python, Flask, Angular.



## Docker commands

```bash
    
        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath

        
        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>


```
