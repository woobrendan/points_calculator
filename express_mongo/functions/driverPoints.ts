import { ReqPointsArr } from "../models/Points/points_models";
import SeriesPoints from "../models/Points/seriesPoints_schema";

const handleDriverPoints = async (
    driverObj: ReqPointsArr,
    seriesName: string,
    round: string,
) => {
    const series = await SeriesPoints.findOne({ name: seriesName });
};
