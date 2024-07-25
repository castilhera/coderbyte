import $ from "jquery";

$.ready(
    function() {
        $("button").on('click', function() {
            let btn = $(this);
            const currentText = btn.text();
            btn.text(currentText === 'ON' ? 'OFF' : 'ON');
        });
    }
);

const rootApp = document.getElementById("root");
rootApp.innerHTML = '<button>ON</button>';
