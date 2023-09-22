$(document).ready(() => {
    let selectedSeries = null;

    $("#series_button").click((e) => {
        e.preventDefault();
    });

    $(".series-select").click(() => {
        const selected = $(this).text().trim();

        selectedSeries = selected;
        updateSelected();
    });

    const updateSelected = () => {
        if (selectedSeries) {
            $("#selectedSeries").text(`${selectedSeries}`);
        }
    };
});
