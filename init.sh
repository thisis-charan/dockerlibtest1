#!/bin/bash
#script to be run locally on *nix based platform

targetdir="$1"


if [[ -z "$targetdir" ]]; then
   echo "Invalid Input. Please enter the full Image directory that you want to create : "
    read targetdir
    if [[ -z "$targetdir" ]]; then
        echo "No Input provided. Exiting ......"
         exit 1
    fi
fi


[ -d "$targetdir" ] && echo "Directory $targetdir exists. Exiting ....." && exit 1


mkdir -p "$targetdir"
cp .template/platformTemplate.json "$targetdir"/platform.json
cp .template/versionTemplate.toml "$targetdir"/version.toml
cp .template/DockerfileTemplate "$targetdir"/Dockerfile
cp .template/READMETemplate.md "$targetdir"/README.md

echo "Your directory $targetdir is ready to use. Please modify the file within $targetdir as per your requirement"