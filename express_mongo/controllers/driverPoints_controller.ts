import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import DriverPoints from "../models/DriversPoints/driver_schema";
import { getSeriesName } from "../functions/functions";

const getAllDrivers = async (req: Request, res: Response) => {
    return DriverPoints.find()
        .then((drivers) => res.status(201).json({ drivers }))
        .catch((error) => res.status(500).json({ error }));
};

const driversBySeries = async (req: Request, res: Response) => {
    const series = getSeriesName(req.params.series);
    try {
        const seriesDrivers = await DriverPoints.findOne({ name: series });
        return seriesDrivers
            ? res.status(200).json({ seriesDrivers })
            : res.status(400).json({ message: "Entries Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    driversBySeries,
    getAllDrivers,
};
