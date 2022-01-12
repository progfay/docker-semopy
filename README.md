# docker-semopy

run visualization with semopy in Docker

## Build

```sh
$ docker build -t docker-semopy .
```

## Run

```sh
$ docker run -v $(pwd)/out:/usr/src/app/out --rm docker-semopy
```
