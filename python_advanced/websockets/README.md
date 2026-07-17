# Real-time communication with WebSockets

------------------------------------------------------------------------

General Requirements

- Environment used for correction:

    - Ubuntu 20.04
    - Python 3.x
- You must use:

    - the websockets library
    - asynchronous programming (async / await)
- Your implementation must:

    - behave exactly as specified
    - handle continuous communication correctly
    - support multiple concurrent connections when required
- Unless explicitly stated, do not:

    - introduce additional frameworks
    - modify the communication protocol
    - add features beyond the requirements

Important Notes
- Communication is persistent: connections remain open and must be handled accordingly
- Multiple clients may interact at the same time
- Message formats must be respected exactly when specified

Final Remarks

This project focuses on building a working real-time communication system.

Accuracy in behavior is essential. Small deviations from the expected behavior may result in failure during evaluation.

------------------------------------------------------------------------

## 0. Server

Introduction

In this step, you will build your first WebSocket server.

Unlike traditional HTTP servers, a WebSocket server maintains a persistent connection with each client. This allows both the client and the server to send messages at any time, enabling real-time communication.

Your goal is to implement a minimal server that accepts connections and echoes back any message it receives.

This behavior establishes the basic communication loop that will be extended in later steps.

Instructions

Implement a WebSocket server that:

- Listens on localhost at port 8765
- Accepts multiple client connections
- Receives text messages from a client
- Sends back the exact same message to the sender (echo behavior)

Expected Behavior

When a client sends:
```
Hello
```
The server must respond:
```
Hello
```
The connection must remain open after the response, allowing continuous communication.

Constraints

- Use the websockets library
- Use asynchronous programming (async / await)
- The server must handle messages continuously (it must not stop after one message)
- Messages must be processed as they arrive (no batching or delays)
- Only text messages need to be supported
- The server must start when executing:
```
python3 echo_server.py
```

Suggested Approach

- Define an asynchronous handler function that receives a connection
- Use a loop to process incoming messages
- Send responses using the same connection
- Start the server using the appropriate websockets utility
- Do not modify messages in this step (output must match input exactly)
- Error handling is not required at this stage

How to Test Manually

websockets provides an interactive client:
```
spam@camelot$ websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
Connection closed: 1000 (OK).
```
Or you can test your server using:

- A Python client using websockets.connect
- A browser-based WebSocket client
- Tools such as websocat, Postman or Insomnia

Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/websockets  
File: echo_server.py  

------------------------------------------------------------------------

## 1. Client

Introduction

In this step, you will implement a WebSocket client.

A WebSocket client connects to a WebSocket server and sends messages through an open connection. Unlike a traditional HTTP request, the connection does not need to be recreated for every message.

Your goal is to create a minimal client that connects to the echo server, sends one message, receives the response, and prints it.

This confirms that your server and client can communicate using the same WebSocket connection.

Instructions

Implement a WebSocket client that:

- Connects to ws://localhost:8765
- Sends the message:

```
Hello WebSocket
```
- Waits for the server response
- Prints the response exactly as received
- Closes the connection after receiving the response

Expected Behavior

If the echo server is running and the client sends:
```
Hello WebSocket
```
The client must print:
```
Hello WebSocket
```
Constraints
- Use the websockets library
- Use asynchronous programming (async / await)
- The client must send only one message
- The client must print only the server response
- The client must not start the server
- The client must run when executing:
```
python3 ws_client.py
```
Suggested Approach
- Create an asynchronous function for the client logic
- Connect to the server using the WebSocket URL
- Send the required message
- Wait for one response
- Print the response
- Let the connection close cleanly after the exchange

Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/websockets  
File: ws_client.py  

------------------------------------------------------------------------

## 2. Validation

Introduction

In this step, you will add basic message validation to your server.

Until now, messages were assumed to be valid. In real systems, this is not a safe assumption. Clients may send empty or invalid data, and the server must handle these cases correctly.

Your goal is to validate incoming messages before processing them.

Instructions

Update your server so that it:

- Receives text messages from connected clients
- Validates each message before responding
- Rejects empty messages
A message is considered invalid when, after removing leading and trailing whitespace, it is empty.

Expected Behavior

If a client sends:
```
Hello
```
The server must respond:
```
OK:Hello
```
If a client sends an empty message or only spaces the server must respond:
```
ERR:EMPTY
```
Constraints

- Use the websockets library
- Use asynchronous programming (async / await)
- Validate each message before responding
- Do not close the connection after an invalid message
- The server must continue handling messages after validation

Suggested Approach

- Receive messages continuously from each client
- Trim whitespace before validation
- Check if the message is empty after trimming
- Send the appropriate response
- Keep the connection open

Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/websockets  
File: validation_server.py  

------------------------------------------------------------------------

## 3. Unicast

Introduction

In this step, you will manage multiple connected clients and control how messages are delivered.

Even when multiple clients are connected, messages must be sent only to the client that initiated the communication. This is known as unicast communication.

Your goal is to ensure that each message is handled independently for each client.

Instructions

Implement a server that:

- Accepts multiple client connections
- Keeps track of connected clients
- Receives messages from any client
- Sends the response only to the sender
- Prefixes responses with:
```
U:
```
Expected Behavior

If a client sends:
```
Hello
```
That client must receive:
```
U:Hello
```
Other clients must not receive the message.

Constraints

- Maintain a collection of active connections
- Add clients on connect and remove on disconnect
- Do not broadcast messages in this step

Suggested Approach
- Store active connections in a shared structure
- Process messages per connection
- Send responses only through the originating connection

Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/websockets  
File: unicast_server.py  

------------------------------------------------------------------------

## 4. Broadcast

Introduction

In this step, you will implement broadcast communication.

Instead of responding only to the sender, the server must distribute messages to all connected clients. This pattern is commonly used in real-time applications such as chat systems.

Instructions

Implement a server that:

- Accepts multiple client connections
- Keeps track of connected clients
- Receives messages from any client
- Sends each message to all connected clients
- Prefixes messages with:
```
B:
```
Expected Behavior

If a client sends:
```
Hello
```
All connected clients must receive:
```
B:Hello
```
Constraints

- Maintain a collection of active connections
- Add clients on connect and remove on disconnect
- Do not send messages to disconnected clients
Suggested Approach
- Store active connections
- Iterate over connections when broadcasting
- Send the message to each active client

Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/websockets  
File: broadcast_server.py  

------------------------------------------------------------------------


## 5. ASGI Integration

Introduction

In this step, you will integrate WebSocket communication into a web-facing Python application.

Until now, your servers have been started using simple helper functions designed for development and experimentation. These approaches are useful for learning, but they are not suitable for real-world applications.

In production environments, applications must:

- Handle different types of traffic (HTTP and WebSocket)
- Support multiple simultaneous users
- Be scalable and maintainable
- Run behind a dedicated application server

To achieve this, Python web applications use standardized interfaces such as WSGI and ASGI.

- WSGI (Web Server Gateway Interface) is designed for traditional synchronous HTTP applications.
- ASGI (Asynchronous Server Gateway Interface) extends this model to support asynchronous communication and long-lived connections such as WebSockets.

ASGI is required in this project because:

- WebSockets rely on persistent connections
- Multiple clients must be handled concurrently
- The application must support both HTTP (for serving pages) and WebSocket communication

While it is possible to implement an ASGI application directly, it would require handling low-level details such as routing, connection management, and protocol handling.

Frameworks like Starlette provide a higher-level abstraction that simplifies this process. They allow you to:

- Define HTTP and WebSocket routes clearly
- Focus on application logic instead of protocol details
- Reduce boilerplate code
- Follow patterns commonly used in real-world applications

Using a framework in this step is intentional: it reflects how production systems are built, where developers rely on well-tested tools to manage infrastructure concerns while focusing on business logic.

In this step, you will build an ASGI application using Starlette, and run it using Uvicorn, a production-ready ASGI server.

This setup reflects how real-world applications are structured and deployed.

Instructions

Implement an application that:

- Serves an HTML page at:
```
http://localhost:8000
```
- Exposes a WebSocket endpoint at:
```
ws://localhost:8000/ws
```
- Accepts WebSocket connections on /ws
- Receives text messages from connected clients
- Sends back the exact same message to the sender (echo behavior)

Expected Behavior

When accessing:
```
http://localhost:8000
```
A web page must be returned.

When connecting to:
```
ws://localhost:8000/ws
```
and sending:
```
Hello
```
The server must respond:
```
Hello
```
Constraints

- Use an ASGI-compatible application
- Use Starlette for routing
- The application must handle both HTTP and WebSocket connections
- The WebSocket endpoint must be /ws
- The WebSocket behavior must follow echo logic
- The application must listen on port 8000

Running the Application

You must run the application using Uvicorn:
```
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```
Explanation of parameters

- asgi_server:app Refers to the Python file and application instance:

- asgi_server → file name (asgi_server.py)

- app → ASGI application object inside the file

- --host 0.0.0.0 Makes the server accessible from outside the local machine (useful for testing and containers)

- --port 8000 Specifies the port where the server will run

- --reload Automatically restarts the server when code changes (development only)

Suggested Approach

- Create a Starlette application

- Define:
    - one HTTP route (/)
    - one WebSocket route (/ws)

- Accept the WebSocket connection before receiving messages

- Use a loop to receive and send messages continuously

- Keep the connection open for multiple exchanges

Example structure:
```
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

async def homepage(request):
    return HTMLResponse("<h1>WebSocket App</h1>")

async def websocket_endpoint(websocket):
    await websocket.accept()
    # message loop here

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
```
Repo:

    GitHub repository: holbertonschool-core-engineering  
    Directory: python_advanced/websockets  
    File: asgi_server.py  

------------------------------------------------------------------------


6. Browser Client
Introduction

In this step, you will build a browser-based client for your WebSocket application.

Until now, you have tested communication using scripts and tools. In real applications, users interact through a web interface that connects to a backend server using WebSockets.

This task is intentionally open-ended. Your goal is to create a simple but functional web client that demonstrates real-time communication using the system you have built.

This step completes the project by producing a working, user-facing application.
Instructions

Create a web client that:

    Connects to your WebSocket endpoint:

ws://localhost:8000/ws

    Allows a user to send messages
    Displays messages received from the server
    Works in real time without reloading the page

You are free to design the interface and structure the code as you prefer, as long as the required behavior is implemented.
Requirements

Your implementation must include:

    An HTML file (index.html)
    A JavaScript file (chat.js)
    A CSS file (style.css)

The client must:

    Establish a WebSocket connection from the browser
    Send messages through that connection
    Receive messages from the server
    Display messages dynamically in the page

Expected Behavior

When the application is running and the page is opened in a browser:

    The interface is displayed correctly
    The client connects to the WebSocket server
    The user can send messages
    Server responses are displayed in the page
    The page does not reload during interaction
    Multiple messages can be exchanged in a single session

Suggested Approach

    Create a simple layout with:
        a text input
        a send button
        a message display area

    Use the browser’s WebSocket API to:
        open a connection
        send messages
        listen for responses

    Update the page dynamically using JavaScript

Example connection:

const socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = (event) => {
    console.log(event.data);
};

How to Test

    Start your ASGI server:

uvicorn asgi_server:app --reload

    Open:

http://localhost:8000

    Interact with your interface and verify that communication works in real time.

Optional Challenges

If you want to extend your implementation, you can try one or more of the following:

    Add a username field and display the sender name with each message

    Show a timestamp for each message

    Keep a chat history during the session (messages remain visible after sending new ones)

    Differentiate visually between:
        sent messages
        received messages

    Add basic styling improvements to make the interface more readable

    Display a message when:
        the connection is established
        the connection is lost

These improvements are optional. They are intended to help you explore how real-time applications are built and improve the user experience.

Repo:

    GitHub repository: holbertonschool-core-engineering
    Directory: python_advanced/websockets
    File: index.html styles.css chat.js
