## Welcome to my ePortfolio

### Self Assessment 

My Computer Science education has prepared me for a future career. This ePortfolio showcases some of the important skills that I’ve gained. One of my courses consisted of a group project which required many students to utilize one repository in GitHub together. This course required clear communication to ensure that everyone made changes that wouldn’t conflict with one another. This project made me confident with group projects that include pushing and commiting changes to a shared repository.  

I have found that communicating to stakeholders is another valuable skill to have. It’s very easy to get a very basic understanding of what a stakeholder expects a project to look like. However, what a developer envisions is often different than what the stakeholder is expecting. Issues like this which are caused by poor communication can cause development delays and they can be costly. I have found that spending the extra time in the beginning of a project can save a lot of time and frustrations when a project is complete. 
 
 Data structures and algorithms play a key role in software development. While every programming language uses these slightly different, I’ve become proficient with arrays and lists. I’ve used these to organize large amounts of data which is required in code I’ve written. I can index a specific element of an array to either use or modify the data. I’ve also proficient in many different types of algorithms, such as using hashing algorithms to securely store passwords. 

I also have strong software engineering and database skills. These two skills work well together because I can write code that interacts with a database. This is a very important step in software development since this allows programs to be much more practical. I can read data, modify it, and then save it back into the database. I’ve used this several times in the past including during a course that heavily utilized SQL. 

Security is a very critical aspect to software development, and it’s something that I try to implement every time I write code. I ensure that anytime a password is used to login, it’s not stored in plaintext in a database or a text file. A hashing algorithm can solve this problem very easily. It’s also important to ensure that SQL input is sanitized or coded in a manner that won’t allow a user to input harmful queries. 

The artifacts that are included below showcase some of my skills that I’ve developed during my education at Southern New Hampshire University. The first artifact, which renders 3D images, will show how software design and engineering skills. The second artifact will show my algorithm and data structure skills, and my database skills. This project uses a graphical user interface to allow employees to login and modify their data. The combination of these artifacts will help showcase the skillset that I’ve built while obtaining my Computer Science degree. 



### Code Review
This  video is a code review that I made. The code review is from the artifacts below, before any enhancements were made to them. I will point out any issues that I see, and how I plan to fix them. 



<iframe width="560" height="315" src="https://www.youtube.com/embed/MJ2W3gtf5lc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




### Software design and engineering

The artifact that I am choosing to use for this portion of my ePortfolio is from an assignment for CS-330 (comp graphic and visualization); this was created last term. This is a C++ project that utilizes OpenGL to render a 3D shape. This artifact is a great choice for my ePortfolio because it showcases multiple different skills. The project is written in C++, so it shows a high level of understanding of this language and how it functions. Using OpenGL shows many skills such as importing and using libraries, using external input to control the camera, and texturing objects in a 3D world. 
	
  This artifact was improved by adding texture to a pyramid which previously just had predefined colors. This required quite a bit of modification to the existing code. The vertex shader and fragment shader had to be modified to accept a texture. The texture had to be loaded from a file, and the shape mesh data had to be modified to accept texture coordinates instead of colors. The render function also had to be modified to bind the texture to the pyramid being displayed.  
The modifications that I made do meet the course objectives; these were the enhancements that I planned to complete for this project. As of now, I don’t have any updates to my outcome-coverage plans since I was able to make all of the changes that I planned. However, I will reevaluate this when I’m completing other projects. If I find that I have inadequate coverage, I will write about these areas in my self-assessment as outlined in the final project rubric. 

  I did learn quite a bit when enhancing this project. I learned how to modify both the vertex and fragment shader code. I then learned how to locate and load an appropriate texture image file. This was challenging to me since many of the images didn’t look professional when applied to the pyramid; I had to find a high-quality image that worked well. I also learned how to modify the shapes mesh data and attrib pointers. This was also challenging to me, since I had to make a lot of changes without being able to test anything until it was completed; I was finally able to get it working after fixing multiple minor mistakes. Everything that I’ve learned in this project will be a great fit for my ePortfolio! 
  
[Download Project](https://drive.google.com/file/d/1BvPQS5n1rIQ_duI41JmX6TpYzZPmw_Cq/view?usp=sharing)


### Algorithm and Data Structures

This artifact was inspired by a project from a previous course that I completed. The project was fairly simple; employees that worked for a zoo would be able to login to a simple program. I believe that the course required the code to be written in Java. Recently, I recreated this project in Python using sqlite3 to connect to a local database. I also utilized tkinter to provide a graphical user interface (GUI). 

I believe that this artifact is a good choice for my ePortfolio to showcase my skills. This artifact displays an understanding of how to encrypt and decrypt a password to provide much better security than storing a plaintext password. My code incorporates sha256 hashing to ensure that the passwords can’t be easily decrypted. The hashing algorithm also utilized something called a salt; this is a randomly generated which gets added to the password to make it even more secure. 
This project does successfully incorporate all of the enhancements that were planned earlier in the course for my ePortfolio. Since this was thoroughly planned out, I don’t think I’ll need to make any changes for my outcome-coverage plans. I will make any changes if the instructor has suggestions to further improve the project. The enhancements made to this project will fulfill the requirements of the course, and they will showcase my skills as a software developer.  

I enjoyed adding these enhancements to this project. While I already knew what hashing was, I had to figure out how to make it work with python on sqlite3. I did struggle when I was trying to read the password from the database to decrypt it. I kept getting datatype errors and didn’t understand why. I figured out that when I retrieved the password from the database, it was getting returned in a tuple. I didn’t realize this, and the decryption algorithm was throwing errors because it wanted a datatype of bytes. Once I realized this, I was able to retrieve the byte data from the tuple and send that to the decryption algorithm. 

[View Project](https://github.com/erik-2021/CS-499/tree/main/Employee_App)


### Database

This artifact demonstrates my abilities to create and manipulate databases. It is python code which utilizes sqlite3 to interact directly with a local database. This project was created to enhance a project that I created in a past course. In the past course, a simple java program was created to allow zoo employees to login. The usernames and passwords were stored in a text file. I wanted to enhance this, so I recreated and enhanced the program in Python. This new project uses sqlite3 to perform CRUD operations on a database. 

I included this artifact in my ePortfolio because I believe that it showcases my skills and knowledge of interacting with a SQL database which is a very good skill to have (Nweke, 2021). To login, a query is made to verify the login credentials are correct. New employees can be created and written to the database. An admin is able to update an employee’s record by loading it via their employee id. An employee can also be deleted from the database. Knowing how to perform these operations are critical to a database, so this is why I’ve chosen this project for my ePortfolio. 

This project does meet the course objectives that I planned out in the early stages of my ePortfolio. Currently, my outcome-coverage plan will not need updated since I was able to successfully complete the changes that I had previously planned for. Prior to starting my ePortfolio I had not practiced my SQL skills for a long time. This left a learning curve that I had to overcome. Working with databases is not something that I’ve done recently so I knew that I would have to relearn some of it. 

I had to refresh my memory on how SQL wanted queries written to interact with the database. This was a small challenge at first, since create, read, update, and delete are all handled slightly different (Python Docs, n.d.). However, after some research I was able to successfully complete all of the queries. I manually verified in the database that the correct changes were being made. I now feel much more confident with my SQL skills since I’ve overcame these challenges. 

[View Project](https://github.com/erik-2021/CS-499/tree/main/Employee_App)



### References
Nweke, B. (2021, June 8). SQL skills (if mastered) will get you better data science opportunities. Medium. Retrieved April 3, 2022, from https://towardsdatascience.com/sql-skills-if-mastered-will-get-you-better-data-science-opportunities-9f912d4f88d3#:~:text=SQL%20is%20used%20by%20over,of%20SQL%20and%20its%20applications. 

Python Docs. (n.d.). SQLITE3 - DB-API 2.0 interface for SQLite databases. sqlite3 - DB-API 2.0 interface for SQLite databases - Python 3.10.4 documentation. Retrieved April 3, 2022, from https://docs.python.org/3/library/sqlite3.html 



