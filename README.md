# CycleGANs Demo
A demo on style transfer using CycleGAN Image-to-Image translation.

## Execution Directions
This application is fully dockerized. To build and run:

1. `./build.sh`
2. `./run.sh`
3. Navigate to `127.0.0.1:8888`

## Configuration
### Port
Adjust the `PORT` variable in `run.sh` to choose which port to run it on.

### Daemon
By default, the application will be run as a daemon. This is how it should be
running in an server environment. For debugging, however, simply uncomment
the `interactive` and recomment the `daemonized` line in `run.sh`. This will
run the container in an interactive server for easier debugging.