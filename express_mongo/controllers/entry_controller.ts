import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import EntryLists from "../models/EntryList/entryList_schema";

const getAllEntries = async (req: Request, res: Response) => {
    return EntryLists
        .find()
        .then((entry) => res.status(201).json({ entry }))
        .catch((error) => res.status(500).json({ error }));
};

// const getEntriesBySeries = async (req: Request, res: Response) => {
//   const series = req.params.series;
//   try {
//     const seriesEntries = await SeriesListModel.findOne({
//       'series.name': series
//     });
//     return seriesEntries.entries
//       ? res.status(200).json({ seriesEntries.entries })
//       : res.status(400).json({ message: "Entries Not Found" });
//   } catch (error) {
//     return res.status(500).json({ error });
//   }
// };

// const getAllEntries = async (req: Request, res: Response) => {
//   return Entries.find()
//     .then((entry) => res.status(201).json({ entry }))
//     .catch((error) => res.status(500).json({ error }));
// };

// const updateEntry = async (req: Request, res: Response) => {
//   const entryId = req.params.entryId;
//   return Entries.findById(entryId)
//     .then((entry) => {
//       if (entry) {
//         entry.set(req.body);
//         return entry
//           .save()
//           .then((entry) => res.status(201).json({ entry }))
//           .catch((error) => res.status(500).json({ error }));
//       } else {
//         res.status(404).json({ message: "Entry not found" });
//       }
//     })
//     .catch((error) => res.status(500).json({ error }));
// };

// const deleteEntry = (req: Request, res: Response) => {
//   const entryId = req.params.entryId;
//   return Entries.findByIdAndDelete(entryId)
//     .then((entry) =>
//       entry
//         ? res.status(201).json({ message: "Deleted" })
//         : res.status(404).json({ message: "Not Found" }),
//     )
//     .catch((error) => res.status(500).json({ error }));
// };

export default {
    // getEntriesBySeries,
    getAllEntries,
    // updateEntry,
    // deleteEntry,
};
