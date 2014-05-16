container-agent
===============

container-agent is a small python agent designed to start a group of [Docker](https://docker.io) containers according to a YAML [manifest](#manifest).

## Usage

### Locally

```
virtualenv env
env/bin/pip install git+http://github.com/proppy/container-vm-agent.git
env/bin/container-agent <path/to/manifest.yaml>
```

### Google Cloud Platform

Container-optimized images including `container-agent` are available for Google Compute Engine.

You can list available versions using:
```
gcutil --project=google-containers listimages
```

You can launch a new instance running `container-agent`. It will try to read the [manifest](#manifest) from `google-container-manifest` metadata on startup:
```
gcutil addinstance containervm-test \
    --image=projects/google-containers/global/images/container-vm-v20140522 \
    --metadata_from_file=google-container-manifest:containers.yaml
```

[Read more about Containers on the Google Cloud Platform](https://developers.google.com/compute/docs/containers)

## Manifest

[Documentation](https://developers.google.com/compute/docs/containers#manifest_format)

### Examples

A simple netcat server.
```
version: v1beta1
containers:
  - name: simple-echo
    image: google/busybox
    command: ['nc', '-p', '8080', '-l', '-l', '-e', 'echo', 'hello world!']
    ports:
      - name: nc-echo
        hostPort: 8080
        containerPort: 8080
```

A container group including:
- [`google/docker-registry`](https://index.docker.io/u/google/docker-registry) to pull (and push) private image from a [Google Cloud Storage](https://developers.google.com/storage/) bucket.
- Another container pulled from the registry container running localhost.
```
version: v1beta1
containers:
- name: registry
  image: google/docker-registry
  env:
    - key: GCS_BUCKET
      value: my-private-repository-bucket
  ports:
    - name: port5000
      hostPort: 5000
      containerPort: 5000
- name: my-private-app
  image: localhost:5000/my/app
  ports:
    - name: port80
      hostPort: 80
      containerPort: 8080
```

## Community

- Give early feedback and talk with the community (including the developer team) on the [mailing-list](https://groups.google.com/d/google-containers)
- Ask development and best practices questions on [Stack Overflow](http://stackoverflow.com/questions/tagged/google-compute-engine+docker)
- Chat with the community on [IRC](irc://irc.freenode.net/#google-containers)
- [Submit](https://github.com/GoogleCloudPlatform/container-agent/issues) Issues & Feature requests to the GitHub issue tracker
- [Fork](https://github.com/GoogleCloudPlatform/container-agent/fork) the repository and start [contributing](CONTRIB.md)

## License

[Apache License, Version 2.0](tree/master/COPYING.md)
