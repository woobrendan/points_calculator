import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { getSeriesName } from "../functions/functions";

const getAll = async (req: Request, res: Response) => {
    try {
        const data = await SeriesPoints.find();

        if (data) {
            // Loop through each series object returned (type Series) and only return keys needed
            const filtered = data.map((series: any) => {
                const keys = ["name", "teamPoints"];

                const cleanSeriesObj: any = {};

                keys.forEach((key) => {
                    cleanSeriesObj[key] = series[key];
                });

                return cleanSeriesObj;
            });

            return res.status(201).json({ seriesData: filtered });
        } else {
            return res.status(400).json({ message: "Series Not Found" });
        }
    } catch (error) {
        res.status(500).json({ error });
    }
};

const getTeamPoints = async (req: Request, res: Response) => {
    const series = req.params.series;
    const seriesName = getSeriesName(series);

    try {
        const data = await SeriesPoints.findOne({ name: seriesName });
        return data
            ? res.status(200).json({ seriesData: data?.teamPoints })
            : res.status(400).json({ message: "Series Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    getTeamPoints,
    getAll,
};
