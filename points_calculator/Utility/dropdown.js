$(document).ready(() => {
    let selectedSeries = null;

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
