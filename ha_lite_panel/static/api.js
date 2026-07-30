"use strict";

var API = {

    get: function (url, callback) {

        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {

            if (xhr.readyState !== 4) {
                return;
            }

            if (xhr.status === 200) {

                callback(
                    JSON.parse(xhr.responseText)
                );
            }
        };

        xhr.open("GET", url, true);
        xhr.send();
    },

    post: function (url, data, callback) {

        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {

            if (xhr.readyState !== 4) {
                return;
            }

            if (callback) {
                callback(xhr.status);
            }
        };

        xhr.open("POST", url, true);

        xhr.setRequestHeader(
            "Content-Type",
            "application/json"
        );

        xhr.send(
            JSON.stringify(data)
        );
    }
};