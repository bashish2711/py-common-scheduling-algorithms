#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
print "Content-type:text/html\r\n\r\n"
print """
<form action="" method = "post" >
<input type = "radio" name = "sch" value = "RR" > Round Robin
<input type = "radio" name = "sch" value = "EDF"> EDF 
<input type = "radio" name = "sch" value = "LLF" > LLF
<input type = "radio" name = "sch" value = "FCFS"> FCFS
<input type="submit" name = "new" value="Add">
<input type="submit" name = "new" value="Remove"> 
"""
print """
         <style>
        table, th, td {
        border: 1px solid black;
        }
        </style>
        </head>
        <body>

        <table id="myTable" >
        <caption>Monthly savings</caption>
         <tr>
         <th>Month</th>
         <th>Savings</th>
          </tr>
          <tr>
            <td>January</td>
            <td>$100</td>
          </tr>
          <tr>
         <td>February</td>
          <td>$50</td>
          </tr>
        </table>
        """

form = cgi.FieldStorage()
policy = form.getvalue('sch')
if form.getvalue('new'): 
   sub = form.getvalue('new')
   print "<h1> %s </h1>" %sub
   print "<h1> %s </h1>" %policy
   if sub == "Add":
      if policy == "RR":
         print """
         <action="" method = "post" >
         <pre> Task-Name:Arrival-Time(A.T):Burst Time(B.T):Period (P):Deadline (D):Real (Hard or Soft): </pre>
         <input type="text" name="task" value="Task" size="3"> 
         <input type="text" name="start_time" maxlength="4" size="3">
         <input type="text" name="burst_time" size="3"> 
         <input type="text" name="period" size="3">
         <select name = "dropdown">
         <option value = "Hard" selected>Hard Real Time</option>
         <option value = "Soft">Soft Real Time</option>
         </select>
	 </form>
          """

	

