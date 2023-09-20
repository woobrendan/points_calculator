import {
    ReqPointsArr,
    SeriesDrivers,
    DriverPoints,
} from "../models/Points/points_models";
// import SeriesPoints from "../models/Points/seriesPoints_schema";
import { setNewPoints } from "./functions";

const handleDriverPoints = (
    driverObj: ReqPointsArr,
    backendDrivPoints: SeriesDrivers,
    round: string,
): SeriesDrivers => {
    for (const classification in driverObj) {
        const dbArr = backendDrivPoints[classification];
        const reqArr = driverObj[classification];

        for (const newResult of reqArr) {
            const { Points, driver } = newResult;
            let found = false;

            for (const dbEntry of dbArr) {
                if (dbEntry.name === driver) {
                    dbEntry.points[round] = Points;
                    found = true;
                    break;
                }
            }

            if (!found) {
                const newEntry: DriverPoints = {
                    name: driver as string,
                    classification: newResult.Class,
                    points: setNewPoints(round, Points),
                };

                dbArr.push(newEntry);
            }
        }
    }
    return backendDrivPoints;
};

export default handleDriverPoints;
