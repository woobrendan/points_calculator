import { Request, Response } from "express";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { getSeriesName } from "../functions/teamPointsHelper";
import handleManufPoints from "../functions/manufPtsHelper";

const handleTeamManufPoints = async (req: Request, res: Response) => {
    const seriesName = getSeriesName(req.params.series);
    const { manufResults, teamResults, roundNum } = req.body;

    try {
        const manuf = await handleManufPoints(
            manufResults,
            seriesName,
            roundNum,
        );
        if (manuf) {
            return res.status(200).send();
        } else {
            console.log("I am a failure");
            return res.status(400).send();
        }
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    handleTeamManufPoints,
};