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
Using almost the same Python code from my other repository --> [Controlling-LEDs-RaspberryPi-Webserver](https://github.com/shaanCh/Controlling-LEDs-RaspberryPi-Webserver/tree/main) </br>

The AppControl.py script runs a basic Flask API that established different endpoints for different functions. When there is a request sent to that endpoint the function thats defined underneath it will be called and ran. 
</br>
For example:
```ruby
@app.route("/Red", methods=["GET"])
def red():
	ledcolor(strip, Color(255,0,0))
	return {'message': 'SUCCESS'}
```
The endpoint defined in this example is "/Red" which runs a function defined earlier specifically for controlling the LED lights --> `ledcolor(strip, Color(255, 0, 0))`</br>

All other functions and variables defines are solely for LED light functionality please feel free to check out my other repository for how the code can control LED lights --> [Controlling-LEDs-RaspberryPi-Webserver](https://github.com/shaanCh/Controlling-LEDs-RaspberryPi-Webserver/tree/main) </br>

To make the webserver permanent on my Raspberry Pi I used the nohup command `sudo nohup python3 AppControl.py 2>&1 &`
This will:
- Keep the server running in the background
- Can use Pi terminal and other utilities without interruption
- Output any sort of code or message to the **nohup.out** file which you can easily `sudo cat nohup` into
- Check if the server is still running with `ps -ef |grep nohup`
- kill the session/server with ID from the above command `kill 13113`

## Overall ##
Now I can control the led lights from the comfort of my bed!

https://github.com/shaanCh/Flutter-App-Control-LED/assets/69170712/e2055555-6d5e-4369-ae24-451cd85f963e

More Pictures:
</br>
<center><img src='https://github.com/shaanCh/Flutter-App-Control-LED/assets/69170712/4e0c6f37-42e3-4c6e-b9bf-657c50810725' width=50% height=50%></center>

<center><img src='https://github.com/shaanCh/Flutter-App-Control-LED/assets/69170712/60ff9250-9181-4ab9-9a9f-5a00a5ffedb1' width=50% height=50%></center>
</br>
There is a lot that I left out so feel free to message me
</br>

Here are some other things involved in this project:
- Setting Up Android Studio
- Syncing Vscode and Android Studio
- Setting up an emulator for a phone of your choice
- Setting Static IP on Raspberry PI
- Learned tmux on Raspberry Pi to organize terminals and run multiple terminals at the same time (Very useful for testing API/Server with different code)
- Learning how to build an APK
- Deploying the APK on a device so that your phone can actually use the app you build instead of using an emulator



