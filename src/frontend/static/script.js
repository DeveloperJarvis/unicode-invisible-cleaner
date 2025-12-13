document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('processBtn').addEventListener('click', function () {
        const text = document.getElementById('inputText').value;

        console.log("Here")
        console.log(encodeURIComponent(text).length)
        console.log(encodeURIComponent(text));

        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "text=" + encodeURIComponent(text)
        })
            .then(response => {
                console.log("Response status:", response.status);
                return response.json()
            })
            .then(data => {
                console.log("Data type: ", typeof (data));
                console.log("Data received: ", data);
                console.log("Data length (if applicable): ", Object.keys(data).length);

                if (data.highlighted && data.cleaned) {
                    document.getElementById("detectedText").innerHTML = data.highlighted;
                    document.getElementById("cleanedText").innerHTML = data.cleaned;
                }
                else {
                    console.error("Response data does not contain expected values: ", data)
                }
            })
            .catch(error => {
                console.log("Response: ", response);
                console.error('Error: ', error);
            });

    });

});
