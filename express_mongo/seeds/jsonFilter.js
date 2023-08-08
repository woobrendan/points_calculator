const fs = require("fs");

const series = [
    "GT World Challenge America",
    "GT America",
    "Pirelli GT4 America",
    "TC America",
    "Toyota GR Cup",
];

const seriesShort = ["gtwca", "gta", "pgt4a", "tca", "gr"];

fs.readFile("entries23.json", "utf-8", (err, data) => {
    if (err) {
        console.log("Error reading json entries file", err);
        return;
    }

    const jsonData = JSON.parse(data);

    series.forEach((series, index) => {
        const filtered = jsonData.filter((obj) => obj.series === series);

        const mappedEntries = filtered.map((entry) => {
            const { number, team, series, driver1, driver2, classificaiton } =
                entry;

            return {
                number,
                teamName: team,
                driver1: driver1.teamName,
                ...(driver2 ? { driver2: { ...driver2.name } } : {}),
                classificaiton,
                series,
                events,
            };
        });

        const filename = `${seriesShort[index]}_entries.json`;

        fs.writeFile(
            filename,
            JSON.stringify(mappedEntries, null, 2),
            (err) => {
                if (err) {
                    console.log("Error writing json file");
                }
            },
        );
    });
});
