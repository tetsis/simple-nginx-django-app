# simple-nginx-django-app
Simple django application

# How to docker build and push
## current directory
```
$ ls
docker  README.md  src
```

## proxy
```
$ docker build -t tetsis/simple-nginx-django-proxy -f docker/proxy/Dockerfile .
$ docker push tetsis/simple-nginx-django-proxy:latest
```

## app
```
$ docker build -t tetsis/simple-nginx-django-app -f docker/app/Dockerfile .
$ docker push tetsis/simple-nginx-django-app:latest
```