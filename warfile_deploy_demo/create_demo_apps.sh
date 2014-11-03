#!/bin/bash
#Purpose: Create N war files for rpm deployment demo
#Requires: tomcat/jdk to test the functionality.
#Date: 3/11/2014
#Author: Mohan

#Declare N instance of war file required.
INSTANCES=2

#Clean previous build war files/folders
rm -fv SOURCES/app*.war

#check if tomcat library exists
if [ ! -f /opt/tomcat/lib/servlet-api.jar ];
then
  echo "Requires tomcat library servlet-api.jar under /opt/tomcat/lib. Exiting.."
  exit 2;
fi

#Store the current dir for future use
TOP_DIR=$PWD

#Loop N no of times to create the needed war files
for (( i=1; i<=${INSTANCES}; i++ )); do

#Clean previously built war file with the same name
if [ -f SOURCES/app${i}.war ]; then
  rm -fv SOURCES/app${i}.war
fi

mkdir -pv SOURCES/app${i}/WEB-INF/classes

cat >> SOURCES/app${i}/WEB-INF/web.xml <<EOF
<web-app>
    <servlet>
              <servlet-name>app${i}</servlet-name>
              <servlet-class>app${i}</servlet-class>
     </servlet>
     <servlet-mapping>
             <servlet-name>app${i}</servlet-name>
             <url-pattern>/</url-pattern>
     </servlet-mapping>
</web-app>
EOF

cat >> SOURCES/app${i}/WEB-INF/classes/app${i}.java <<EOF
import java.io.IOException;
import java.io.PrintWriter;
 
import javax.servlet.ServletException;
import javax.servlet.*;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
 
public class app${i} extends HttpServlet {
 
  protected void service(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
      ServletContext sc=getServletContext();
      ServletConfig sg=getServletConfig();
      resp.setContentType("text/html");
      PrintWriter out = resp.getWriter();		
      out.println("<HTML>");
      out.println("<BODY>");
      out.println("Tomcat Details: <BR>");
      out.println("Server Name = " + req.getServerName() + "<BR>");
      out.println("Local Name = " + req.getLocalName() + "<BR>");
      out.println("IP = " + req.getLocalAddr() + "<BR>");
      out.println("Port = " + req.getServerPort() + "<BR>");
      out.println("Server Info = " + sc.getServerInfo() + "<BR>");
      out.println("Servlet Name = " + sg.getServletName() + "<BR>");
      out.println("ServletContext Path = " + req.getContextPath() + "<BR>");
      out.println("</HTML>");
      out.println("</BODY>");
  }
 
}

EOF

cd SOURCES/app${i}/WEB-INF/classes/

javac -cp /opt/tomcat/lib/servlet-api.jar app${i}.java

#package the war files, change dir to appN folder
cd $TOP_DIR/SOURCES/app${i}

jar -cvf app${i}.war *

mv app${i}.war ../

echo "Removing app${i} sources"
cd $TOP_DIR/SOURCES/
rm -rfv app${i}/

#Change dir to top folder for the loop to continue
cd $TOP_DIR

done

