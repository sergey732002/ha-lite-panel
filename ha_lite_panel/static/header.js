"use strict";


function updateHeader() {

    var header =
        document.getElementById(
            "header"
        );


    var now = new Date();


    var time =
        now.toLocaleTimeString(
            [],
            {
                hour: "2-digit",
                minute: "2-digit"
            }
        );


    API.get(

        "/api/header",

        function(data) {

            var temp = "";

            if (
                data.temperature !== null &&
                data.temperature !== undefined
            ) {

                temp =
                    "🌡 " +
                    data.temperature.toFixed(1) +
                    "°C";

            }


            header.innerHTML =

                '<div class="header-card">' +

                '<span>🕒 ' +
                time +
                '</span>' +

                '<span>' +
                temp +
                '</span>' +

                '</div>';

        }
    );
}



window.addEventListener(
    "load",
    function() {

        updateHeader();


        setInterval(
            updateHeader,
            5000
        );

    }
);
