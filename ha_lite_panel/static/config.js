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


function moveUp(item) {

    API.post(

        "/api/move_up",

        {
            entity: item.entity
        },

        function () {

            refresh();
        }
    );
}


function moveDown(item) {

    API.post(

        "/api/move_down",

        {
            entity: item.entity
        },

        function () {

            refresh();
        }
    );
}


function renameEntity(item) {

    var title = prompt(

        "Введите новое название",

        item.name

    );

    if (
        title === null ||
        title === ""
    ) {

        return;
    }

    API.post(

        "/api/rename",

        {
            entity: item.entity,
            title: title
        },

        function () {

            refresh();
        }
    );
}


function addToPanel(item) {

    API.post(

        "/api/config",

        item,

        function () {

            refresh();
        }
    );
}


function deleteFromPanel(item) {

    API.post(

        "/api/delete",

        {
            entity: item.entity
        },

        function () {

            refresh();
        }
    );
}


function addButton(
    row,
    text,
    callback
) {

    var button =
        document.createElement(
            "button"
        );

    button.innerHTML =
        text;

    button.onclick =
        callback;

    row.appendChild(
        button
    );
}


function addEntity(item) {

    var row =
        document.createElement(
            "div"
        );

    row.className =
        "row";

    var title =
        document.createElement(
            "div"
        );

    title.className =
        "title";

    title.innerHTML =

        item.name +

        " (" +

        item.entity +

        ")";

    row.appendChild(
        title
    );

    if (item.added) {

        addButton(
            row,
            "▲",
            function () {

                moveUp(item);
            }
        );

        addButton(
            row,
            "▼",
            function () {

                moveDown(item);
            }
        );

        addButton(
            row,
            "✎",
            function () {

                renameEntity(item);
            }
        );

        addButton(
            row,
            "✖",
            function () {

                deleteFromPanel(item);
            }
        );
    }
    else {

        addButton(
            row,
            "Добавить",
            function () {

                addToPanel(item);
            }
        );
    }

    container.appendChild(
        row
    );
}


window.onload = function () {

    container =

        document.getElementById(
            "entities"
        );

    refresh();
};
