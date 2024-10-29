# UserClientProjectMain
User Client Project



## 3] Users with password and tokens 
dhiraj

dhiraj

b76ff47569b86e1e67619bbe6ba6e303dfdd0315


ramesh

rames@123

71fbf448663f869d2d95444db216a5d45cbc60c1


mangesh

ngesh@123

7a120fb216e9fb3b3641406949b884582378096d


soham

oham@123

80b0280564aaada4b6da845f41edd1df6dabd578


chintu

hintu@123

966b71135031bb8994d43a731e653a46bad7e484



## 4] Test APIs in postman
#### Pass Token in headers

Key : Authorization 

Value : Token token_put_here

#### i.Create Client
POST request - https://userclientprojectmainapp.onrender.com/clients/

need token

Input:

{

    "client_name": "Test Client5"
    
}



#### ii. List all clients
GET request - https://userclientprojectmainapp.onrender.com/clients/


#### iii. Specific Client
GET request - https://userclientprojectmainapp.onrender.com/clients/4


#### iv. Create Project
POST request - https://userclientprojectmainapp.onrender.com/clients/4/projects/

Need Token

Input:

{

    "project_name": "Project Test",
    
    "users": [
    
        {
        
            "id": 1
           
        }
    ]
}

#### v. Update Client Info
PUT request - https://userclientprojectmainapp.onrender.com/clients/4/

Input:

{
    "client_name": "Test Client5 Upgraded"
}

#### vi. Delete Client
DELETE request - https://userclientprojectmainapp.onrender.com/clients/4/

#### vii) Project assigned to logged in user
GET request : https://userclientprojectmainapp.onrender.com/projects/

Need token
