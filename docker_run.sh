image_name="djangoproject:1.0.0"

if [ -z $1 ]; then
  container_name="django-base"
else
  container_name=$1
fi

docker inspect ${container_name} > /dev/null
if [ $? -eq 0 ]; then
  docker rm -f ${container_name}
fi

docker run -dt -v work:/home/benp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name ${container_name} \
  -w /home/benp \
  --env DISPLAY="$DISPLAY" \
  -p 8000:8000 \
  --restart always "$image_name"

