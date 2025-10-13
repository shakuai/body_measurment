# Shaku - Body Measurement

**AI-powered Human Body Measurement from 2D Images**  

Shaku is designed to revolutionize online fashion and clothing shopping by providing **highly accurate body measurements** using AI. By leveraging front and side images, the service calculates precise dimensions to help users find perfectly fitting clothes, reducing returns and increasing satisfaction.

---

<img src="https://shaku.tech/_next/image?url=%2Fhero%2Fhero-slides%2Fbody-measurement.png&w=640&q=75" width="500" alt="Shaku Intro Section Logo">

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
   
   - **Python**
      ```python
      import requests
      import json
      
      url = "https://api.shaku.tech/oauth/token"
      
      payload = json.dumps({
        "grant_type": "password",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_Secret_Key",
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
    "client_id":"5",
    "client_secret":"NroznofBcPakYEsD2C1yfcPdfRms1rLx59hqrolD",
    "username":"abbas.habibnejad.j@gmail.com",
    "password":"thqNCWFg2CzQjkF"
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

- **SDK Integration**  
  Quickly embed Shaku’s SDK into your site with minimal setup, delivering fast and accurate results out of the box.
  


## Pricing

Shaku offers a cost-effective and scalable solution that provides maximum features for online fashion and apparel businesses. By reducing return rates and improving customer satisfaction, Shaku helps businesses increase revenue and optimize operations. Pricing plans are designed to accommodate small shops to large enterprises, ensuring that every business can benefit from AI-powered body measurement technology. For detailed pricing, subscription plans, and enterprise solutions, visit Shaku Pricing

## Application

Shaku also offers a mobile application that brings AI-powered body measurement tools directly to users’ smartphones. The app allows users to capture their front and side images, receive instant measurements, and track changes over time. This mobile accessibility ensures that users can benefit from accurate body measurements anytime and anywhere, enhancing convenience and engagement. The app can also serve as a complement to your e-commerce platform, providing users with on-the-go insights that improve confidence in their clothing choices.


---

*For more information, visit [Shaku.tech](https://shaku.tech).*
