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

    addButton: function (
        row,
        title,
        entity,
        action
    ) {

        var button =
            document.createElement(
                "button"
            );

        button.innerHTML = title;

        button.onclick = function () {

            Render.action(
                entity,
                action
            );
        };

        row.appendChild(button);
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
                item.domain === "sensor" ||
                item.domain === "binary_sensor"
            ) {

                var value =
                    document.createElement(
                        "div"
                    );

                value.className =
                    "value";

                value.innerHTML =
                    item.state +
                    " " +
                    item.unit;

                row.appendChild(
                    value
                );
            }

            if (
                item.domain === "switch" ||
                item.domain === "light" ||
                item.domain === "fan"
            ) {

                this.addButton(
                    row,
                    item.state,
                    item.entity,
                    "toggle"
                );
            }

            if (
                item.domain === "cover"
            ) {

                this.addButton(
                    row,
                    "▲",
                    item.entity,
                    "open"
                );

                this.addButton(
                    row,
                    "■",
                    item.entity,
                    "stop"
                );

                this.addButton(
                    row,
                    "▼",
                    item.entity,
                    "close"
                );
            }

            if (
                item.domain === "climate"
            ) {

                var climate =
                    document.createElement(
                        "div"
                    );

                climate.className =
                    "value";

                climate.innerHTML =
                    item.state;

                row.appendChild(
                    climate
                );
            }

            this.container.appendChild(
                row
            );
        }
    }
};
