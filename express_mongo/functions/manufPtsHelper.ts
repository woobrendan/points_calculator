import {
    ReqPointsArr,
    ReqPoints,
    ManufacturerPoints,
    IManufPoints,
} from "../models/Points/points_models";

import { setNewTeamPoints } from "./teamPointsHelper";

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

const handleGT3GT4ManufPts = async (
    reqList: ReqPoints[],
    backendManufPoints: ManufacturerPoints[],
    round: string,
) => {
    // acc is accumulator, which starts as the backendManufPoints. newResult is the current iteration through reqList
    return reqList.reduce((acc, newResult) => {
        const { Manufacturer, Points } = newResult;

        // same as backendManufPoints.find
        const foundManuf = acc.find(
            (manuf) => manuf.manufName === Manufacturer,
        );

        if (foundManuf) {
            foundManuf.points[round] = Points;
        } else {
            const newManuf: ManufacturerPoints = {
                manufName: Manufacturer,
                classification: newResult.Class,
                points: setNewTeamPoints(round, Points),
            };

            acc.push(newManuf);
        }

        return acc;
    }, backendManufPoints);
};

export { handleGT3GT4ManufPts, handleManufPoints };
