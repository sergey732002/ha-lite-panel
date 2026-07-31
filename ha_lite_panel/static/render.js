"use strict";

var Render = {

    container: null,

    init: function () {

        this.container =
            document.getElementById(
                "panel"
            );
    },

    action: function (entity, action) {

        API.post(

            "/api/service",

            {
                entity: entity,
                action: action
            },

            function () {

                setTimeout(
                    loadPanel,
                    500
                );
            }
        );
    },

    renderButton: function (row, item) {

        var button =
            document.createElement(
                "button"
            );

        button.innerHTML = "Переключить";

        button.onclick = function () {

            Render.action(
                item.entity,
                "toggle"
            );
        };

        row.appendChild(button);
    },

    renderValue: function (row, item) {

        var value =
            document.createElement(
                "div"
            );

        value.className = "value";

        value.innerHTML =
            item.state +
            " " +
            item.unit;

        row.appendChild(value);
    },

    render: function (items) {

        this.container.innerHTML = "";

        for (var i = 0; i < items.length; i++) {

            var item = items[i];

            if (!item.visible) {
                continue;
            }

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
                item.title;

            row.appendChild(title);

            if (
                item.domain === "light" ||
                item.domain === "switch" ||
                item.domain === "fan"
            ) {

                this.renderButton(
                    row,
                    item
                );

            } else {

                this.renderValue(
                    row,
                    item
                );
            }

            this.container.appendChild(
                row
            );
        }
    }
};
