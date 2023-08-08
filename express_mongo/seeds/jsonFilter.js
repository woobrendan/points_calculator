const fs = require("fs");

fs.readFile("entries23.json", "utf-8", (err, data) => {
    if (err) {
        console.log("Error reading json entries file", err);
        return;
    }

    const jsonData = JSON.parse(data);

    const filtered = jsonData.filter(
        (obj) => obj.series === "GT World Challenge America",
    );

    fs.writeFile(
        "gtwca_entries.json",
        JSON.stringify(filtered, null, 2),
        (err) => {
            if (err) {
                console.log("Error writing json file");
            }
        },
    );
});
