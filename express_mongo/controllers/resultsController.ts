import { Request, Response } from "express";
import { getSeriesName } from "../functions/teamPointsHelper";
import { handleGT3GT4ManufPts } from "../functions/manufPtsHelper";
import teamManufPoints from "../functions/teamManufPoints";

const handleTeamManufPoints = async (req: Request, res: Response) => {
    const series = req.params.series;
    const seriesName = getSeriesName(series);
    const { manufResults, teamResults, roundNum } = req.body;

    try {
        let manuf = false;
        if (series === "gtwca" || series === "pgt4a") {
            manuf = await handleGT3GT4ManufPts(
                manufResults,
                teamResults,
                roundNum,
                seriesName,
            );
        } else {
            manuf = await teamManufPoints(
                manufResults,
                teamResults,
                seriesName,
                roundNum,
            );
        }
        if (manuf) {
            return res.status(200).send();
        } else {
            console.log("Error Updating all team and manuf points");
            return res.status(400).send();
        }
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    handleTeamManufPoints,
};
