from pprint import pprint
import copy

results = open("results.csv").read().strip()
circuits = open("circuits.csv").read().strip()
seasons = open("seasons.csv").read().strip()
races = open("races.csv").read().strip()
drivers = open("drivers.csv", encoding="utf8").read().strip()
constructors = open("constructors.csv").read().strip()
status = open("status.csv").read().strip()

def two_d_list_maker(s):
    lst = []
    for i in s.split('\n'):
        lst.append(i.split(','))
    return lst
two_d_seasons = two_d_list_maker(seasons)
two_d_races = two_d_list_maker(races)
two_d_circuits = two_d_list_maker(circuits)
two_d_results = two_d_list_maker(results)
two_d_constructors = two_d_list_maker(constructors)
two_d_drivers = two_d_list_maker(drivers)
two_d_status = two_d_list_maker(status)

# print(two_d_races)
def dict_maker(data):
    d = {}
    for i in data[1:]:
        d[i[0]] = i[1:]
    return d

dict_seasons = dict_maker(two_d_seasons)
dict_races = dict_maker(two_d_races)
dict_results = dict_maker(two_d_results)

print(dict_results['995'])

def one_info_list(pos,lst):
    new = []
    for i in lst[1:]:
        element = [i[0]]
        element.append(i[pos])
        new.append(element)
    return new

one_info_list_circuits = one_info_list(2,two_d_circuits)
one_info_list_drivers = []
for i in two_d_drivers[1:]:
    element = [i[0]]
    element.append(i[4][:-1] + ' ' + i[5][1:])
    one_info_list_drivers.append(element)
print(one_info_list_drivers[:5])

one_info_list_racenames = one_info_list(4,two_d_races)
one_info_list_constructors = one_info_list(2,two_d_constructors)
one_info_list_status = one_info_list(1,two_d_status)
print(one_info_list_status)
print(one_info_list_circuits)

edited_dict_races = copy.deepcopy(dict_races)

for i in edited_dict_races:
    edited_dict_races[i] = edited_dict_races[i][:6]
    for each in one_info_list_circuits:
        if each[0] == edited_dict_races[i][2]:
            edited_dict_races[i][2] = each[1]

print(edited_dict_races['995'])
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

body_homepage = ('''
placeholder
''')
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
              <a class="nav-link active" aria-current="page" href="home.html">HOME</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="sub0.html" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                TYPES
              </a>
              <ul class="dropdown-menu">''')

for each in sorted(list(dict_seasons.keys())):
    name = (f'{each} Formula One season')
    nav_home += (f'<li><a class="dropdown-item" href="season{each}.html">{name.upper()}</a></li>')
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

nav_top10 = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="top',' active" aria-current="page" href="top')
nav_all = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="all',' active" aria-current="page" href="all')
nav_type = nav_home.replace('class="nav-link active" aria-current="page"','class="nav-link"').replace('" href="sub0',' active" aria-current="page" href="sub0')

def make_season_table(dct,year,two_d):
    output = "<table>\n"
    output += "\t<tr>\n"
    for each in two_d[0][2:7]:
        output += f"\t\t<th>{each}</th>\n"
    output += "\t</tr>\n"
    for i in dct:
        if dct[i][0] == year:
            output += "\t<tr>\n"
            for thing in dct[i][1:]:
              output += f"\t\t<td>{thing if thing.isdigit() else thing[1:-1]}</td>\n"
            output += "\t</tr>\n"
    output += "</table>"
    return output

print(make_season_table(edited_dict_races,'1950',two_d_races))

print(dict_races['995'])

def make_result_table(dct,raceId,two_d):
    output = "<table>\n"
    output += "\t<tr>\n"
    headers = two_d[0][2:6].append(two_d[0][7]).append(two_d[0][9:12]).append(two_d[0][14]).append(two_d[0][17])
    for each in header:
        output += f"\t\t<th>{each}</th>\n"
    output += "\t</tr>\n"
    for i in dct:
        if dct[i][0] == raceId:
            output += "\t<tr>\n"
            for thing in dct[i][1:]:
              output += f"\t\t<td>{thing if thing.isdigit() else thing[1:-1]}</td>\n"
            output += "\t</tr>\n"
    output += "</table>"
    return output

for i in sorted(list(dict_seasons.keys())):
    name = (f'{i} Formula One season')
    head = (f'<a href={dict_seasons[i][0]}>{i} Formula One season</a>')
    subpage = site.replace("?TITLE?",f"{name}").replace("?HEADING?",f"{head}").replace("?BODY?",f"{make_season_table(edited_dict_races,i,two_d_races)}").replace("?STYLE?",gen_style).replace("?NAV?",nav_type)

    file = open(f"season{i}.html","w")
    file.write(subpage)
    file.close()
    
homepage = site.replace("?TITLE?","Home").replace("?HEADING?","Home").replace("?BODY?",body_homepage).replace("?STYLE?",gen_style).replace("?NAV?",nav_home)
file = open(f"home.html","w")
file.write(homepage)
file.close()