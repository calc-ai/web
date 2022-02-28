```shell
# build
docker build --cache-from ${YOUR_DOCKERHUB_ID}/${YOUR_PROJECT_NAME} -t ${YOUR_DOCKERHUB_ID}/${YOUR_PROJECT_NAME}
 --build-arg YOUR_ENV=production .

# run
docker run -p 8080:8080 -it ${YOUR_DOCKERHUB_ID}/${YOUR_PROJECT_NAME}
```
