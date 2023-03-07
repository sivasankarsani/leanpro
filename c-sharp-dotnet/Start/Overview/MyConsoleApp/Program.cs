// See https://aka.ms/new-console-template for more information
using System;

Console.WriteLine("Hello, World!");

string userName;

Console.WriteLine("please provide your name here..!!");

userName = Console.ReadLine();
Console.WriteLine($"welcome to the dotnet course: {userName}");
Console.WriteLine("This is the testing the app");

OperatingSystem thisOS = Environment.OSVersion;
Console.WriteLine(thisOS.Platform);
Console.WriteLine(thisOS.VersionString);