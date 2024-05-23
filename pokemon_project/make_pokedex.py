#paste the output (or pipe the output) of this program to the pokedex.html file.
with open("pokemon.csv","r") as text:
    data = text.read()

#Skeleton for site
site = (f'''
<DOCTYPE HTML>
<html>
  <head>
    <title>
      ?TITLE?
    </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <style>
    ?STYLE?
    </style>
  </head>
  <body>
  ?NAV?
  <h1>
  ?HEADING?
  </h1>
    ?BODY?
 <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD" crossorigin="anonymous"></script>
  </body>
</html>''')
# print(site)

#Author: Mai
#Contract: String -> List
#Description: Takes in the data from the CSV file and returns a list with sublists as rows for the table
data_list = []
for i in data.split("\n"):
    element = []
    element.extend(i.split(","))
    data_list.append(element)
#Tests:
#print(data_list[-1])
#print(data_list[0])
#print(data_list[:10])

#Clean up list and add 2 new columns
data_list.pop(-1)
data_list[0].append("Front")
data_list[0].append("Back")
#print(data_list[-1])

#Author: Mai
#Contract: List -> List
#Description: For each sublist in the original list except the header, append the image for the front and back
for i in data_list[1:]:
    i.append(f"<img src='img/front/{data_list.index(i)}.png'>")
    i.append(f"<img src='img/back/{data_list.index(i)}.png'>")
#Tests:
#print(data_list[9])
#print(data_list[-1])
#print(data_list[0])

poke_types = ["Grass", "Fire", "Water", "Bug", "Normal", "Poison", "Electric", "Ground", "Fairy", "Fighting", "Psychic", "Rock", "Ghost", "Dragon", "Ice", "Flying", "Steel"]

#Author: Mai
#Contract: List -> Dictionary
#Description: With each pokemon type as the key, outputs a dictionary with the values for each key as the pokemon that contain that type
poke_type_dict = {}
for i in poke_types:
    poke_type_dict[i] = [x for x in data_list if i in x] 
    poke_type_dict[i].insert(0,data_list[0])
#Tests:
print(poke_type_dict["Grass"])
print(poke_type_dict["Bug"])
# print(poke_type_dict["Fire"])

#Author: Winnie
#Contract: List -> List
#Description: Takes in a list of top 10 pokemons and outputs a new list that contains the data for each pokemon
top10poke = ["Wigglytuff", "Jigglypuff","Weedle", "Kakuna", "Bulbasaur", "Sandslash", "Mewtwo", "Lapras", "Farfetch'd", "Eevee"]
top10list = []
top10list.append(data_list[0])
for item in top10poke:
    for element in data_list:
        if item in element:
            top10list.append(element)
#Tests:
# print (top10list[5])
# print (top10list[0])
# print (top10list[:3])

#Author: Mai
#Contract: List -> String
#Description: This function takes in a list with data inside and returns the HTML to make that data a table with the first element as the header
def makeHTMLTable(data):
    output = "<table>\n"
    output += "\t<tr>\n"
    for each in data[0]:
        output += f"\t\t<th>{each}</th>\n"
    output += "\t</tr>\n"
    for sub in data[1:]:
        output += "\t<tr>\n"
        for i in sub:
            output += f"\t\t<td>{i}</td>\n"
        output += "\t</tr>\n"
    output += "</table>"
    return output
#Tests:
# print(makeHTMLTable(poke_type_dict["Poison"]))
# print(makeHTMLTable(poke_type_dict["Grass"]))
# print(makeHTMLTable(poke_type_dict["Bug"]))

#nav skeleton
nav_home = ('''
  <nav class="navbar navbar-expand-lg" style="background-color: #629677;">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="https://www.pngmart.com/files/22/Wigglytuff-Pokemon-PNG-Transparent.png"
          alt="wigglytuff" width="80" height="me-auto">
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="homepage.html">HOMEPAGE</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="sub0.html" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                TYPES
              </a>
              <ul class="dropdown-menu">''')
n = 0
#Author: Winnie and Mai
#Contract: String -> String
#Description: This function takes in elements from the poke_types list and outputs the HTML line for each to be added to the navbar
for part in poke_types:
    nav_home += (f'<li><a class="dropdown-item" href="sub{n}.html">{poke_types[n].upper()}</a></li>')
    n += 1
nav_home += (f'''
</ul>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="topten.html">TOP TEN POKEMONS</a>
              </li>
              <li class="nav-item">
              <a class="nav-link" href="allpokemons.html">ALL POKEMONS</a>
              </li>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>''')
# print(nav_home)
#Tests:
#print(f'<li><a class="dropdown-item" href="sub{0}.html">{poke_types[0].upper()}</a></li>')
#print(f'<li><a class="dropdown-item" href="sub{2}.html">{poke_types[2].upper()}</a></li>')
#print(f'<li><a class="dropdown-item" href="sub{5}.html">{poke_types[5].upper()}</a></li>')

#Changes the active navbar class according to page for CSS reasons
nav_top10 = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="top',' active" aria-current="page" href="top')
nav_all = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="all',' active" aria-current="page" href="all')
nav_type = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="sub0',' active" aria-current="page" href="sub0')

#CSS for all pages
gen_style = '''body {background-color: #98b6b1;
    font-family: Garamond, serif;}
    table, td, th {
      border: 2px solid black;
      border-collapse: collapse;
    }
    td,th {
    padding: 10px;}
    h1{
    font-size:70px;
    text-align: center;
    padding:30px;
    font-weight: 500;
    color: #FFFBDB;
    }
    table{
    margin-left:auto;
    margin-right:auto;}
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
.navbar {
    font-family: 'Montserrat', sans-serif;   
}
.navbar-brand {
    padding-left: 30px;
    padding-right: 0px;
}
.navbar-nav {
    padding: 15px;
}
.nav-item {
    padding-left: 10px;
    padding-right: 15px;
    font-size: 108%;
    font-weight: 500;
    
}
.nav-link {
    color: #FFFBDB;
    letter-spacing: 2px;
}
.offcanvas {
    background-color: #629677;
}
.offcanvas-title {
    color: #FFFBDB;
}
h3{
padding-left: 70px;
padding-right: 70px;
}
.center{
display: block;
margin-left: auto;
margin-right: auto;
}
p{
text-align: center;
padding: 40px;
padding-bottom: 20px;
font-size:100%;}
ol{
font-size: 20px;
padding: 100px;
padding-top: 15px;
padding-bottom: 50px;
}
'''
#Author: Mai
#Contract: String -> File
#Description: For each subtype, creates a page containing a table of that subtype's pokemons
subpagenum = 0
for key in poke_type_dict:
    subpage = site.replace("?TITLE?",key).replace("?HEADING?",key).replace("?BODY?",f"{makeHTMLTable(poke_type_dict[key])}").replace("?STYLE?",gen_style).replace("?NAV?",nav_type)
    file = open(f"sub{subpagenum}.html","w")
    file.write(subpage)
    file.close()
    subpagenum += 1
#Tests:
#subpage = site.replace("?TITLE?","Grass").replace("?HEADING?","Grass").replace("?BODY?",f"{makeHTMLTable(poke_type_dict["Grass"])}").replace("?STYLE?",gen_style).replace("?NAV?",nav_type)
# file = open(f"sub0.html","w")
# file.write(subpage)
# file.close()

#subpage = site.replace("?TITLE?","Bug").replace("?HEADING?","Bug").replace("?BODY?",f"{makeHTMLTable(poke_type_dict["Bug"])}").replace("?STYLE?",gen_style).replace("?NAV?",nav_type)
# file = open(f"sub1.html","w")
# file.write(subpage)
# file.close()

#subpage = site.replace("?TITLE?","Poison").replace("?HEADING?","Poison").replace("?BODY?",f"{makeHTMLTable(poke_type_dict["Poison"])}").replace("?STYLE?",gen_style).replace("?NAV?",nav_type)
# file = open(f"sub2.html","w")
# file.write(subpage)
# file.close()

#Creates the all pokemons page
allpage = site.replace("?TITLE?","All Pokemons").replace("?HEADING?","All Pokemons").replace("?BODY?",f"{makeHTMLTable(data_list)}").replace("?STYLE?",gen_style).replace("?NAV?",nav_all)
file = open(f"allpokemons.html","w")
file.write(allpage)
file.close()
#Body of the homepage
#Author: Frank
body_homepage = ('''
<h3>Hello, this is our pokemon website! We have subpages that sort pokemons based on their types, and a page about our top ten pokemons based on a set of criteria. Pokemon from newer generations are not included in this website. This list is based solely on our opinion and should not be taken seriously.</h3>
<img src = "https://www.pngmart.com/files/22/Wigglytuff-Pokemon-PNG-Isolated-HD-Pictures.png" alt = "wiggly" class = "center" width = "300" height = "auto">
<p>This is our favorite pokemon, Wigglytuff. It fits all of our criteria; in addition to looking really cute, it has one of the highest HPs of the pokemons in the list.</p>

<h3>When deciding our favorite pokemon, we analyzed each candidate with a rigorous set of criteria. They are as follows:</h3>
<ol>
    <li>Ideally has two types</li>
    <li>Has a high HP (we want a pokemon strong enough to win battles with!)</li>
    <li>A cool name</li>
    <li>Looks cute</li>    
</ol>
''')
#Creates the homepage
homepage = site.replace("?TITLE?","Homepage").replace("?HEADING?","Homepage").replace("?BODY?",body_homepage).replace("?STYLE?",gen_style).replace("?NAV?",nav_home)
file = open(f"homepage.html","w")
file.write(homepage)
file.close()
#The body of the top 10 page
body_topten = (f"{makeHTMLTable(top10list)}")
#Creates the top ten page
topten = site.replace("?TITLE?","Top Ten Pokemons").replace("?HEADING?","Our Top Ten Pokemons").replace("?BODY?",body_topten).replace("?STYLE?",gen_style).replace("?NAV?",nav_top10)
file = open(f"topten.html","w")
file.write(topten)
file.close()

