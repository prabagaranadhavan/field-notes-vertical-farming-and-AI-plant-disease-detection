const form =
    document.getElementById("uploadForm");

if (form) {

    form.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();

            const imageInput =
                document.getElementById("imageInput");

            const loading =
                document.getElementById("loading");

            const result =
                document.getElementById("result");

            const prediction =
                document.getElementById("prediction");

            const confidence =
                document.getElementById("confidence");

            const error =
                document.getElementById("error");


            if (!imageInput.files.length) {

                error.textContent =
                    "Please select an image.";

                return;
            }


            const formData =
                new FormData();

            formData.append(
                "image",
                imageInput.files[0]
            );


            loading.style.display =
                "block";

            result.style.display =
                "none";

            error.textContent =
                "";


            try {

                const response =
                    await fetch(
                        "/predict",
                        {
                            method: "POST",
                            body: formData
                        }
                    );


                const data =
                    await response.json();


                loading.style.display =
                    "none";


                if (!response.ok) {

                    error.textContent =
                        data.error ||
                        "Prediction failed.";

                    return;
                }


                prediction.textContent =
                    data.prediction;


                confidence.textContent =
                    data.confidence + "%";


                result.style.display =
                    "block";

            }

            catch (errorObject) {

                loading.style.display =
                    "none";

                error.textContent =
                    "Could not connect to the server.";

                console.error(
                    errorObject
                );

            }

        }
    );

}