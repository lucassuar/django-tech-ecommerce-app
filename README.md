[![Build Status](https://travis-ci.org/lucassuar/django-tech-ecommerce-app.svg?branch=master)](https://travis-ci.org/lucassuar/django-tech-ecommerce-app)

<h6>Lucas Suarez</h6>

<h1> Full Stack Framework Milestone </h1>

<a href="https://django-tech-ecommerce-app.herokuapp.com" target="_blank"> Click here to view website</a>


## Purpose

<p>
    The purpose of this project is to create a website for a startup called B&O. B&O is a company that sells innovative products based on users opinions..
    The objective of B&O website is to let users drive and be involved in the companys innovation process of new products. It allows users not onlye to buy new products
    but also to share their product ideas so the community can vote and the company can then choose what products they will sell or not.
    A key prt of the business model of the company is to sell prodcuts through their ecommerce funcionality. Users can register/login to thei online shop
    and purchase the latest innovations produced.
</p>


## UX
This platform hass been built to be fully responsive so it works perfectly on any device and screen size.

Some of the initial Wireframes for both descktop and mobile versions can be found here: [UI Mockup Images](https://github.com/lucassuar/django-tech-ecommerce-app/tree/master/media/ui%20mockups)


### User stories
Below are some of the potential stories that users can follow:

- A new user should be able to:
    - Visualize a homepage with all products and blog entries.
    - Visualize the main navigation (sticky) with links to the main sections.
    - Visualize a search bar for finding products.
    - User always have the option to go to any page thanks to a sticky navbar with all pages accesible from there.

- If I user want to purchase a product they should be able to:
    - Visualize all products in one page
    - Register a new account or login to existing one
    - See the account profile.
    - Search individual products from anywhere trough the searchbar on the navbar.
    - Add to cart.
    - Visualise a list of the final order and change that order (remove or edit)
    - Add contact details and payment option
    - Pay

- When a user would like to add a new suggestion, they should be able to:
    - Access a complete list of suggestions
    - Add a new suggestion (no account needed as we want to promote as many interactions as possible)
    - See personal suggestion


## Quick Tutorial
<p>If you would like to buy:</p>
<ol>
    <li>First, register an account or login (if you already have one). This can be achieved by clicking on one of the login or register buttons on the navbar.</li>
    <li>Then users will be able to purchase any of the products and as many as they wish. They will only have to add to cart the items and go to their cart page when they are ready to continue.</li>
    <li>From the cart page they will be able to see a breackdown of their prodcuts and modify it if needed.</li>
    <li>Then they will be able to follow the checkout process and pay with stripe. Below you can see a card example you can follow to finilise the purchase</li>
        <table>
            <tr>
                <th>Card number</th>
                <th>CVV</th>
                <th>Date</th>
            </tr>
            <tr>
                <td>4242 4242 4242 4242</td>
                <td>111</td>
                <td>08/24 (or any valid credit card date)</td>
            </tr>
        </table>
</ol>   

<p>If you would like to send a suggestion:<p>
<ol>
    <li>Just go to the suggestion page and see all open sugestions.</li>
    <li>If your idea is not available you can press the button add sugestion and add the information you wish to send.</li>
    <li>Then your product sugestion will be available for the community to vote.</li>
    <li>If your ideas get enough votes and its viable to produce, B&O will produce that product and place for sale until performance its assesed.</li>
</ol>   


## Features overview

<p>B&O platfom has variety of functionalities/features to let users achieve diferent goals. See below some of the main functionalities:<p>

- See all products
- See each product
- Add to cart from products page, homepage or specific product page
- See order list and modify order from the cart page.
- Checkout form to add customer details and credit card details
- Purchase
- Search products by keyword
- Add a product suggestion
- Blog entries page
- Single blog page
- Fully responsive

### Features I'd like to implement in future versions
- Comments on suggestion ideas
- Edit own ideas
- Share social media
- Similar products section on product page


## Technologies
<p>This website its Djago platform that uses bootsrap for the interface. See below some of the key technologies used;</p>

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is an open source framework for developing with HTML, CSS, and JS.
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript) - to activate bootstrap elements and for DOM manipulation.
- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
- [Github](https://github.com/) - Github is one of the platforms used to push all the savings on the code.
- [Heroku](https://www.heroku.com/) - Platform used to import the entirely platfom into the cloud.

## Databse schema:

Data e-commerce example:
<img width="928" alt="database products" src="https://user-images.githubusercontent.com/47657461/57696729-5dce4480-7649-11e9-917c-d4a42959f419.png">

Data Blog Post:

Id | When is Created | Id Name | Text | Tag | Image | 
--- | --- | --- | --- | --- | --- | 
1 | Date | Title| Blog Post content | Category type | image|

Data Suggestions:

Id | When is Created | Id Name | Text |
--- | --- | --- | --- | 
1 | Date | Suggestion title| Suggestion content |

## Testing
<p>
This project has been tested in many different ways: . 
    - I used chrome developer tools to check for errors, responisvenes and test if something was wrong with my html, css or javascript files. 
    - I used Django error page that appeared when my code had any errors, I also use print command at time with specific messages to understand if, for example, data was been aplied.
    - As well, I used Django built-in test funcionality to create automated, custom test. This had allow me to create multiple tests for my views, models, forms...
    - I also usedd Travis CI by connecting it trough my github repo. 
    - Finally I went through lots of manual tests to understand and make sure the funcionality of the website was on point.
Below you see some of the tests performed:

#### Django Built-in tests

<table>
    <tr>
        <th>PRODUCTS APP</th>
        <th>CHECKOUT APP</th>
        <th>ACCOUNTS APP</th>
    </tr>
    <tr>
        <td>1 Test</td>
        <td>5 Test</td>
        <td>3 Test</td>
    </tr>
</table>

#### Some of Manual Tests done

<table>
    <tr>
        <th>Manual Test</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Clicking on logo icon in navigation takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Clicking on logo icon in navigation takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The platform has been tested on all modern desktop and mobile browsers to ensure cross compatibility and functionalities.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The platform has been tested to be fully responsive and that is correctly displayed across all of type devices.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The platform has been tested to ensure that all of the user stories were functional without errors.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The platform has been tested to make sure all urls work properly</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The platform has been tested to ensure all text-area and inputs are perfectly funcioning and sending/reciving corrct data.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>All links and buttons tested to make sure they all works as they should.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The user can come back to the previous window from everywhere, no rabbit holes. </td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Data from database is been accesible at all times.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Purchase process until the purchase its done works perfectly.</td>
        <td>Successful</td>
    </tr>
</table>


## Deployment
<p>
    I created a git hub repostory first and conncted to a heroku app and then pushed the entire website code to it. 
    To ensure this worked and based on Heroku documentation I had to create a procfile and a requirements.txt file. This allowed heroku to install the correct packages and run my project accordingly. I also had to install the whitenoise package so heroku could find
    my static files. To also get my models working I had to migrate my database from sqlite to herokus postgres database.
    
    The app is hosted on Heroku. The code uses the default GitHub master branch. This wproject has been deployed to heroku via Github so the code in both GitHub and Heroku are the same. 
    Both platforms have been connected too, therefor changes made to the master branch on GitHub are automatically pushed to Heroku. The only data used in Heroku not 
    visible on GitHub are the secret config variables detailed in the contributing section of this readme, and the static and media files
    hosted on Amazon S3.
</p>


## References/Acknowledgements:
- Products and design inspiration: https://www.bang-olufsen.com/
- Checout page structure from: https://getbootstrap.com/docs/4.0/examples/checkout/
- Some code logic has been used from video tutorialS and modified acordignly to suit this specific project.



#### Licence
Copyright (c) 2019 Lucas Suarez