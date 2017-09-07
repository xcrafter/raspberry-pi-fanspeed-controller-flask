# IOT Fanspeed Controller (Raspberry Pi Project)

The home environment has seen a rapid introduction of network enableddigital technology. This technology offers new and exciting opportunities to
increase the connectivity of home appliances within the home for the purpose of home automation and remote controlling. Thus the already existing methods for
remote controlling of home appliances are Bluetooth, Zigbee, GSM based technology. But with the help of rapid expansion of the Internet, there is the
potential to control, network and automate the home appliance using it. As we know internet is being popular day by day. Its applications and internet based
devices growing and updating very fast. Internet may conquer the world under its hub in a very short span. So as we choose internet to control the home environment as it removes the connectivity barriers. It is achieved by interfacing the internet with embedded systems. Here a Web based Home appliance control system is implemented to show the remote controlling of home appliances over the web. It can be organized intranet as well as internet based. Here we have implemented an intranet based home appliance control through a web based
interface.


Hardware Requirements
---------------------------------------------------

1. Raspberry Pi ( We use RPi Model B+ )
2. Relay Control
3. Power Supply ( 5v 2amp for PI &amp; Relay, 12V for relay Board )
4. 3V to 5V Step Up Circuit
5. Electric Socket
6. Wifi Module
7. Router

Software Requirements
---------------------------------------------------
1. Flask Webserver
2. HTML & CSS (FrontEnd)
3. Python (Backend)

# Concept Behind the System
We have already seen home appliances are remotely controlled with help
of Bluetooth, Zigbee, RFID, GSM based technologies. The working of the switching
mechanism is as similar to the previous one. It works in such a way that whenever
a 3.3v is generated its step up to 5v and this 5v will turn on the relay and
complete the circuit. This is absolutely a common technique but the innovation
with this system is that the system is controlled over a web page and interfaced
with internet / intranet. One of the main advantages with this is the home
appliances can behave as similar to nodes in computer network. This will make
advantage of networking, remote controlling of this home appliance over a
computer network. As we know one of the paramount factor in computer
network is Internet Protocol (IP). We achieved the system by assigning IP Address
to these home appliances (Conceptually). The device we have used in this IP
Assignment is Raspberry PI. As raspberrypi is connected to a network that IP
address is shared to all of its connected home appliances. Home Appliances can
be determined on the basis of PI’s GPIO pins they are being shared.

# How a Webpage is used to control Home Appliances?
Raspberry Pi is actually a Host Machine which is capable of running a Linux
distro (Here we use Raspbian OS). It is having almost all capabilities of a linux
operating system. In internet computing web pages are delivered using a client
server mechanism. Here we have also a server and no: of clients. Here the server
is raspberry pi. In order to behave like a server we should add server capabilities
to it. In order to achieve this we install Flask Web Server in Raspberry pi. Flask
provides programmability of GPIO Pins as well as processing web requests &amp;
rendering HTML Pages.
Whenever a user clicks on a button in a web interface Javascript will form
the url and send to the flask web server. Flask web server will process the request
according to the query string and in turns make GPIO pin on or off.

# How it can be networked?
Using a wi-fi dongle raspberry pi is connected to a network router. The
DHCP protocol of that router assigns an ip address to the PI. Flask Webserver is
running over an open port in PI. As the port is open the other nodes connected to
that router can access the flask web server running over PI. The other nodes can
be computers, tablets, smartphones, wearables etc…Hence the system is
universally available over a network.

# Block Diagram

![alt text](https://image.ibb.co/n52ceF/Drawing1.jpg "Block Diagram")

https://ibb.co/kH08mv

# Format of url used by another nodes

“http://{IPAddress/hostname}:portnumber”

# Usefull Links

[How to access Raspberry PI over the internet](https://www.raspberrypi.org/documentation/remote-access/access-over-Internet/)

[how-to-run-a-shell-script-at-startup](https://stackoverflow.com/questions/12973777/how-to-run-a-shell-script-at-startup)

