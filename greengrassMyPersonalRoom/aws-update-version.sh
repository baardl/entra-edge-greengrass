#!/bin/sh
new_version=$1
echo new version: $new_version
aws lambda update-alias --function-name Greengrass_MyPersonalRoom --name GG_MyPersonalRoom --function-version $new_version 
