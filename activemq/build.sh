#!/bin/sh
#Author: Mohan
#Date:31/10/2014
#Purpose: Build script to build activemq-5.9 rpm

#Variables
VERSION="5.9.0"
FILENAME="apache-activemq-5.9.0-bin.tar.gz"
DOWNLOAD_URL="http://archive.apache.org/dist/activemq/apache-activemq/${VERSION}/${FILENAME}"

#Clean up old build dirs
rm -rf BUILD RPMS SRPMS TEMP BUILDROOT
mkdir -p BUILD RPMS SRPMS TEMP BUILDROOT

#Download only if the source doesnt exist
if [ ! -f SOURCES/${FILENAME} ]; then

  curl -L $DOWNLOAD_URL -o SOURCES/${FILENAME}

fi

#start rpm build with spec file
rpmbuild -bb --define="_topdir $PWD" --define="_tmppath $PWD/TEMP" SPECS/activemq-5.9.spec

#Clean up unwanted build dirs, rpms should be available in the rpm directory
rm -rf BUILD SRPMS TEMP BUILDROOT

