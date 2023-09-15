import { PointsInterface, Series } from "../models/Points/points_models";

const getSeriesName = (val: string): string => {
    const series: { [key: string]: string } = {
        gtwca: "GT World Challenge America",
        pgt4a: "Pirelli GT4 America",
        gta: "GT America",
        tca: "TC America",
        tgr: "Toyota GR Cup",
    };

    return series[val];
};

const setNewPoints = (round: string, points: number) => {
    const pts: PointsInterface = {
        R1: null,
        R2: null,
        R3: null,
        R4: null,
        R5: null,
        R6: null,
        R7: null,
        R8: null,
        R9: null,
        R10: null,
        R11: null,
        R12: null,
        R13: null,
        R14: null,
        R15: null,
        R16: null,
        R17: null,
        R18: null,
    };

    for (const roundNum in pts) {
        if (roundNum === round) {
            pts[roundNum] = points;
        }
    }

    return pts;
};

const filterSeriesByPoints = (data: Series[], pointsType: string) => {
    const filtered = data.map((series: any) => {
        const keys = getPointsKeys(pointsType, series.name);

        const cleanSeriesObj: any = {};

        keys.forEach((key) => {
            cleanSeriesObj[key] = series[key];
        });

        return cleanSeriesObj;
    });

    return filtered;
};

const getPointsKeys = (pointsType: string, series: string): string[] => {
    const keys = ["name"];

    if (pointsType !== "manuf") {
        keys.push(pointsType);
    }

    if (pointsType === "manuf") {
        const gt3Gt4 = series === gtwca || series === pgt4a ? true : false;

        gt3Gt4 ? keys.push("manufPointsList") : keys.push("manufPoints");
    }

    return keys;
};

const gtwca = "GT World Challenge America";
const pgt4a = "Pirelli GT4 America";

export { getSeriesName, setNewPoints, filterSeriesByPoints };
