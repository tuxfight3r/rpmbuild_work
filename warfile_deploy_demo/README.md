#WARFILE RPM DEPLOY DEMO

Generate 2 dummy war files with create_demo_apps.sh and build an rpm for
the generated war files and deploy it under /opt/tomcat/webapps as user tomcat

The above war files will print out the following details about the sytem its
running

```shell
#Test the deployment if you created under webapps
curl http://192.168.0.1:8080/app1/

<HTML>
<BODY>
Tomcat Details:
Server Name = 192.168.0.1
Local Name = server01.test.local
IP = 192.168.0.1
Port = 8080
Server Info = Apache Tomcat/7.0.52
ServletContext Path = /app1
Servlet Name = HelloServlet
</HTML>
</BODY>

```
