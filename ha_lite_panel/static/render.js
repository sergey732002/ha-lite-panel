"use strict";

var Render = {

    container: null,

    icons: {
        sensor: "🌡",
        binary_sensor: "📟",
        switch: "🔌",
        light: "💡",
        fan: "🌀",
        media_player: "🎵"
    },


    init: function () {

        this.container =
            document.getElementById(
                "panel"
            );

    },


    action: function (
        entity,
        action
    ) {

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
        text,
        entity,
        action
    ) {

        var button =
            document.createElement(
                "button"
            );


        button.innerHTML =
            text;


        button.onclick = function () {

            Render.action(
                entity,
                action
            );

        };


        row.appendChild(
            button
        );

    },


    renderValue: function (
        row,
        item
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
            (item.unit || "");


        row.appendChild(
            value
        );

    },


    renderMediaPlayer: function (
        row,
        item
    ) {

        row.className +=
            " media-player";


        var state =
            document.createElement(
                "div"
            );


        state.className =
            "value";


        state.innerHTML =
            item.state;


        row.appendChild(
            state
        );


        this.addButton(
            row,
            "▶",
            item.entity,
            "play"
        );


        this.addButton(
            row,
            "⏸",
            item.entity,
            "pause"
        );


        this.addButton(
            row,
            "■",
            item.entity,
            "stop"
        );

    },


    render: function (
        items
    ) {

        this.container.innerHTML =
            "";


        for (
            var i = 0;
            i < items.length;
            i++
        ) {


            var item =
                items[i];


            if (!item.visible) {

                continue;

            }


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


            var icon =
                this.icons[item.domain]
                ||
                "⚙";


            title.innerHTML =
                icon +
                " " +
                item.title;


            row.appendChild(
                title
            );



            if (
                item.domain === "sensor" ||
                item.domain === "binary_sensor"
            ) {


                this.renderValue(
                    row,
                    item
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
                item.domain === "media_player"
            ) {


                this.renderMediaPlayer(
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
