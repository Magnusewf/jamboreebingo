#### Read "bingo_tasks.txt" into a list ####
f = open("bingo_tasks.txt", "r")
tasks = f.read().split("\n")
f.close()

#### Make basic bingo table i html format ####
f = open("build/bingo-table.html", "w")

# Add html header to the file:
f.write("""<!doctype html>
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
  .content {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
  }
  .content .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: rgb(248, 233, 210);
    color: black;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    
    /* Position the tooltip */
    position: absolute;
    z-index: 1;
    top: 100%;
    left: 50%;
    margin-left: -60px;
  }
  .content:hover .tooltiptext {
    visibility: visible;
  }
</style>
<style>
h1{
  text-align: center;
  color: rgba(0, 0, 0, 0.716)
}
body {
  background: beige;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 10px;
}       
.completed {
  background-color: rgb(67, 105, 67);
  color: beige;
  text-decoration: line-through;
}

table {
  width: min(90%, 600px);
  table-layout: fixed;
  margin-left: auto; 
  margin-right: auto;
}
td .content {
  text-align: center;
  
  aspect-ratio: 1 / 1 ;
  
}  
</style>       
""")

completedTASKSarray="0"
for x in range(24):
   completedTASKSarray+=",0"

# Add javascript to the file:
f.write("""        
<script>
// #### Basic cookie functions: ####
function setCookie(cname, cvalue, exdays) {
       const d = new Date();
       d.setTime(d.getTime() + (exdays*24*60*60*1000));
       let expires = "expires="+ d.toUTCString();
       document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
     }
function getCookie(cname) {
       let name = cname + "=";
       let decodedCookie = decodeURIComponent(document.cookie);
       let ca = decodedCookie.split(';');
       for(let i = 0; i <ca.length; i++) {
         let c = ca[i];
         while (c.charAt(0) == ' ') {
           c = c.substring(1);
         }
         if (c.indexOf(name) == 0) {
           return c.substring(name.length, c.length);
         }
       }
       return"";
}

// #### Check if cookie exist, if not create it: ####                
if (getCookie("completedTASK") != "") {
  var completedTASKS = JSON.parse(getCookie("completedTASK"));
 }
else {
  var completedTASKS = [""")
f.write(completedTASKSarray)
f.write("""]; 
  setCookie("completedTASK", JSON.stringify(completedTASKS), 400);
}        
        
// #### Function to toggle completed tasks: ####    
function QuestionOK(question,num){
  if (completedTASKS[num]==0){
    question.classList.toggle("completed", true);
    completedTASKS[num]=1;
  }
  else{
    question.classList.toggle("completed", false);
    completedTASKS[num]=0;
  }
  setCookie("completedTASK", JSON.stringify(completedTASKS), 400);
}

// #### Function to load completed tasks - called later: ####        
function loadCompletedTasks(){
  for (var i = 0; i < 25;i++){
    if (completedTASKS[i]==1){    
      document.getElementById("q"+i).classList.toggle("completed");
    }
  } 
}        

</script>    
           
""")

# Skrver tabellen:
f.write("<table>\n")
for x in range(5):
    f.write("\n<tr>\n")
    for y in range(5):
      f.write(f"<td id=\"q{x*5+y}\" ")
      f.write(f"onclick=\"QuestionOK(this ,{x*5+y});\"")
      f.write("><div class=\"content\">")
      f.write(f"Task {x*5+y+1}")
      f.write(f"<span class=\"tooltiptext\">{tasks[x*5+y]}</span>")
      f.write("</div></td>\n")
    f.write("</tr>\n")
f.write("</table>\n")


# Add ccs style to the file:
f.write("""
        
<script>
loadCompletedTasks();
</script>
              
<footer>
</footer>
</html>
""")

# Close the file:
f.close()
