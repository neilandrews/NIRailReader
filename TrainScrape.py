################################################################################################
#
#	TODO // Description // Overview
#		
################################################################################################


from BeautifulSoup import BeautifulSoup
import xml.etree.cElementTree as ET
import urllib2
import math



# data feed object
class DataFeedItem(object):
    def __init__(self, routeDescription=None, url=None):
		self.routeDescription = routeDescription
		self.url = url


# generate feed (from txt file) 
def GenerateFeedList():
	urlFeeds = []

	with open('TimetableUrls.txt') as f:
		lines = f.read().splitlines()


	for i in range(len(lines)):
		
		if (i % 3 == 0):
			urlFeeds.append(DataFeedItem(lines[i], lines[i+1]))

	print len(urlFeeds)
	print urlFeeds[11].url

GenerateFeedList()


# ttGridList = []

# xml_timetable = ET.Element('Timetable')

# for feed in feedList:

# 	xml_route = ET.SubElement(xml_timetable, 'Route')
# 	xml_route.attrib["line"] = feed.routeDescription

# 	soup = BeautifulSoup(urllib2.urlopen(feed.url).read())

# 	#get each tt on the page
# 	ttList = (soup.findAll(summary="layout table"))

# 	#note:  ttlist contains data that is not a timetable - notably the smaller textual table that appears abover each actual tt.
# 	# so we only want to add every other item in ttList to our 'ttGridList
# 	readThis = False
# 	currentServiceDay = ''
# 	for tt in ttList:
 		
# 		if readThis:

# 			## We needs to find out what day/s this service runs on.
# 			dayRow = tt.findAll('tr')[3].findAll('td')[0].text
# 			##end

# 			## different tag depending on day
# 			if (dayRow != currentServiceDay):
# 				if (dayRow == '&nbsp;M-F&nbsp;') :
# 					xml_day = ET.SubElement(xml_route, 'WeekDayServices')
# 					currentServiceDay = '&nbsp;M-F&nbsp;'
# 				elif (dayRow == '&nbsp;S&nbsp;') :
# 					xml_day = ET.SubElement(xml_route, 'SaturdayServices')
# 					currentServiceDay = '&nbsp;S&nbsp;'
# 				elif (dayRow == '&nbsp;Su&nbsp;'):
# 					xml_day = ET.SubElement(xml_route, 'SundayServices')
# 					currentServiceDay = '&nbsp;Su&nbsp;'
# 			##end

# 			timetableRows = tt.findAll('tr')
# 			for row in timetableRows[5:len(timetableRows)-1]:

# 				stopName = row.contents[0].text
# 				xml_service = ET.SubElement(xml_day, 'CallingPoint')
# 				xml_service.attrib["nme"] = stopName

# 				times = row.findAll('td')

# 				for time in times:

# 					thisTime = time.text
# 					xml_stopTime = ET.SubElement(xml_service, 'Time')
# 					xml_stopTime.attrib["StopTime"] = thisTime

# 		   	readThis = False
# 		else:
# 		   	readThis = True

					
# print '....finished!'

# tree = ET.ElementTree(xml_timetable)
# tree.write("Trains.xml")
