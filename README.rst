vw-auth
===============================

auth service for vw

### Run Locally using docker

docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up

The auth service should be available at:

```
your-docker-machine-ip:5000
```

The mock mail client to receive confirmation email generated by user registration will be available at:

```
your-docker-machine-ip:1080
```
