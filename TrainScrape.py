################################################################################################
#
#
#	- url's for train timetables located on the Translink/NI Railways website.
#	- each page may have three tabs (Mon-Fri, Sat, Sun, plus multiple (7+) tables on each tab)
#	- urls are specified at the start of the program.
#
#	--proposed xml markup
#	--A timetable has multiple routes, which have three types of services (weekday, sat & sun), 
#	--each service has multiple calling points
#		
###########################################################################################################################


from BeautifulSoup import BeautifulSoup
import xml.etree.cElementTree as ET
import urllib2
import math



###  BUILD DATA FEED   ###
class DataFeedItem(object):
    def __init__(self, routeDescription=None, url=None):
		self.routeDescription = routeDescription
		self.url = url

feedList = []

feedList.append(DataFeedItem("Newry, (NIR) Rail Station - Belfast, (NIR) Central Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Inbound/"))
feedList.append(DataFeedItem("Belfast, (NIR) Central Rail Station - Newry, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Outbound/"))

feedList.append(DataFeedItem("Belfast, (NIR) Gt Victoria St (GVS) - Bangor, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Inbound1/"))
feedList.append(DataFeedItem("Bangor, (NIR) Rail Station - Belfast, (NIR) Gt Victoria St (GVS)", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Outbound1/"))

feedList.append(DataFeedItem("Larne Harbour, (NIR) Rail Station - Belfast, (NIR) Gt Victoria St (GVS)", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-2-Outbound/"))
feedList.append(DataFeedItem("Belfast, (NIR) Gt Victoria St (GVS) - Larne Harbour, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-2-Inbound/"))

feedList.append(DataFeedItem("Portrush, (NIR) Rail Station - Belfast, (NIR) Gt Victoria St (GVS)", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-3-Inbound/"))
feedList.append(DataFeedItem("Belfast, (NIR) Gt Victoria St (GVS) - Portrush, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-3-Outbound/"))

feedList.append(DataFeedItem("Portrush, (NIR) Rail Station - Coleraine, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-4-Inbound/"))
feedList.append(DataFeedItem("Coleraine, (NIR) Rail Station - Portrush, (NIR) Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-4-Outbound/"))

feedList.append(DataFeedItem("Dublin, (IE) Connolly Rail Station - Belfast, (NIR) Central Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Enterprise-Service-5-Inbound/"))
feedList.append(DataFeedItem("Belfast, (NIR) Central Rail Station - Dublin, (IE) Connolly Rail Station", "http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Enterprise-Service-5-Outbound/"))
###  BUILD DATA FEED   ###



ttGridList = []

xml_timetable = ET.Element('Timetable')

for feed in feedList:

	xml_route = ET.SubElement(xml_timetable, 'Route')
	xml_route.attrib["line"] = feed.routeDescription

	soup = BeautifulSoup(urllib2.urlopen(feed.url).read())

	#get each tt on the page
	ttList = (soup.findAll(summary="layout table"))

	#note:  ttlist contains data that is not a timetable - notably the smaller textual table that appears abover each actual tt.
	# so we only want to add every other item in ttList to our 'ttGridList
	readThis = False
	currentServiceDay = ''
	for tt in ttList:
 		
		if readThis:

			## We needs to find out what day/s this service runs on.
			dayRow = tt.findAll('tr')[3].findAll('td')[0].text
			##end

			## different tag depending on day
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
			##end

			timetableRows = tt.findAll('tr')
			for row in timetableRows[5:len(timetableRows)-1]:

				stopName = row.contents[0].text
				xml_service = ET.SubElement(xml_day, 'CallingPoint')
				xml_service.attrib["nme"] = stopName

				times = row.findAll('td')

				for time in times:

					thisTime = time.text
					xml_stopTime = ET.SubElement(xml_service, 'Time')
					xml_stopTime.attrib["StopTime"] = thisTime

		   	readThis = False
		else:
		   	readThis = True

					
print '....finished!'

tree = ET.ElementTree(xml_timetable)
tree.write("Trains.xml")
