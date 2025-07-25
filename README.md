# vyos-container
VyOS container images for use in home or network labs.

To pull a VyOS container image, use the following command:

```bash
docker pull ghcr.io/evilhamsterman/vyos:<tag>
```
Or
```bash
podman pull ghcr.io/evilhamsterman/vyos:<tag>
```

> [!Caution]
> It is **NOT** recommended to use these images in production environments. All images are released under the same terms as the [VyOS project](https://github.com/vyos/vyos-1x)

> [!Note]
> I am not associated VyOS Networks or the VyOS project in any way. These images are built from the official VyOS releases per their [documentation](https://docs.vyos.io/en/latest/installation/virtual/docker.html) as a convenience for users who want to run VyOS in a containerized environment.

## Tags
Containers are automatically built for the Rolling release every day with the last 7 available for download.

I will also build the latest [Stream](https://vyos.net/get/stream/) when they are released.

* `latest` - Latest Rolling release
* `rolling` - Latest Rolling release
* `YYYY.MM.DD-xxxx-rolling` - Specific Rolling release. See [VyOS Nightly Builds](https://github.com/vyos/vyos-nightly-build/releases) for recent names and changelogs.
* `stream` - Latest Stream release
* `1.5-stream-YYYY-Qx` - Specific Stream release. See [VyOS Stream Releases](https://vyos.net/get/stream/)

## Building
### Requirements

* Docker
* [Taskfile](https://taskfile.dev/)
* bsdtar
* squashfs-tools-ng

### Build

1. Download the ISO file you wish to build from the [VyOS download page](https://vyos.net/get/) into the root of the repository.

2. Then run the following command in the root of this repository `task build`
