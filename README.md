# Shaku - Body Measurement

**AI-powered Human Body Measurement from 2D Images**  

Shaku is designed to revolutionize online fashion and clothing shopping by providing **highly accurate body measurements** using AI. By leveraging front and side images, the service calculates precise dimensions to help users find perfectly fitting clothes, reducing returns and increasing satisfaction.

---

<img width="1181" height="1315" alt="Add da subheading" src="https://github.com/user-attachments/assets/a808dc37-d607-4978-9653-767a94770861" />

## Overview

Shaku is an AI-powered platform designed to revolutionize the fashion and apparel industry by providing highly accurate body measurements. Using state-of-the-art computer vision and machine learning techniques, Shaku analyzes two simple 2D images (front and side) of a user to calculate precise body dimensions.

The platform addresses common challenges in online fashion retail, including fit uncertainty, high return rates, and customer dissatisfaction. By providing precise body measurements, it ensures that customers receive clothing that fits perfectly the first time, reducing the need for returns and exchanges. This not only saves costs for retailers but also enhances customer trust and brand loyalty.

This platform delivers a complete AI-driven solution for accurate body measurement, helping online clothing brands and e-commerce platforms improve customer satisfaction, minimize returns, and boost sales and engagement.
 
## Architecture & Workflow

1. **Input**: Users upload **front and side images**. Images should be clear, full-body, and well-lit.
2. **Processing**: AI detects body keypoints and calculates measurements based on anthropometric ratios and image coordinates.
3. **Output**: Returns a JSON containing numeric measurements in **centimeters** and detailed **coordinates** for each body part.
4. **Error Handling**: Validates image quality and ensures accurate measurement calculations. Returning a descriptive error if images are unsuitable.


## Integration

### 1. API Integration
Shaku provides a robust and flexible API that allows developers to integrate body measurement capabilities directly into websites, e-commerce platforms, or mobile applications. The API is designed for fast and reliable performance, capable of handling multiple requests simultaneously while delivering precise measurements.

Developers can customize endpoints, parameters, and responses to fit their business requirements, whether it’s an online clothing store, virtual fitting platform, or health and fitness app. Using the API directly provides full control over requests and responses, making it suitable for projects that require customized workflows or complex integrations.

You can explore and test the API via logging to the Shaku Dashboard:
[Shaku Dashboard - Login & Test](https://dashboard.shaku.tech/auth/login)

Below are example HTTP requests for Python, PHP, and Node.js that you can also try in Postman:

#### 1.1. Authentication (API Tokens)
 - **Get Access Token**
   
   Use this endpoint to log in with client ID, client secret, username, and password to receive an access token.
   
   - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/oauth/token"
      
      payload = json.dumps({
        "grant_type": "password",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_SECRET_KEY",
        "username": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD"
      })
      headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
      
      ```

   - **PHP**
      ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/oauth/token',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "grant_type":"password",
          "client_id":"YOUR_CLIENT_ID",
          "client_secret":"YOUR_SECRET_KEY",
          "username":"YOUR_EMAIL_ADDRESS",
          "password":"YOUR_PASSWORD"
      }',
        CURLOPT_HTTPHEADER => array(
          'Content-Type: application/json',
          'Accept: application/json'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;

      ```
   - **Node.Js**
      ```javascript
      var request = require('request');
      var options = {
        'method': 'POST',
        'url': 'https://api.shaku.tech/oauth/token',
        'headers': {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          "grant_type": "password",
          "client_id": "YOUR_CLIENT_ID",
          "client_secret": "YOUR_SECRET_KEY",
          "username": "YOUR_EMAIL_ADDRESS",
          "password": "YOUR_PASSWORD"
        })
      
      };
      request(options, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body);
      });

      ```
  - **Refresh Token**
    
    Refresh the access token when it expires.
     
    - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/oauth/token"
      
      payload = json.dumps({
        "grant_type": "refresh_token",
        "refresh_token": "YOUR_REFRESH_TOKEN",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_SECRET_KEY"
      })
      headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'shaku_session=N3tqPfDYa4oCHa1YBkWLIfHoiuJ7LvuRIZZ0Kbna'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
      
      ```

    - **PHP**
      ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/oauth/token',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "grant_type":"refresh_token",
          "refresh_token":"YOUR_REFRESH_TOKEN",
          "client_id":"YOUR_CLIENT_ID",
          "client_secret":"YOUR_SECRET_KEY"
      }',
        CURLOPT_HTTPHEADER => array(
          'Content-Type: application/json',
          'Accept: application/json',
          'Cookie: shaku_session=N3tqPfDYa4oCHa1YBkWLIfHoiuJ7LvuRIZZ0Kbna'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;


      ```
    - **Node.Js**
      ```javascript
      var request = require('request');
      var options = {
        'method': 'POST',
        'url': 'https://api.shaku.tech/oauth/token',
        'headers': {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Cookie': 'shaku_session=N3tqPfDYa4oCHa1YBkWLIfHoiuJ7LvuRIZZ0Kbna'
        },
        body: JSON.stringify({
          "grant_type": "refresh_token",
          "refresh_token": "YOUR_REFRESH_TOKEN",
          "client_id": "YOUR_CLIENT_ID",
          "client_secret": "YOUR_SECRET_KEY"
        })
      
      };
      request(options, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body);

      ```

   - **Revoke Token**
    
     Revoke an access token to log out or terminate access.
     
     - **Python**
       ```python
       import requests
       
       url = "https://api.shaku.tech/api/v1/auth/revoke"
       
       payload = ""
       headers = {
         'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
         'Cookie': 'shaku_session=oQhS4k3h5QBHs77YoGVKhEwsWmtu8E48lr4sTimt'
       }
       
       response = requests.request("GET", url, headers=headers, data=payload)
       
       print(response.text)
            
       ```

     - **PHP**
       ```php
       <?php
       
       $curl = curl_init();
       
       curl_setopt_array($curl, array(
         CURLOPT_URL => 'https://api.shaku.tech/api/v1/auth/revoke',
         CURLOPT_RETURNTRANSFER => true,
         CURLOPT_ENCODING => '',
         CURLOPT_MAXREDIRS => 10,
         CURLOPT_TIMEOUT => 0,
         CURLOPT_FOLLOWLOCATION => true,
         CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
         CURLOPT_CUSTOMREQUEST => 'GET',
         CURLOPT_HTTPHEADER => array(
           'Authorization: Bearer YOUR_ACCESS_TOKEN'
         ),
       ));
       
       $response = curl_exec($curl);
       
       curl_close($curl);
       echo $response;
 
 
       ```
     - **Node.Js**
       ```javascript
       var request = require('request');
       var options = {
         'method': 'GET',
         'url': 'https://api.shaku.tech/api/v1/auth/revoke',
         'headers': {
           'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
         }
       };
       request(options, function (error, response) {
         if (error) throw new Error(error);
         console.log(response.body);
       });
       ```

#### 1.2. Body Measurement API Service

 
  Measure a person’s body from two images (full-view and side-view). This service returns detailed measurements like Chest, Waist, Hips, Shoulder, Neck, and more.
 
   - **Python**
     ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/api/v1/services/sizeMeasurement"
      
      payload = json.dumps({
        "present_height": "YOUR_HEIGHT",
        "img_full_view_body": "IMAGE_BASE64_FORMAT",
        "img_side_view_body": "IMAGE_BASE64_FORMAT",
    
      })
      headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'Content-Type': 'application/json',
        'Cookie': 'shaku_session=N3tqPfDYa4oCHa1YBkWLIfHoiuJ7LvuRIZZ0Kbna'
      }
      
      response = requests.request("POST", url, headers=headers, data=payload)
      
      print(response.text)
          
     ```

- **PHP**
  
  ```php
      <?php
      
      $curl = curl_init();
      
      curl_setopt_array($curl, array(
        CURLOPT_URL => 'https://api.shaku.tech/api/v1/services/sizeMeasurement',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS =>'{
          "present_height":"YOUR_HEIGHT",
          "img_full_view_body":"IMAGE_BASE64_FORMAT",
          "img_side_view_body":"IMAGE_BASE64_FORMAT"
      }',
        CURLOPT_HTTPHEADER => array(
          'Authorization: Bearer YOUR_ACCESS_TOKEN',
          'Content-Type: application/json',
          'Cookie: shaku_session=N3tqPfDYa4oCHa1YBkWLIfHoiuJ7LvuRIZZ0Kbna'
        ),
      ));
      
      $response = curl_exec($curl);
      
      curl_close($curl);
      echo $response;


  ```
- **Node.Js**
    ```javascript
       var request = require('request');
       var options = {
         'method': 'POST',
         'url': 'https://api.shaku.tech/api/v1/services/sizeMeasurement',
         'headers': {
           'Authorization': 'Bearer '
         },
         body: JSON.stringify({
           "present_height": "",
           "img_full_view_body": "",
           "img_side_view_body": ""
         })
       
       };
       request(options, function (error, response) {
         if (error) throw new Error(error);
         console.log(response.body);
       });

    ```

- **SDK Integration**
  
  For simpler and faster integration, you can test directly on the Dashboard or use the Python package.
  - [Shaku Dashboard - Login & Test](https://dashboard.shaku.tech/auth/login)
  - Install via PyPI:
    ```python
    pip install shakuapi
    ```
    
    Python Example:

    ```python
    from shakuapi import ShakuClient

    client = ShakuClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")
    
    # login
    client.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")
    
    # get size measurement
    result = client.size_measurement(
        present_height=YOUR_HEIGHT,
        img_full_view_body="full_view.jpg",
        img_side_view_body="side_view.jpg"
    )
    
    print(result)

    ```


## Pricing

Shaku offers a cost-effective and scalable solution that provides maximum features for online fashion and apparel businesses. By reducing return rates and improving customer satisfaction, Shaku helps businesses increase revenue and optimize operations. Pricing plans are designed to accommodate small shops to large enterprises, ensuring that every business can benefit from AI-powered body measurement technology. For detailed pricing, subscription plans, and enterprise solutions, visit [Shaku Pricing](https://shaku.tech/#pricing)

## Application

Shaku also offers a mobile application that brings AI-powered body measurement tools directly to users’ smartphones. The app allows users to capture their front and side images, receive instant measurements, and track changes over time. This mobile accessibility ensures that users can benefit from accurate body measurements anytime and anywhere, enhancing convenience and engagement. The app can also serve as a complement to your e-commerce platform, providing users with on-the-go insights that improve confidence in their clothing choices.



## Privacy & Data Handling

- Uploaded images are processed and deleted immediately after inference.
- No personal data is stored or shared.


## Resources

- Official website: [Shaku.tech](https://shaku.tech)
- GitHub Repository: https://github.com/shakuai/body_measurment
- Documentation: [[API Reference]](https://api.shaku.tech/docs.html)


## License

MIT License © 2025 ShakuAI

