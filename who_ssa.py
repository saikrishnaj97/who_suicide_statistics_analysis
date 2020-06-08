from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
cmap = plt.get_cmap("tab10")

client = MongoClient("localhost",27017)
db = client['mydb']
coll = db['bdaproject']

while(1):
	print("\n 1:analyzing number of suicides of each sex(Men and women) \n 2: Counting the number of suicides for each age group \n 3:Analyzing the number of suicides in each year \n 4:Finding countrywise suicides over years \n 5.Insert a record in the dataset \n 6:Deleting the documents \n 7.Updating the documnets in the table \n 8.Finding the documents by country name \n 10.Exit \n " )
	choice = int(input("Enter choice:"))
	if(choice==1):
		print("\n")
		print("count number of suicides for each sex")
		i1 = db.bdaproject.aggregate([{"$group":{"_id":"$sex", "count":{"$sum":"$suicides_no"}}}])
		data1 = []
		dt1 = []
		for item in i1:
			dt1.append(item["_id"])
			data1.append(item["count"])
			print(item)
		fig, ax1 = plt.subplots(figsize=(10, 5))
		print(data1)
		ax1.bar(dt1,data1)
		ax1.set_xlabel("Sex")
		ax1.set_ylabel("Number of suicides")
		plt.title("Number of suicides vs Sex")
		plt.show()
		
	elif(choice==2):
		print("\n")
		print("count number of suicides in each country")
		i2 = db.bdaproject.aggregate([{"$group":{"_id":"$age", "count":{"$sum":"$suicides_no"}}}])
		data = []
		dt = []
		for item in i2:
			dt.append(item["_id"])
			data.append(item["count"])
			print(item)
		#explode = (0,0.1, 0, 0)
		fig1, ax1 = plt.subplots(figsize=(10,5))
		ax1.pie(data,labels=dt, autopct='%1.1f%%',shadow=True, startangle=90)
		ax1.axis('equal')
		plt.title("Pie chart of suicides of each age group")# Equal aspect ratio ensures that pie is drawn as a circle.
		plt.show()

		####	
	elif(choice==3):
		print("\n")
		print("count number of suicides in each year")
		i3 = db.bdaproject.aggregate([{"$group":{"_id":"$year", "count":{"$sum":"$suicides_no"}}}])
		data2 = []
		dt2 = []
		for item in i3:
			dt2.append(item["_id"])
			data2.append(item["count"])
			print(item)
		fig, ax1 = plt.subplots(figsize=(10, 5))
		print(data2)
		ax1.bar(dt2,data2)
		ax1.set_xlabel("Year")
		ax1.set_ylabel("Number of suicides")
		plt.title("Number of suicides vs Year")
		plt.show()
	
	elif(choice==4):
		i4 = db.bdaproject.aggregate([{"$group":{"_id":"$country","count":{"$sum":"$suicides_no"}}},{"$sort":{"count":1}},{"$limit":7}])
		data4 = []
		dt4= []
		for i in i4: 
			dt4.append(i["_id"])
			data4.append(i["count"])
			print(i)
		fig, ax1 = plt.subplots(figsize=(10, 5))
		print(data4)
		ax1.plot(dt4,data4,color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='green', markersize=10)
		ax1.set_xlabel("Country")
		ax1.set_ylabel("Number of suicides")
		plt.title("Line plot of country vs suicide_no")
		plt.show()
	elif(choice==5):
		cname=str(input("Enter country name"))
		iyear=input("Enter the year:")
		isex=str(input("Enter the sex:"))
		iage=str(input("Enter the age:"))
		isuicides_no=input("Enter number of suicides:")
		ipopulation=input("Enter the population:")
		db.bdaproject.insert_one({'country':cname,'year':iyear,'sex':isex,'age':iage,'suicides_no':isuicides_no,'population':ipopulation})
		print("Document inserted")
	elif(choice==6):
		i2=str(input("Enter the country records that are to be deleted:"))
		db.bdaproject.remove({'country':i2})
		print("Documents deleted")
	elif(choice==7):
		i3=str(input("Enter the country name to be updated:"))
		ii3=str(input("Enter the new country name:"))
		db.bdaproject.update_many({'country':i3},{"$set":{'country':ii3}});
		print("Documents updated")
	elif(choice==8):
		i4=str(input("Enter the country name:"))
		abc=db.bdaproject.find({'country':i4})
		for item in abc:
			print(item)
	else:
		exit(0)
