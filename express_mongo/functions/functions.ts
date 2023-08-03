const getSeriesName = (val: string): string => {
    if (val === "gtwca") return "GT World Challenge America";
    if (val === "pgt4a") return "Pirelli GT4 America";
    if (val === "gta") return "GT America";
    if (val === "tca") return "TC America";
    if (val === "tgr") return "Toyota GR Cup";

    return "";
};

export { getSeriesName };
