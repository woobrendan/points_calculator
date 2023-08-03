import { Request, Response } from "express";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { getSeriesName } from "../functions/functions";

const getAll = async (req: Request, res: Response) => {
    return SeriesPoints.find()
        .then((series) => res.status(201).json({ series }))
        .catch((error) => res.status(500).json({ error }));
};

const getBySeries = async (req: Request, res: Response) => {
    const series = req.params.series;
    const seriesName = getSeriesName(series);

    try {
        const seriesData = await SeriesPoints.findOne({ name: seriesName });
        return seriesData
            ? res.status(200).json({ seriesData })
            : res.status(400).json({ message: "Series Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default { getAll, getBySeries };
