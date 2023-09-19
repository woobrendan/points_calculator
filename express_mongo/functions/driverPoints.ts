import { ReqPointsArr, SeriesDrivers } from "../models/Points/points_models";
import SeriesPoints from "../models/Points/seriesPoints_schema";

const handleDriverPoints = async (
    driverObj: ReqPointsArr,
    backendDrivPoints: SeriesDrivers,
    round: string,
) => {
    for (const classification in driverObj) {
        const dbArr = backendDrivPoints[classification];
        const reqArr = driverObj[classification];

        for (const newResult of reqArr) {
            const { Points, driver } = newResult;
        }
    }
};
