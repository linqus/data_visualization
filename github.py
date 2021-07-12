import requests
from plotly.graph_objs import Bar
from plotly import offline 

url = 'https://api.github.com/search/repositories?q=language:python&sort:stars'

r = requests.get(url)

print(f'status: {r.status_code}')

repos = r.json()
#print(repos.keys())
#print(repos['items'][0])
xs,ys,hovers = [],[],[]
for repo in repos['items']:
	repo_url = repo['html_url']
	repo_name = repo['name']
	ys.append(repo['stargazers_count'])
	xs.append(f'<a href="{repo_url}">{repo_name}</a>' )
	hovers.append(f'{repo["owner"]["login"]}</br>{repo["description"]}')


data = [{
		'type':'bar',
		'x':xs,
		'y':ys,
		'hovertext':hovers,
		'marker':{
			'color':'rgb(60,100,150)',
			'line':{'width':2,'color':'rgb(25,25,25)'}
		},
		'opacity':0.6
		}]

layout = {
	'title':'Top 30 githubowych repozytoriów Pythona',
	'titlefont':{
		'size':20,
		'color':'rgb(10,200,10)',
		'family':'Raleway'
	},
	'xaxis':{
		'title':'Repo',
		'titlefont':{
			'size':24,
			'color':'rgb(200,10,10)',
			'family':'Balto'
		},
	},
	'yaxis':{
		'title':'Gwiazdki',
		'titlefont':{
			'size':24,
			'color':'rgb(10,10,200)',
			'family':'Overpass'
		}
	}
}

offline.plot({'data':data,'layout':layout},filename='gitrepos.html')