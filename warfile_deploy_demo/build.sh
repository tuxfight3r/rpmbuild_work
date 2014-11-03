#!/bin/sh
#Author: Mohan
#Date:3/11/2014
#Purpose: Build script for warfile deployment rpm

#Clean up old build dirs
rm -rf BUILD RPMS SRPMS TEMP BUILDROOT
mkdir -p BUILD RPMS SRPMS TEMP BUILDROOT


#start rpm build with spec file
rpmbuild -bb --define="_topdir $PWD" --define="_tmppath $PWD/TEMP" SPECS/warfile_demo.spec

#Clean up unwanted build dirs, rpms should be available in the rpm directory
rm -rf BUILD SRPMS TEMP BUILDROOT

