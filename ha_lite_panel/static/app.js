"use strict";

var panel = "home";

function loadPanel() {

    API.get(

        "/api/panel?panel=" + panel,

        function (data) {

            Render.render(data);

        }

    );
}

window.onload = function () {

    Render.init();

    loadPanel();

    setInterval(
        loadPanel,
        5000
    );
};