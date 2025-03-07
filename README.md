The sentiment score-
This project shows the sentiment score (positive, negative, neutral) of the entered text.

To start the project in your own ec2 instance you need to follow the steps below-
1.	Make sure your files are in the directory as listed below

home/ec2-user/app.py  
home/ec2-user/comprehend.py  
home/ec2-user/templates/index.html  

2.	Once you setup the files add the relevant code into it

3.	Make sure your ec2 instance have all the libraries installed to run the application, for that use the below commands – 
sudo yum install python3-pip -y  
sudo pip install flask  
sudo pip install boto3  

4.	Once you have all the libraries installed on your instance run the flask application using – 
sudo python3 app.py
 
6.	After this go to your browser and type 
[http://<Your-Public-IP-of-ec2>:80]  

 8. If everything is OK you will see a box to enter the text.
