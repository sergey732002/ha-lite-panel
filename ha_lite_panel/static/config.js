"use strict";

var container = null;

function addEntity(item) {

    var row = document.createElement("div");

    row.className = "row";

    var title = document.createElement("div");

    title.className = "title";

    title.innerHTML =
        item.name +
        " (" +
        item.entity +
        ")";

    row.appendChild(title);

    var button = document.createElement("button");

    button.innerHTML = "Добавить";

    button.onclick = function () {

        addToPanel(item);
    };

    row.appendChild(button);

    container.appendChild(row);
}

function addToPanel(item) {

    API.post(

        "/api/config",

        item,

        function () {

            alert("Сохранено");
        }
    );
}

window.onload = function () {

    container =
        document.getElementById(
            "entities"
        );

    API.get(

        "/api/entities",

        function (data) {

            container.innerHTML = "";

            for (
                var i = 0;
                i < data.length;
                i++
            ) {

                addEntity(
                    data[i]
                );
            }
        }
    );
};