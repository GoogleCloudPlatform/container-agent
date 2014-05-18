ContainerVM
===========

ContainerVM is a lightweight [Debian](https://debian.org) Virtual Machine image designed to simplify running [Docker](https://docker.io) containers in the Cloud.

It is composed of:
- A YAML/JSON [manifest](#manifest-examples) format to configure and run a group of containers
- A python [agent](tree/master/agent) that start containers according this manifest
- A [bootstrap-vz](http://bootstrapvz.readthedoc.org/) plugin to build Cloud Provider images with the agent and its dependencies

[Get started with ContainerVM](tree/master/docs/)

## Usage

### Google Cloud Platform

```
gcutil addinstance containervm-test \
    --image=projects/google-containers/global/images/containervm-v20140517 \
    --metadata_from_file=google-container-manifest:containers.yaml
```

[More advanced instructions](tree/master/docs/README.md#google)

## Manifest

### Example

A simple netcat server
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

[More examples](tree/master/docs/README.md#manifest)

## Community

- Give early feedback and talk with the community (including the developer team) on the [mailing-list](https://groups.google.com/d/google-containers)
- Ask development and best practices quesiton on [Stack Overflow](https://stackoverflow/container-vm)
- Chat with the community on [IRC](irc://irc.freenode.net/#container-vm)
- [Submit](/issues) Issues & Feature requests to the GitHub issue tracker
- [Fork](/fork) the repository and start [contributing](CONTRIBUTING.md)

## License

[Apache License, Version 2.0](tree/master/COPYING.md)
