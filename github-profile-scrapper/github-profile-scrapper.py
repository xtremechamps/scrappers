# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json, ast


# Example https://github.com/devendradora

url = "https://github.com/devendradora"
values = {}
def scrap_github_profile(url):
	req = requests.get(url)
	name = url.split("/")
	status = req.status_code

	if status == 200:
		html = BeautifulSoup(req.text, "html.parser")
		values['git_name'] = html.find('span',{'class':'p-name vcard-fullname d-block'}).getText()
		values['git_username'] = html.find('span',{'class':'p-nickname vcard-username d-block'}).getText()
		values['git_description'] = html.find('div',{'class':'p-note user-profile-bio'}).getText()
        values['git_organization'] = html.find('div',{'class':'border-top py-3 clearfix'}).getText()
        print values;
		for a in html.findAll('a',{'href':'/pedrotoba?tab=repositories'}):
			s = a.find('span',{'class':'Counter'}).getText()
			values['git_repositories'] = s.strip(' \t\n\r')

		for a in html.findAll('a',{'href':'/'+name[3]+'?tab=stars'}):
			s = a.find('span',{'class':'Counter'}).getText()
			values['git_stars'] = s.strip(' \t\n\r')

		for a in html.findAll('a',{'href':'/'+name[3]+'?tab=followers'}):
			s = a.find('span',{'class':'Counter'}).getText()
			values['git_followers'] = s.strip(' \t\n\r')

		for a in html.findAll('a',{'href':'/'+name[3]+'?tab=following'}):
			s = a.find('span',{'class':'Counter'}).getText()
			values['git_following'] = s.strip(' \t\n\r')
			
	val_json = ast.literal_eval(json.dumps(values))
	print(json.dumps(val_json, indent=2))



if __name__ == "__main__":
    scrap_github_profile(url)

