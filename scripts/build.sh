#!/bin/bash

BRed='\033[1;31m'
BGreen='\033[1;32m'
NC='\033[0m' # No Color

echo -e "${BGreen}Enter version tag${BRed}"
read version

docker build -t bhartford419/flask_login:${version} .
docker run -d -p 3007:3007 bhartford419/flask_login:${version}

echo -e "${BGreen}Push docker image? [y/n]"
read push_repo


if [[ $push_repo == "y" ]]
then
  # push Docker repo
  docker push bhartford419/flask_login:${version}
else
  echo -e "${BRed}Skipping Docker repo push."
fi

