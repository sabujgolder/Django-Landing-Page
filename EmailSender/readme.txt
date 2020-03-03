This projects is usefull for people who want to build a website for a particular service then rank it on top of the page,
can gather a few requests from clients and finally sell the website to a firm who can make use of those requests in
their business.

for running the project:

1. go to settings.py and replace sender mail with your mail and password with your password.If you can buy bulk email
 service then you can use that instead of you mail and password.For security reason open a gmail only for sending client requests to your 
 mail.

EMAIL_HOST_USER = 'sender email'
EMAIL_HOST_PASSWORD = 'sender email password'

2. then go to views.py and replace 'recepeint email' with the email you want to receive the mail sent by the client

recepient = str('recepeint email')

3. for making the google map location service you need to activate your api from developer account by sigining in google deveopler
   by using any gmail password(Note it costs a few dollars to use this service).After getting the google map api key replace it below
   in the map.html.
	
	  <script async defer src="https://maps.googleapis.com/maps/api/js?key='write down your api key'&callback=initMap">

4. run the project.

