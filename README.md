ContainerVM
===========

ContainerVM is a lightweight [Debian](https://debian.org) image designed to simplify running [Docker](https://docker.io) containers in the Cloud.

It is composed of:
- A YAML/JSON manifest format to configure a group of containers
- A python agent that start containers according this manifest
- A bootstrap-vz plugin to build Cloud Provider images including the agent

## Usage

### Google Compute Engine

```
gcutil addinstance containervm-test \
    --image=projects/google-containers/global/images/containervm-v20140517 \
    --metadata_from_file=google-container-manifest:containers.yaml
```

## Manifest examples

### Redis
```
version: v1beta1
containers:
  - name: my-redis
    image: dockerfile/redis
    ports:
      - name: redis
        hostPort: 6379
        containerPort: 6379
```


### Simple netcat server
```
version: v1beta1
containers:
  - name: simple-echo
    image: google/busybox
    command: ['nc', '-l', '-p', '8080', '-c', 'echo hello world!']
    ports:
      - name: nc-echo
        hostPort: 8080
        containerPort: 8080
```

### Multiple containers (w/ private images)

```
version: v1beta1
containers:
  - name: docker-registry
    image: google/docker-registry
    ports:
      - name: registry
        hostPort: 5000
        containerPort: 5000
    env:
      - name: GCS_BUCKET
        value: my-gcs-bucket
  - name: my-private-app
    image: localhost:5000/my/private-app
    ports:
      - name: http
        hostPort: 80
        containerPort: 8080
```

## Community

- Give early feedback and talk with the community (including the developer team) on the [mailing-list](https://groups.google.com/d/google-containers)
- Ask development and best practices quesiton on [Stack Overflow](https://stackoverflow/container-vm)
- Chat with the community on [IRC](irc://irc.freenode.net/#container-vm)
- [Submit](/issues) Issues & Feature requests to the GitHub issue tracker
- [Fork](/fork) the repository and start [contributing](CONTRIBUTING.md)
