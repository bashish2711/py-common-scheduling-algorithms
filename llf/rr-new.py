#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
print "Content-type:text/html\r\n\r\n"
print """

<form action="" method = "post" > 
<input type = "radio" name = "sch" value = "RR" /> Round Robin
<input type = "radio" name = "sch" value = "EDF" /> EDF 
<input type = "submit" value = "Choose" />
</form>
"""
print """
<form action="" method = "post" >
  <input type="submit" name = "new" value="Add">
</form>
    
"""
form = cgi.FieldStorage() 
#
if form.getvalue('new'): 
   sub = form.getvalue('new')
   print "<h1> %s </h1>" %sub
   if sub == "Add":
      print """
      <form action="/Ferret/Ashish/action_page.php" method = "post" >
      <input type="text" name="email" size="1"> 
      <input type="text" name="pin" maxlength="4" size="1">
      <input type="submit" value="Submit">
      </form>
      """ 

# Import modules for CGI handling 
# Get data from fields
if form.getvalue('sch'):
   subject = form.getvalue('sch')
   print "<h1> %s </h1>" %subject
   if subject == "RR":
       print """
    <form action="/cgi-bin/Ferret/Ashish/rr.py">
        <input type="submit" value="Open Script">
    </form>
        """
else:
   subject = "Not set"
