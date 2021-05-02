# Django_API


# Sample data already added

     users = [{
          id:1
          name:'user1'
          email:'user1@gmail.com'
          password:'user1password'},
          {
          id:2
          name:'user2'
          email:'user2@gmail.com'
          password:'user2password'},
         {
          id:3
          name:'user2'
          email:'user2@gmail.com'
          password:'user2password'},
         ]
         
    Advisor = [

            {
            id:1
            name:advisor1
            photo_url:advisor1@gmail.com (by mistake) },
            
            {
            id:2
            name:advisor2
            photo_url:advisor2photourl}
            
            {
            id:3
            name:advisor3
            photo_url:advisor3photourl}
            
            
            {
            id:4
            name:advisor4
            photo_url:advisor4photourl}

Use the routs according to the data.

# Available Routs  

1. herokuUrl/admin/advisor/   Method = POST,  Request = name, photo_url,  Return = None, status code 
2. herokuUrl/user/register/   Method = POST, Request = name, email, password, Return = id, jwt token
3. herokuUrl/user/login/      Method = POST, Request = name, passwrod, Return = id, jwt token
4. herokuUrl/user/<id>/advisor/  Method = GET, Request = None , Return = List of advisor  
5. herokuUrl/user/<user_id>/advisor/<adv_id>/   Method= POST, Request = dateTime eg: '25/3/2021 10:22', Return = None , status code
6. herokuUrl/user/<user_id>/advisor/booking/   Method= GET, Request = None, Return = An array of advisor , status code
