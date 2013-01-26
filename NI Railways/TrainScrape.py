################################################################################################
#
#	NI Rail Reader - Web Scraper for NI Rail timetables
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


# generate feed list (from txt file) 
def GenerateFeedList():
	urlFeeds = []
	with open('TimetableUrls.txt') as f:
		lines = f.read().splitlines()
	for i in range(len(lines)):
		if (i % 3 == 0):
			urlFeeds.append(DataFeedItem(lines[i], lines[i+1]))
	return urlFeeds


# start parsing the feeds
def StartParse():
	feedList = GenerateFeedList()
	ttGridList = []
	xml_timetable = ET.Element('Timetable')

	# for each web page / timetable
	for feed in feedList:

		print 'processing feed: ' + feed.routeDescription

		xml_route = ET.SubElement(xml_timetable, 'Route')
		xml_route.attrib["line"] = feed.routeDescription

		soup = BeautifulSoup(urllib2.urlopen(feed.url).read())

		# get each tt on the page
		ttList = (soup.findAll(summary="layout table"))

		# note:  ttlist contains items that are not a timetable - notably the smaller textual table that appears above each actual tt.
		# So we only want to add every other item in ttList to our 'ttGridList'
		ignoreThis = True
		currentServiceDay = ''
		for tt in ttList:
	 		# ignore every other table - i.e the title tables
			if ignoreThis:
				ignoreThis = False
				continue
			else:
				ignoreThis = True

			# We needs to find out what day/s this service runs on. e.g. 'M-F'
			dayRow = tt.findAll('tr')[3].findAll('td')[0].text

			# Different tag depending on day of service
			if (dayRow != currentServiceDay):
				if (dayRow == '&nbsp;M-F&nbsp;') :
					xml_day = ET.SubElement(xml_route, 'WeekDayServices')
					currentServiceDay = '&nbsp;M-F&nbsp;'
				elif (dayRow == '&nbsp;S&nbsp;') :
					xml_day = ET.SubElement(xml_route, 'SaturdayServices')
					currentServiceDay = '&nbsp;S&nbsp;'
				elif (dayRow == '&nbsp;Su&nbsp;'):
					xml_day = ET.SubElement(xml_route, 'SundayServices')
					currentServiceDay = '&nbsp;Su&nbsp;'

			timetableRows = tt.findAll('tr')

			# number of rows & tables we need to iterate through
			tdCount = len(tt.findAll('tr')[3].findAll('td'))
			trCount = len(timetableRows)

			for n in xrange(0, tdCount-1):
				# new service
				xml_service = ET.SubElement(xml_day, 'Service')

				for m in xrange(5, trCount):
					# station name
					stationName = tt.findAll('tr')[m].findAll('th')[0].text

					# stop time
					stopTime = tt.findAll('tr')[m].findAll('td')[n].text
					if (stopTime == '&nbsp;...&nbsp;'):
						stopTime = ""
					else:
						stopTime = stopTime[6:10]

					# location and time of each stop
					xml_stop = ET.SubElement(xml_service, 'Stop')
					xml_stop.attrib["Station"] = stationName
					xml_stop.attrib["Time"] = stopTime

	tree = ET.ElementTree(xml_timetable)
	tree.write("Trains.xml")

#run program
StartParse()