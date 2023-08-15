import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { getSeriesName, filterSeriesByPoints } from "../functions/functions";

const getAllDrivers = async (req: Request, res: Response) => {
   try {
        const data  = await SeriesPoints.find()

        if (data) {
            const filtered = filterSeriesByPoints(data, "driverPoints")

            return res.status(201).json({ seriesData: filtered });
        } else {
            return res.status(400).json({ message: "Series Not Found" });
        }
   } catch (error) {
        console.log("Error fetching driver points")
        res.status(500).json({ error });
   }
};

const driversBySeries = async (req: Request, res: Response) => {
    const series = getSeriesName(req.params.series);
    try {
        const data = await SeriesPoints.findOne({ name: series });
        return data
            ? res.status(200).json({ seriesDrivers: data.driversPoints })
            : res.status(400).json({ message: "Entries Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    driversBySeries,
    getAllDrivers,
};
