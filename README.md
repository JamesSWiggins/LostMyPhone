# [The 'I Lost My Phone' serverless, IoT button](https://medium.com/@james.s.wiggins/the-i-lost-my-phone-serverless-iot-button-d3550b89ec79)

![alt text](https://cdn-images-1.medium.com/max/1000/1*dLsOIvaA8xO7ao953IgACQ.png)

### The ‘I lost my phone’ serverless, IoT button
This is a tutorial about technology, but it starts with my wife and three young children. Due to a very busy lifestyle and the fact that women’s clothes often lack functional pockets, it’s common that we’ll lose my wife’s phone somewhere in the house.
The usual outcome of this scenario is “James! Would you call my phone?!” After a few tries and some wandering around we can usually find it in a place that only a 1 to 5 year old would choose to put a phone. If I’m not home though, this presents a whole new problem. We haven’t had a landline in quite some time, so the next step is logging into iCloud and… 
It’s inconvenient.
So, while I was digging into serverless computing recently I really wanted to find another practical use-case to implement. Enter the ‘I lost my phone’ serverless, IoT button. You just press the button and seconds later your phone rings! So now, my wife can take the button with her around the house and press it as many times as she needs to until her phone makes it’s location clear.
It’s pretty functional, but it’s also a great way to get your feet wet with IoT and Lambda Functions on AWS. Best of all, with the exception of the Button itself, all of the features of AWS and Twilio used here are within their ‘free tiers’!
### Step 1: Get an IoT Button
The first thing you’ll need to do is buy an IoT Button which you can get from (surprise!) Amazon. It’s $20, but when you consider what the thing actually does its pretty amazing.
### Step 2: Sign Up for Twilio
A lot of the heavy lifting here is actually done by Twilio, an amazing service the does pretty much anything you can imagine with phone calls (check out their presentation at AWS re:Invent 2016). We’ll need a developer API key to make the phone calls, but don’t worry, everything we’re doing is in their free tier. Go ahead an sign up for an account and copy down your Account SID and Auth Token.
### Step 3: Edit Your Lambda Function Code
To connect the button presses to Twilio, we’ll use a small Python function that implements the Twilio API. Go ahead and clone the code from my GitHub Repo.
You’ll need to edit the main function in lambda_function.py and provide your Twilio credentials as well as the phone number you want to call (your wife’s or otherwise). It’s pretty straightforward.

![alt text](https://cdn-images-1.medium.com/max/800/1*OtnnqpmBDBPEei6LqcHfng.png)

At first glance it might seem like AWS Lambda can only execute functions that exist in a single file, but that’s not the case. You can have a Lambda function that contains lots of file, but you need to zip them all up first. Once you’ve edited our main function in the ‘lambda_function.py’ file, go ahead and zip it up along with all of the sub-directories in the repo.

![alt text](https://cdn-images-1.medium.com/max/800/1*QtIILWeUxFeIQj1DBJeYhw.png)

### Step 4: Set Up Your IoT Configuration
Follow the Getting Started Configuration Wizard to get the Button set up on AWS and ready to call your Lambda function. Be sure to download the certificate files created during this process and save them in a safe place. You’ll need to put these on your IoT button later to authenticate it.
When you are prompted to configure your Lambda function, select Python 2.7 as the runtime. Initially, you’ll see where you could write your Lambda function right in the browser, but we want to provide our own function with it’s dependencies in a zip file. Select ‘Upload a .ZIP file’ from the ‘Code entry type’ drop down box and provide the code we zipped up earlier.

![alt text](https://cdn-images-1.medium.com/max/800/1*ZgPrslWP_Mscj4pdhflw2A.png)

Be sure to set the ‘Handler’ field to ‘lambda_function.lambda_handler’. This is what tells Lambda where to look for our main Python function ‘filename.functionname’.
Roles are a way to govern security and permissions with AWS and are a really important concept. Security on AWS is a deep subject, but one that’s definitely worth understanding. Be sure to give your AWS Role a clear name so that you’ll remember what it was used for in the future.

![alt text](https://cdn-images-1.medium.com/max/800/1*JRv9i7QL73DZGuGMAZ117g.png)

### Step 5: Connect your IoT Button and Test!
Almost there! Now you can follow the instructions to connect your IoT Button to your WiFi network and upload your certificate files. Once that’s done, give it a press! Now reflect back on the diagram at the top of this article and marvel at all of the technology magic that’s actually happening to make that phone call. Best of all, there are NO SERVERS that you need to pay for, patch, or troubleshoot to make this work!
