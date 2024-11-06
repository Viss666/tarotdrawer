console.log("Hello, world.");

var askButton = document.querySelector("#ask-button");
console.log("ask", askButton);
//target, event (not camel cased for some reason)

//the ask button, most all the code
askButton.onclick = function () {
    console.log("ask button was clicked");


    //grabs the first instance of the selected in the query, important, usually always precedes JS
    var h1 = document.querySelector("h1");
    console.log("h1 element", h1);

    //hide banner tarot deck image
    var firstImage = document.querySelector("#first-image");
    firstImage.src = "";

    //generate a random number based on card size, floor it
    var randomCard = tarotCards[Math.floor(Math.random() * tarotCards.length)];
    console.log(randomCard);

    //display random drawn card
    var currentImage = document.querySelector("#current-image");
    currentImage.src = randomCard["imagePath"];

    //user input
    var questionInput = document.querySelector("#input-question");
    console.log("user typed",questionInput.value);

    //prepare data to be sent to server
    var data = "question=" + encodeURIComponent(questionInput.value);
    data += "&card=" + encodeURIComponent(randomCard["tarotName"]);
    data += "&description=" + encodeURIComponent(randomCard["tarotDescription"]);
    data += "&image=" + encodeURIComponent(randomCard["imagePath"]);
    data += "&rating=" + encodeURIComponent(0);
    console.log("data to be sent to the server:", data);

    //send new restaurant values to the server API:
    fetch("http://localhost:8080/previous_readings", {
        // IMPORTANTT !!!! 
        credentials: "include",
        method: "POST",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(function (response) {
        console.log("previous reading created!");
        loadReadingsFromServer();
    });




    
    //display users question
    var currentQuestion = document.querySelector("#current-question");
    currentQuestion.innerHTML = questionInput.value;

    //display current tarot description
    var currentReading = document.querySelector("#current-reading");
    currentReading.innerHTML = randomCard["tarotDescription"]

    //previous readings section underneath
    var previousReadings = document.querySelector("#previous-readings");
    console.log("Previous readings selected");
    previousReadings.innerHTML = "Previous Readings:";

    var questions = document.querySelector("#questions");

    var previousQuestion = document.createElement("li");
    previousQuestion.innerHTML = randomCard["tarotName"] + " - " + questionInput.value;
    //var child = previousQuestion, " - ", currentQuestion.value;
    questions.appendChild(previousQuestion);


    //added card flip audio
    var cardFlip = new Audio("cardflip.mp3");
    cardFlip.play()

};


var loginButton = document.querySelector("#login-button");

loginButton.onclick = function () {
    console.log("Login button was clicked");

    var loginDiv = document.querySelector("#login-div");
    //registrationList = document.createElement("li");

    loginButton.style.display = "none";

    var emailInput = document.createElement("input");
    emailInput.placeholder = "email";
    loginDiv.appendChild(emailInput);
    var passwordInput = document.createElement("input");
    passwordInput.placeholder = "password";
    passwordInput.type = "password";
    loginDiv.appendChild(passwordInput);
    var submitButton = document.createElement("button");
    submitButton.innerHTML = "Submit";
    loginDiv.appendChild(submitButton);

    var cancelButton = document.createElement("button");
    cancelButton.innerHTML = "Cancel";
    loginDiv.appendChild(cancelButton);
    // var data = "email=" + encodeURIComponent(emailInput.value);
    // data += "&password=" + encodeURIComponent(passwordInput.value);

    //console.log(data)


    submitButton.onclick = function () {
        if ((emailInput.value == null || emailInput.value == "") || (passwordInput.value == null || passwordInput.value == "")) {
            alert("Please fill in all required fields");
            return
          } else {
            var data = "email=" + encodeURIComponent(emailInput.value);
            data += "&password=" + encodeURIComponent(passwordInput.value); 
            console.log(data)       
        fetch("http://localhost:8080/sessions", {
            credentials: "include",
            method: "POST",
            body: data,
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }).then(function (response) {
            if (response.status == 401) {
                alert("Error logging in.");
                console.log("failed to log in");
                return 
            } else {
                
            console.log("logged in!");
            loadReadingsFromServer();
            loginDiv.removeChild(emailInput);
            loginDiv.removeChild(passwordInput);
            loginDiv.removeChild(submitButton);
            loginDiv.removeChild(cancelButton);
            }

          });
        }
            
        }
    

    
    cancelButton.onclick = function () {
        loginDiv.removeChild(emailInput);
        loginDiv.removeChild(passwordInput);
        loginDiv.removeChild(submitButton);
        loginDiv.removeChild(cancelButton);  
        
        loginButton.style.display = "inline-block";
    }


    

}












var regButton = document.querySelector("#reg-button");

regButton.onclick = function () {
    console.log("Registration button was clicked");

    var registrationDiv = document.querySelector("#registration-div");
    //registrationList = document.createElement("li");

    regButton.style.display = "none";

    var firstnameInput = document.createElement("input");
    firstnameInput.placeholder = "first name";
    registrationDiv.appendChild(firstnameInput);

    var lastnameInput = document.createElement("input");
    lastnameInput.placeholder = "last name";
    registrationDiv.appendChild(lastnameInput);

    var emailInput = document.createElement("input");
    emailInput.placeholder = "email";
    registrationDiv.appendChild(emailInput);

    var passwordInput = document.createElement("input");
    passwordInput.type = "password";
    passwordInput.placeholder = "password";
    registrationDiv.appendChild(passwordInput);

    var submitButton = document.createElement("button");
    submitButton.innerHTML = "Submit";
    registrationDiv.appendChild(submitButton);

    var cancelButton = document.createElement("button");
    cancelButton.innerHTML = "Cancel";
    registrationDiv.appendChild(cancelButton);


    submitButton.onclick = function () {
        if (window.confirm("Are you sure you want to create this user?")){
            var data = "firstname=" + encodeURIComponent(firstnameInput.value);
            data += "&lastname=" + encodeURIComponent(lastnameInput.value);
            data += "&email=" + encodeURIComponent(emailInput.value);
            data += "&password=" + encodeURIComponent(passwordInput.value);

            fetch("http://localhost:8080/users", {
                credentials: "include",
                method: "POST",
                body: data,
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            }).then(function (response) {
                if (response.status == 422) {
                    alert("Error processing request.")
                    return
                }
                console.log("user created!");
                registrationDiv.removeChild(firstnameInput);
                registrationDiv.removeChild(lastnameInput);
                registrationDiv.removeChild(emailInput);
                registrationDiv.removeChild(passwordInput);
                registrationDiv.removeChild(submitButton);
                registrationDiv.removeChild(cancelButton);
                var thankYou = document.createElement("p");
                thankYou.innerHTML = "Thank you for creating a user! now please sign in."
                registrationDiv.appendChild(thankYou);
        
            
        
    
            });
            
        }
    }

    
    cancelButton.onclick = function () {
        registrationDiv.removeChild(firstnameInput);
        registrationDiv.removeChild(lastnameInput);
        registrationDiv.removeChild(emailInput);
        registrationDiv.removeChild(passwordInput);
        registrationDiv.removeChild(submitButton);
        registrationDiv.removeChild(cancelButton);   

        regButton.style.display = "inline-block";
    }


    

}


var tarotCards = [];
var previousSessionReadings = [];

//fetch("https://api.jsonbin.io/v3/b/64efadcc9d312622a398a63a").then(function (response) {
fetch("http://localhost:8080/cards",{
    credentials: "include",
    }).then(function (response) {
    // IMPORTANT !!!! 

    console.log("card response received");
    response.json().then(function (data) {
        console.log("response data received:", data);
    
        tarotCards = data;

        //tarotCards.append(data.record)

    //for card in tarotCards
    //tarotCards.forEach(function (card){
        //THIS NEXT PIECE OF CODE MIGHT NOT WORK
        //previousQuestion.innerHTML = card;
        //var child = previousQuestion, " - ", currentQuestion.value;
        // IN THE BUTTON, CONFIGURE THE DATA, CHANGE THINGS
        // data += for extra items, 
    //})

    });

});


// fetch("http://localhost:8080/previous_readings").then(function (response) {
//     console.log("previous readings received");
//     response.json(),then(function (data) {
//         console.log("response data received:", data);
//     }

//     previousReadings.forEach(function (reading){
//         // var child = previousQuestion, " - ", currentQuestion.value; 
//         var child = reading + " - " + reading.value;

var hiddenbody = document.getElementById("hidden-body");
var hiddenbuttons = document.getElementById("hidden-buttons");

function loadReadingsFromServer() {
    fetch("http://localhost:8080/previous_readings",{
    credentials: "include"}) 
    .then(function (response) {
        if (response.status== 401){
            console.log("not logged in")
            hiddenbody.style.display = "none";
            hiddenbuttons.style.display = "block";
            return
            
        }
        else if (response.status == 200){
            hiddenbuttons.style.display = "none";
            hiddenbody.style.display = "block";
        }
        console.log("readings were received");
        response.json().then(function (data) {
            console.log("response data received:", data);

            previousSessionReadings = data;

            
            var previousReadings = document.querySelector("#questions");
            previousReadings.innerHTML = ""
            previousSessionReadings.forEach(function (reading){
                //var child = reading.question + " - " + reading.card;
                var newListItem = document.createElement("li");
                //newListItem.innerHTML = child;


                var containerdiv = document.createElement("div");



                //var titleDiv = document.createElement("div");
                var titleDiv = document.createElement("h3");
                titleDiv.innerHTML = reading.question;
                //titleDiv.innerHTML = title;
                titleDiv.classList.add("cardTitle");
                newListItem.appendChild(titleDiv);

                var question = document.createElement("h4");
                question.innerHTML = reading.card;
                question.classList.add("pastQuestion");
                newListItem.appendChild(question)

                var readingDiv = document.createElement("div");
                readingDiv.innerHTML = reading.description;
                readingDiv.classList.add("reading");
                newListItem.appendChild(readingDiv);


                

                var readingImage = document.createElement("img");
                readingImage.src = reading.image;
                readingImage.classList.add("readingImage");
                newListItem.appendChild(readingImage);

                var rating = document.createElement("h5");
                rating.innerHTML = "Tarot Reading Rating:  " + reading.rating;
                rating.classList.add("pastRating");
                newListItem.appendChild(rating);



                var deleteButton = document.createElement("button");
                deleteButton.classList.add("deleteButton");
                deleteButton.innerHTML = "Delete";
                newListItem.appendChild(deleteButton)
                deleteButton.onclick = function () {
                    if (window.confirm("Are you sure you want to delete this reading?")){
                        console.log("delete me", reading.id);
                        deleteReadingFromServer(reading.id);
                    }

                };
                var editButton = document.createElement("button")
                editButton.innerHTML = "Edit"
                editButton.classList.add("editButton");
                newListItem.appendChild(editButton)
                editButton.onclick = function () {
                    var editQuestionDiv = document.createElement("input");
                    editQuestionDiv.value = reading.question;
                    newListItem.appendChild(editQuestionDiv);
                    var editRatingDiv = document.createElement("input");
                    editRatingDiv.value = reading.rating;
                    newListItem.appendChild(editRatingDiv);
                    var submitButtonDiv = document.createElement("button");
                    submitButtonDiv.innerHTML = "Submit changes";
                    newListItem.appendChild(submitButtonDiv);
                    


                    submitButtonDiv.onclick = function () {
                        editReadingFromServer(reading.id,editQuestionDiv.value,editRatingDiv.value)
                    }
                    console.log("edit me",reading.id);
                    //editReadingFromServer(reading.id) 
                }


                previousReadings.appendChild(newListItem);


            });
        });
    });
};
loadReadingsFromServer();

function deleteReadingFromServer(reading_id) {
    fetch("http://localhost:8080/previous_readings/" + reading_id, {
        credentials: "include",
        method: "DELETE"
    }).then(function (response) {
        console.log("previous readings created!");
        loadReadingsFromServer();
    });
}

function editReadingFromServer(reading_id,question,rating) {
    var data = "question=" + encodeURIComponent(question)
    data += "&rating=" + encodeURIComponent(rating)
    fetch("http://localhost:8080/previous_readings/" + reading_id, {
        credentials: "include",
        method: "PUT",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(function (response) {
        loadReadingsFromServer();
    });
}




// function updateReadingFromServer(reading_id, data) {
//     fetch("http://localhost:8080/previous_readings/" + reading_id, {
//         method: "PUT",
//         body: 
//     })
// }

// fetch("http://localhost:8080/previous_readings", {
//     method: "POST",
//     body: data,
//     headers: {
//         "Content-Type": "application/x-www-form-urlencoded"
//     }
// }).then(function (response) {
//     console.log("previous reading created!");
//     loadReadingsFromServer();
// });



