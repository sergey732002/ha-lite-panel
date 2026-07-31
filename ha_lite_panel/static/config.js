"use strict";

var container = null;


function refresh() {

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
}


function addEntity(item) {

    var row =
        document.createElement(
            "div"
        );

    row.className = "row";

    var title =
        document.createElement(
            "div"
        );

    title.className = "title";

    title.innerHTML =

        item.name +

        " (" +

        item.entity +

        ")";

    row.appendChild(
        title
    );

    var addButton =
        document.createElement(
            "button"
        );

    addButton.innerHTML =
        "Добавить";

    addButton.onclick = function () {

        addToPanel(item);
    };

    row.appendChild(
        addButton
    );

    var deleteButton =
        document.createElement(
            "button"
        );

    deleteButton.innerHTML =
        "Удалить";

    deleteButton.onclick = function () {

        deleteFromPanel(item);
    };

    row.appendChild(
        deleteButton
    );

    container.appendChild(
        row
    );
}


function addToPanel(item) {

    API.post(

        "/api/config",

        item,

        function () {

            alert(
                "Сохранено"
            );
        }
    );
}


function deleteFromPanel(item) {

    API.post(

        "/api/delete",

        {

            entity:
                item.entity

        },

        function () {

            alert(
                "Удалено"
            );
        }
    );
}


window.onload = function () {

    container =

        document.getElementById(
            "entities"
        );

    refresh();
};
