import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import EntryLists from "../models/EntryList/entryList_schema";
import { getSeriesName } from "../functions/functions";

const getAllEntries = async (req: Request, res: Response) => {
    return EntryLists.find()
        .then((entry) => res.status(201).json({ entry }))
        .catch((error) => res.status(500).json({ error }));
};

const getEntriesBySeries = async (req: Request, res: Response) => {
    const series = getSeriesName(req.params.series);
    try {
        const seriesEntries = await EntryLists.findOne({ name: series });
        return seriesEntries
            ? res.status(200).json({ seriesEntries })
            : res.status(400).json({ message: "Entries Not Found" });
    } catch (error) {
        return res.status(500).json({ error });
    }
};

export default {
    getEntriesBySeries,
    getAllEntries,
};
