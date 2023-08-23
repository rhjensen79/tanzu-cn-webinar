# 1 - Modernize your applications

### Demo Steps

- Build

```bash
#docker build -t registry.tanzu.dk/webinars/app:1 .
docker buildx build -t registry.tanzu.dk/webinars/app:1 --platform linux/amd64,linux/arm64 .
```

- Run

```bash
docker run -p 5000:5000 registry.tanzu.dk/webinars/app:1
```

- Push

```bash
docker push registry.tanzu.dk/webinars/app:1
```

- Build 2

```bash
#docker build -t registry.tanzu.dk/webinars/app:2 .
docker buildx build -t registry.tanzu.dk/webinars/app:2 --platform linux/amd64,linux/arm64 .
```

- Push 2

```bash
docker push registry.tanzu.dk/webinars/app:2
```

- Run 2

```bash
docker run -p 5000:5000 registry.tanzu.dk/webinars/app:2
```
