import { Request, Response } from "express";
import { getSeriesName } from "../functions/teamPointsHelper";
import handleGT3GT4ManufPts from "../functions/manufPtsHelper";
import teamManufPoints from "../functions/teamManufPoints";

const handleTeamManufPoints = async (req: Request, res: Response) => {
    const seriesName = getSeriesName(req.params.series);
    const { manufResults, teamResults, roundNum } = req.body;

    try {
        let manuf = false;
        if (seriesName === "gtwca" || seriesName === "pgt4a") {
            manuf = await handleGT3GT4ManufPts(
                manufResults,
                seriesName,
                roundNum,
            );
        } else {
            const manufComplete = await teamManufPoints(
                manufResults,
                seriesName,
                roundNum,
                "manufPoints",
            );
            const teamComplete = await teamManufPoints(
                teamResults,
                seriesName,
                roundNum,
                "teamPoints",
            );

            if (manufComplete && teamComplete) manuf = true;
        }
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
