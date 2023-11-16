# Pyqt5-Leaflet
Use Pyqt5 and Leaflet to embed maps Openstreetmap

In this example, I used the Qt5 graphics library to create a UI in Python. Then, I used the QtWebChannel module, which is a part of the Qt framework that allows exposing C++ objects as remote services usable by web applications. This module provides a solution for bidirectional communication between web applications and Qt-based desktop applications, allowing web applications to access functionalities provided by desktop applications and vice versa.

The QtWebChannel module allows exposing C++ objects as remote services using either the WebSocket or HTTP protocol. To use the QtWebChannel module, you need to create a QWebChannel object in your Qt application and register the C++ objects you want to expose as remote services. In the web application, you can use the QWebChannel.js JavaScript client provided by the QtWebChannel module to access the remote services exposed by the desktop application.

The QtWebChannel module is particularly useful for creating hybrid desktop-web applications that integrate advanced desktop functionalities within a web interface. For example, you can use the QtWebChannel module to expose functionalities such as printing, file generation, and access to hardware devices like cameras and scanners, so they can be used by a web application.

In this way, I am able to intercept in real-time the calls that come from both the map and button click events, and save them in Python variables that I can use for anything.

If you like my code, please subscribe to my Github channel and follow me on my other social channels.

---

![Pyqt5-Leaflet](https://github.com/gerfra/Pyqt5-Leaflet/blob/main/image.png)

---

## Requirements
<li>https://www.qt.io/</li>
<li>https://leafletjs.com/</li>
<li>https://www.python.org/</li>

