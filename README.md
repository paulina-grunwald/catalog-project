# Item Catalog Project  
[![catalogProject.png](https://s25.postimg.org/w8epjomn3/catalog_Project.png)](https://postimg.org/image/6pmd6o32z/)

Developed a content management system using the Flask framework in Python. Authentication is provided via OAuth and all data is stored within a PostgreSQL database. Authenticated users will have the ability to post, edit, and delete their own items.  

####Live version of this project is available at: https://catalog-2016.herokuapp.com/
## Tools and Frameworks
This web application was built with HTML5, CSS, Bootstrap, Vagrant, Flask, SQLAlchemy, Google and Facebook Oauth2 & APIs.
## Instruction
To run the web application:  
1. Install Vagrant and Virtual Box  
2. Clone this repository  
3. Launch the Vagrant VM (by typing `vagrant up` in the directory */udacity-catalog-project* from the terminal).  
4. From directory */udacity-catalog-project/catalog*, initialize the application database by typing `python database_setup.py` follows by `python feedcatalog.py`.  
5. From directory */udacity-catalog-project/catalog*, run the application within the VM by typing `python main.py` into the Terminal.  
6. Access the application by visiting http://localhost:8000 locally on the browser.
