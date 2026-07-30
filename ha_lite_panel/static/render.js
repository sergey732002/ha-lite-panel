"use strict";

var Render = {

    container: null,

    init: function () {

        this.container =
            document.getElementById(
                "panel"
            );
    },

    render: function (items) {

        this.container.innerHTML = "";

        for (var i = 0; i < items.length; i++) {

            var item = items[i];

            if (!item.visible) {
                continue;
            }

            var row = document.createElement("div");

            row.className = "row";

            var title = document.createElement("div");

            title.className = "title";

            title.innerHTML = item.title;

            row.appendChild(title);

            var value = document.createElement("div");

            value.className = "value";

            value.innerHTML =
                item.state + " " + item.unit;

            row.appendChild(value);

            this.container.appendChild(row);
        }
    }
};