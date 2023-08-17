# Flutter-App-Control-LED
***I created a Flutter Application that could control WS2812b LED lights using a Raspberry Pi running a Flask web server***

## Frontend ##
**Flutter to create User Interface**</br>
Flutter is an open-source SDK (Software Development Kit) developed by Google for projects.
</br>
I used Flutter in the Dart programming language for this project to create interactive buttons representing different colors.
</br>
</br>
<img src="https://github.com/shaanCh/Flutter-App-Control-LED/assets/69170712/488b94b1-beb8-4bb0-ab17-cf884d51efa9" >

Each button sent an HTTP request to a Python Flask server that was set up locally on a Raspberry Pi.  



```ruby
Future<void> getdata(String endpoint) async{
    var url = 'http://192.168.0.178:80/$endpoint';
    final response = await http.get(Uri.parse(url));

    
    if (response.statusCode == 200) {
      final jsonData = jsonDecode(response.body);
      print('Response: ${jsonData}');
    } else {
      print('Request failed with status: ${response.statusCode}');
    }
  }
```
- Here is the asynchronise function that has a string variable as a parameter.</br>
    - The parameter will be used for each endpoint inside the `url = 'flask_webserver_url'`</br>

In the image above, you can see the **getdata** function call passing in a different color endpoint as a string for the function `ElevatedButton(onPressed: () async{getdata("/Clear");}`


## Backend ##
