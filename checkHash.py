import sys

dataset = {
"-335242539":"F5 BIG-IP",
"-928274465":"GRAFANA v6.7.4",
"2123863676":"GRAFANA v7.1.0",
"1714852389":"GRAFANA 3.0.0-pre1"
}

if len(sys.argv)<=1:
	print("python checkHash.py <favicon_hash>")
	for x,y in dataset.items():
		print(x+":"+y)
else:
	try:
		print(dataset[sys.argv[1]])
	except:
		print("Error!")
