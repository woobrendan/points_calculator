import {
    ReqPointsArr,
    ReqPoints,
    ManufacturerPoints,
    IManufPoints,
} from "../models/Points/points_models";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { setNewTeamPoints, updateTeamPointsObj } from "./teamPointsHelper";

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
                        points: setNewTeamPoints(round, Points),
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
    reqList: ReqPoints[],
    teamPointsObj: ReqPointsArr,
    round: string,
    seriesName: string,
): Promise<boolean> => {
    try {
        const series = await SeriesPoints.findOne({ name: seriesName });
        if (series) {
            const { manufPointsList, teamPoints } = series;

            const updated = updateManufListPoints(
                reqList,
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

            series.markModified("teamPoints");

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
    reqList: ReqPoints[],
    backendManufPoints: ManufacturerPoints[],
    round: string,
) => {
    for (const result of reqList) {
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
                    points: setNewTeamPoints(round, Points),
                };

                backendManufPoints.push(newManuf);
            }
        } else {
            const newManuf: ManufacturerPoints = {
                manufName: Manufacturer,
                classification: result.Class,
                points: setNewTeamPoints(round, Points),
            };

            backendManufPoints.push(newManuf);
        }
    }
    return backendManufPoints;
};

export { handleGT3GT4ManufPts, handleManufPoints };
