import {
    ReqPointsArr,
    ReqPoints,
    ManufacturerPoints,
    IManufPoints,
} from "../models/Points/points_models";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { updateTeamPointsObj } from "./teamPointsHelper";
import { setNewPoints } from "./functions";
import handleDriverPoints from "./driverPoints";

//** Handle Manufacturer Points for GTA, TCA */
// is passed the request object and the backend object, updates each class list accordingly and returns the array
const handleManufPoints = (
    manufObj: ReqPointsArr,
    backendManufPoints: IManufPoints,
    round: string,
) => {
    // Loop through keys (class) from the incoming array manufObj
    for (const classification in manufObj) {
        if (classification in backendManufPoints) {
            // Once found, declare variables for each backend and incoming array for the appropriate class
            const dbArr = backendManufPoints[classification];
            const reqArr = manufObj[classification];

            for (const newResult of reqArr) {
                const { Manufacturer, Points } = newResult;
                let found = false;

                for (const dbEntry of dbArr) {
                    if (dbEntry.manufName === Manufacturer) {
                        dbEntry.points[round] = Points;
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    const newManuf: ManufacturerPoints = {
                        manufName: Manufacturer,
                        classification: newResult.Class,
                        points: setNewPoints(round, Points),
                    };

                    dbArr.push(newManuf);
                }
            }
        }
    }
    return backendManufPoints;
};

//** Handle Manufacturer Points for GTWCA, PGT4A */
// Update backend points and return boolean to be handled by result controller
const handleGT3GT4ManufPts = async (
    manufArr: ReqPoints[],
    teamPointsObj: ReqPointsArr,
    driverPointsObj: ReqPointsArr,
    round: string,
    seriesName: string,
): Promise<boolean> => {
    try {
        const series = await SeriesPoints.findOne({ name: seriesName });
        if (series) {
            const { manufPointsList, teamPoints, driversPoints } = series;

            const driverObj = handleDriverPoints(
                driverPointsObj,
                driversPoints,
                round,
            );

            const updated = updateManufListPoints(
                manufArr,
                manufPointsList,
                round,
            );

            const newTeamObj = updateTeamPointsObj(
                teamPointsObj,
                teamPoints,
                round,
            );

            series.teamPoints = newTeamObj;
            series.manufPointsList = updated;
            series.driversPoints = driverObj;

            series.markModified("teamPoints");
            series.markModified("driversPoints");

            await series.save();

            return true;
        }
        return false;
    } catch (error) {
        console.log("Error updateing GT3/GT4 Points", error);
        return false;
    }
};

const updateManufListPoints = (
    manufArr: ReqPoints[],
    backendManufPoints: ManufacturerPoints[],
    round: string,
) => {
    for (const result of manufArr) {
        const { Manufacturer, Points } = result;
        let found = false;

        // If the backend array has entries in it already
        if (backendManufPoints.length !== 0) {
            for (const manuf of backendManufPoints) {
                if (manuf.manufName === Manufacturer) {
                    manuf.points[round] = Points;
                    found = true;
                    break;
                }
            }

            if (!found) {
                const newManuf: ManufacturerPoints = {
                    manufName: Manufacturer,
                    classification: result.Class,
                    points: setNewPoints(round, Points),
                };

                backendManufPoints.push(newManuf);
            }
        } else {
            const newManuf: ManufacturerPoints = {
                manufName: Manufacturer,
                classification: result.Class,
                points: setNewPoints(round, Points),
            };

            backendManufPoints.push(newManuf);
        }
    }
    return backendManufPoints;
};

export { handleGT3GT4ManufPts, handleManufPoints };
