![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)

# README 0x11: What Happens When You Type "google.com" in Your Browser and Press Enter

This README provides an overview of the typical process that occurs when you type "google.com" in your browser and press Enter. The details may vary slightly depending on the specific browser and network configurations, but the general steps remain consistent.

## 1. DNS Resolution
    The first step is to resolve the domain name "google.com" to its corresponding IP address using the Domain Name System (DNS). The DNS server associated with your network is queried to obtain the IP address of "google.com".

## 2. Initiating a TCP Connection
    Once the IP address is obtained, the browser initiates a Transmission Control Protocol (TCP) connection with the server at that IP address. TCP is a reliable protocol that ensures the reliable delivery of data packets.

## 3. HTTP Request
   After establishing a TCP connection, the browser sends an HTTP (Hypertext Transfer Protocol) request to the server associated with the IP address for the specific webpage "google.com". The request includes information such as the HTTP method (typically GET for webpage retrieval) and any additional headers.

## 4. Server Processing
    The server processes the HTTP request, fetches the requested webpage (in this case, the Google homepage), and generates an HTTP response.

## 5. HTTP Response
    The server sends the HTTP response, which contains the requested webpage's HTML, along with any other resources like CSS, JavaScript, images, etc., to the browser.

## 6. Rendering the Webpage
    The browser receives the HTML and other resources, processes the HTML to construct the Document Object Model (DOM) tree, and then renders the webpage on the screen based on the DOM tree and associated resources.

## 7. JavaScript Execution
    If the webpage includes JavaScript, the browser executes the JavaScript code, which may modify the DOM, make additional requests for data, and enhance the webpage's interactivity and functionality.

## 8. Displaying the Webpage
    The final step involves displaying the fully rendered webpage, complete with text, images, styling, and interactivity, to the user on the browser.

This README provides a high-level overview of the steps involved in loading a webpage when typing "google.com" in your browser. The actual process may involve additional optimizations, caching, and security measures based on browser configurations and website settings.
