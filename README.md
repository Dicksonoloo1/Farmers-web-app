

PROJECT NAME:        MKULIMA WEB APPLICATION
UNIT NAME:              COMMERCIAL PROGRAMMING
UNIT CODE:               ICS 2309
LECTURER:             PROF  JOSEPH WAFULA
MEMBERS
DICKSON.O. OLOO: SCT211-0768/2016
CORNELIUS NYATIKA: SCT211-0397/2018
MONICAH ATIENO: SCT211-0616/2018
OLIVER MUGAMBI: SCT211-0320/2018
DORCAS ACHIENG: SCT211-0039/2018


PROBLEM STATEMENT
Farmers incur huge storage and marketing cost after harvesting their crops this software program will link farmers and warehouse owners and provide marketing facilities to tackle this problem
BRIEF DESCRIPTION
The primary function of this app is to offer timely services that have been crippling the agricultural sector, notably storage spaces and marketing opportunities. Essentially, the app links the farmers to nearby empty storage facilities that are cost-friendly and within their vicinity. Regarding marketing opportunities, the app will offer suitable platforms to market and eventually connect with potential customers. Consequently, losses encountered due to overstaying of produce and possible damage of produce will be overcome while increasing revenue to the farmers.
OBJECTIVES
1.To link farmers with warehouse owners.
2.To provide an easy-to-use application to help farmers advertise their produce.
JUSTIFICATION 
Particularly in third-world countries, crucial resources that support the marketing and storage of farm products have been a hurdle for many farmers and those hoping to enter into the farming business. Few storage facilities which are poorly maintained and equipped are available, making it hard for the farmers to be sure of the state of their produce. At the same time, marketing and reaching potential buyers is challenging considering the level of education and lack of an effective communication medium. And thus, this is where our application comes in to narrow this existing gap to boost farmers' operations for increased productivity and performance.
TECHNOLOGIES TO USE 
Client-Side Programming
Hypertext Markup Language (HTML) 
Cascading Style Sheets (CSS). 
JavaScript (JS). 
Server-Side Programming 
Python (Django) 
Database (MySQL)
Docker: Key in Virtualization through Containerization
Kubernetes: Key in Deployment, Scaling, and Management
Apache Kafka: Key in Messaging and Streams Processing
FUNCTIONAL REQUIREMENT.
1. Registration management:
user management: - includes registration of users and management of login credentials.
2. Product upload and management:
Farmers need to upload and manage their products in the web application. during upload the farmer must select the relevant category provided for the produce. Other details required include produce name, short description, amount of produce in stock and the price.
Farmers: Record the amount of produce to store, market produce on the site, search and book storage space, make sale online
Warehouse owners: record storage space and location, manage available storage space periodically.
3. Search produce: The App allows the user to search for a desired crop.

Non-Functional Requirements.
1. Scalability: The different modules used in Mkulima shall scale accordingly when the number of requests grow.
2. Security: The system, especially the back end, shall be secure and ready to stop any
malicious attacks. Passwords shall be encrypted for both the Web application.
3. Usability: The Application shall have simple and user-friendly interfaces.
4.  Availability: The system as a whole shall be operational and not experience any down
time.
5. Performance: The system back end shall receive, process, and deliver data in timely
fashion without any timeouts.
WORK‌ ‌BREAKDOWN‌ ‌STRUCTURE‌ ‌DICTIONARY‌
No
Item
Description
1
WBS Code
Mkulima Web App 1.0
2
Responsible Individuals
Dorcas Oloo - SCT211-0039/2018
Dickson Oloo - SCT211-0768/2016
Cornelius Nyatika - SCT211-0397/2018
Monica Atieno - SCT211-0616/2018
Oliver Mugambi- SCT211-0320/2018
3
Description
The Mkulima web app's scope included:
    1. Connecting farmers with warehouse owners with sufficient space to store their produce at a fee (monthly or annually).
    2. Providing farmers with a marketing tool where they can advertise their stored products and connect with prospective clients at a fee.
4
Deliverables
The primary deliverable will be a web application that allows farmers to accomplish the objectives defined within the project's scope definition. These objectives include connecting farmers with warehouse owners where they can lease space, and providing an advertisement platform for farmers at a fee.
5
Acceptance Criteria
The final product should have all the following functions:
    1. User registration and management, including registration of farmers and warehouse owners and their login facilities.
    2. Farmers should be able to upload their products details to their profiles for marketing and management.
    3. Warehouse owners should be able to manage their warehouse vacancy and leasing details in their profiles
    4. Farmers should be able to search and contact suitable warehouse owners based on their storage requirements.
    5. Farmers should also be able to receive orders from potential customers on the web app and provide the necessary directions to complete a sale.
    6. The web applications should be easy to use, attractive, fast, and secure to protect the users' data.
6
Budget
For this leg of the work breakdown structure (WBS) leg, the summary budget will range between Kes. 50,000, including the costs for project implementation, conducting extensive alpha and beta tests, hosting the projects in the public domain, and administration fees.
7
Milestones
    1. Architectural setup and diagram for the project
    2. Installation and setup of project dependencies and tools, including Docker, Kubernetes, Python, and Kafka.
    3. User interface design
    4. User Management module
    5. Farmers' inventory management module
    6. Warehouse owners inventory management module
    7. Farmer-warehouse owner connection module
    8. Advertisement for farmers' products module
8
Risks
The most prevalent threat to this project will be the low technological use by farmer's in Kenya today, which can result in low application utilization. Low utilization of the application by the farmers will limit the apps ability to meet the project aim of reducing product wastage due to lack of storage in most Kenyan farms. 
9
Additional Information
The Mkulima web application will introduce Kenyan farmers to additional storage facilities that will reduce the wastage of agricultural products from rodents and decay due to poor storage. Therefore, This app will revolutionize how farmers approach product storage and decouple the process from the food production procedures.
10
Approvals
All approvals will be conducted by the projects steering committee, led by the project sponsor.

‌MILESTONES AND TIMELINES 



 Title

 Notes

1.

 7/10/2021

 Architectural Set Up and Diagram.  

 Design and draw architectural diagrams to illustrate how the various modules work together.
 

2.

 10/10/2021
 
 Local Development


 Set up a local development environment. Install all the dependencies and platform tools: Python, Django, Kubernetes  Docker, Docker Compose, Kafka etc.


3.

 13/10/2021

 Containerization‌ ‌
 
 Package‌ ‌each‌ ‌module‌ ‌with‌ ‌Docker,‌‌
and‌ ‌publish‌ ‌Docker‌ ‌images‌ ‌on‌ ‌Docker‌‌
hub.‌ ‌


4.

 17/10/2021
 
 User Interface Design. 


  Design the interface for users to upload, view edit or delete products, register and login.


5.

 20/10/2021

 User registration and verification.
 
 User will be able to register and verify their accounts via gmail.


6.

 21/10/2021
 
 Password Reset.
 
 Allow users to reset password via gmail.


7. 

 21/10/2021

 User Profile.
  
 A profile will be automatically generated each time a  new user is created in the system. Users will also be able to update their details, such us email, username, occupation etc… 


 7.2 

 
 25/10/2021
 
 Farmers  Contact Profile.

 Farmer will be able to create a contacts profile to so as to connect with potential buyers.


8.

 30/10/2021
 
 Login 
 
 Users will login using email or username and password.


9. 

4/11/2021
 
 Product management.

 
 Users will be able to view their entire list of products available in the system, view the details for each product, edit or delete products (  edit and delete actions to be performed by the user who created the product and must be logged into the system)


10. 

 7/10/2021
 
 Subscriptions.
  
 Users will be offered subscriptions so as to access the application services . These include Storage and Produce subscriptions.

 
11.

 10/10/2021
 
 Admin Panel.
 
 ‌The admin is to manage‌ ‌users‌ ‌and‌‌
 facilitate‌ ‌authentication‌ ‌across‌ ‌the‌‌
system.‌ ‌


12.

 9/10/2021
  
 Search Products.
 
 Create an endpoint to allow users to search for products by the product name.


 13. 


 12/10/2021
 
 Inventory management.

 Create a service to track the status of all products.

14. 

 
 14/10/2021

 Warehouse management.
 
 Create a service for the owners to track the status and availability of warehouses in the system.

 
15. 


 17/10/2021

 Connection module

 Create a module where the farmers and warehouse owners to connect with each other.

 
16. 


 21/10/2021

 Orders Table.

 Farmers will be able to review orders from potential buyers.


MONETIZATION
Our monetization strategy will be through subscriptions. 
We offer two forms of subscriptions to our users:
Storage subscription
This is a type of subscription which applies to warehouse owners who want to advertise storage availability in their warehouses.
Here a warehouse owner has to subscribe to a subscription plan and make payments before his/her storage advert is displayed on the website.
Produce subscription
This is another type of subscription that applies to farmers who want to advertise their produce in the website.
A farmer who wishes to advertise his/her produce on the website will be required to choose a subscription plan and make payment to the Mkulima Web app to have their produce displayed on the website.
For both types of subscriptions, the subscription plan will be monthly or yearly and the payments will be made to the Mkulima Mpesa Till number which will be provided in the website.
On the other hand, all other transactions involving a farmer and a customer or a farmer and a warehouse owner will be handled by the individual parties involved.
 

ARCHITECTURAL  DIAGRAM 
Website architecture
