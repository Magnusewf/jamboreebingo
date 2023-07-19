#### Read "bingo_tasks.txt" into a list ####
f = open("bingo_tasks.txt", "r")
tasks = f.read().split("\n")
f.close()

#### Make basic bingo table i html format ####
f = open("build/bingo-table.html", "w")

# Add html header to the file:
f.write("""
<!doctype html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />        
<html>
<head><title>Jamboree Bingo</title></head>
<body>
<h1 class = "title">Jamboree Bingo</h1>
</body>        
""")

# Add ccs style to the file:
f.write("""
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 10px;
}
        
.completed {
  background-color: Green;
  color: White;
  text-decoration: line-through;
}

        
</style>
        
""")
completedTASKSarray="0"
for x in range(24):
   completedTASKSarray+=",0"
# Add javascript to the file:
f.write("""
<script>
let completedTASKS = [""")
f.write(completedTASKSarray)
f.write("""]      
function QuestionOK(question,num){
  if (completedTASKS[num]==0){
    question.classList.toggle("completed", true);
    completedTASKS[num]=1;
  }
  else{
    question.classList.toggle("completed", false);
    completedTASKS[num]=0;
  }
}
        
</script>     
           
""")

# Skrver tabellen:
f.write("<table>\n")
for x in range(5):
    f.write("\n<tr>\n")
    for y in range(5):
      f.write(f"<td id=\"{x},{y}\" ")
      f.write(f"onclick=\"QuestionOK(this ,{x*5+y});\"")
      f.write(">")
      f.write(tasks[x*5+y])
      f.write("</td>\n")
    f.write("</tr>\n")
f.write("</table>\n")


# Add ccs style to the file:
f.write("""
<footer>
</footer>
</html>
""")

# Close the file:
f.close()
