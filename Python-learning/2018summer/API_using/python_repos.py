import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Stasus code:",r.status_code)
response_dict=r.json()
print(response_dict.keys())
print("Total respostories",response_dict['total_count'])

repo_dicts=response_dict['items']
print("Respositories returned:",len(repo_dicts))

#The first Repo
repo_dict=repo_dicts[0]
print("\nkeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)
print("Name:",repo_dict['name'])
print("Owner:",repo_dict['owner']['login'])
