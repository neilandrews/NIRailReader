###########################################################################################################################
#
#
#	- url's for train timetables located on the Translink/NI Railways website.
#	- each page may have three tabs (Mon-Fri, Sat, Sun, plus multiple (7+) tables on each tab)
#
#	-- Newry-Belfast / Belfast-Newry
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Inbound/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Outbound/
#
#	-- Belfast-Bangor / Bangor-Belfast
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Inbound1/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-1-Outbound1/
#
#	-- Larne-Belfast / Belfast-Larne
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-2-Outbound/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-2-Inbound/
#
#	-- Londonderry-Belfast / Belfast-Londonderry
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-3-Inbound/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-3-Outbound/
#
#	-- Portrush-Coleraine / Coleraine-Portrush
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-4-Inbound/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Northern-Ireland-Railways-Service-4-Outbound/
#
#	-- Dublin-Belfast / Belfast-Dublin
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Enterprise-Service-5-Inbound/
#	http://www.translink.co.uk/Services/NI-Railways/Routes--Timetables/All-Timetables/Enterprise-Service-5-Outbound/
#
#	--Example of proposed xml markup
#	--A timetable has multiple routes, which have three types of services (weekday, sat & sun), each service has multiple calling poits
#	<timetable>
#		<route line='Newry-Portadown-Lisburn-Belfast'>
#			<weekdayService>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0545'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0551'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0557'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0610'></callingPoint>
#				</service>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0625'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0631'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0637'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0650'></callingPoint>
#				</service>
#			</weekDayService>
#			<satService>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0545'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0551'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0557'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0610'></callingPoint>
#				</service>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0625'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0631'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0637'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0650'></callingPoint>
#				</service>
#			</satService>
#			<sunService>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0545'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0551'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0557'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0610'></callingPoint>
#				</service>
#				<service>
#					<callingPoint Station='Portadown, (NIR) Rail Station' Time='0625'></callingPoint>
#					<callingPoint Station='Lurgan, (NIR) Rail Station' Time='0631'></callingPoint>
#					<callingPoint Station='Moira, (NIR) Rail Station' Time='0637'></callingPoint>
#					<callingPoint Station='Lisburn, (NIR) Rail Station' Time='0650'></callingPoint>
#				</service>
#			</sunService>
#		</route>
#	</timetable
#		
###########################################################################################################################


from BeautifulSoup import BeautifulSoup
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

for feed in feedList:

	print feed.routeDescription
	soup = BeautifulSoup(urllib2.urlopen(feed.url).read())

	#get each tt on the page
	ttList = (soup.findAll(summary="layout table"))

	#note:  ttlist contains data that is not a timetable - notably the smaller textual table that appears abover each actual tt.
	# so we only want to add every other item in ttList to our 'ttGridList'
	parity = 0
	for tt in ttList:

		# i.e. the current index is odd (so we want this data!)
		if parity % 2 != 0: 
			ttGridList.append(tt)
		parity += 1


#print len(ttGridList)






