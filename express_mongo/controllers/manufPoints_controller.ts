import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { getSeriesName } from "../functions/teamPointsHelper";

const getAll = async (req: Request, res: Response) => {
    return SeriesPoints.find()
        .then((series) => res.status(201).json({ series }))
        .catch((error) => res.status(500).json({ error }));
};

const getManufPoints = async (req: Request, res: Response) => {
    const series = req.params.series;
    let seriesName = getSeriesName(series);

    const manuf_type =
        series === "gtwca" || series === "pgt4a"
            ? "manufPointsList"
            : "manufPoints";

    try {
        const data = await SeriesPoints.findOne({ name: seriesName });
        return data
            ? res.status(200).json({ [manuf_type]: data[manuf_type] })
            : res.status(400).json({ message: "Series Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    getManufPoints,
    getAll,
};
