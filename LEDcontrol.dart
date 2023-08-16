import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.black,
        useMaterial3: true,
      ),
      home: const ColorButtons(),
    );
  }
}

class ColorButtons extends StatelessWidget {
  const ColorButtons({super.key});

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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Transform.translate(offset: const Offset(0,10), child: const Text("Choose a Color", style: TextStyle(color: Colors.white, fontStyle: FontStyle.italic, fontSize: 50, fontWeight: FontWeight.bold),)),
        backgroundColor: Colors.black38,
        centerTitle: true,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: 
            [ElevatedButton(onPressed: () async{getdata("/Clear");}, child: const Text("Clear", style: TextStyle(fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Red");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.red)), child: const Text("RED", style: TextStyle(color: Colors.white, fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Orange");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.orange)), child: const Text("ORANGE", style: TextStyle(color: Colors.white, fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Yellow");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.yellow)), child: const Text("YELLOW", style: TextStyle(color: Colors.white, fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Green");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.green)), child: const Text("GREEN", style: TextStyle(color: Colors.white, fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Blue");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.blue)), child: const Text("BLUE", style: TextStyle(color: Colors.white, fontSize: 25),)),
             ElevatedButton(onPressed: ()async{getdata("/Violet");}, style: const ButtonStyle(backgroundColor: MaterialStatePropertyAll(Colors.purple)), child: const Text("VIOLET", style: TextStyle(color: Colors.white, fontSize: 25),)),
             Row(
              mainAxisAlignment: MainAxisAlignment.center,
               children: [
                 ElevatedButton(onPressed: () async{getdata("/Start");}, child: const Text("Start", style: TextStyle(fontSize: 25),)),
                 ElevatedButton(onPressed: () async{getdata("/Stop");}, child: const Text("Stop", style: TextStyle(fontSize: 25),)),
               ],
             )]),
        ),
      ),
    );
  }
}