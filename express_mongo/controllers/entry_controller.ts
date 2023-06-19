import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import Entries from "../models/entry_schema";

const createEntry = async (req: Request, res: Response) => {
  const entry = new Entries({
    _id: new mongoose.Types.ObjectId(),
    ...req.body,
    driver1: {
      ...req.body.driver1,
    },
    ...(req.body.driver2 ? { driver2: { ...req.body.driver2 } } : {}),
    ...(req.body.driver3 ? { driver3: { ...req.body.driver3 } } : {}),
  });

  try {
    const savedEntry = await entry.save();
    res.status(200).json({ savedEntry });
  } catch (error) {
    res.status(500).json({ error });
  }

  // return entry
  //   .save()
  //   .then((entry) => res.status(201).json({ entry }))
  //   .catch((error) => res.status(500).json({ error }));
};

const getEntryById = async (req: Request, res: Response) => {
  const entryId = req.params.entryId;
  try {
    const entry = await Entries.findById(entryId);
    return entry
      ? res.status(200).json({ entry })
      : res.status(400).json({ message: "Entry Not Found" });
  } catch (error) {
    return res.status(500).json({ error });
  }
};

const getAllEntries = async (req: Request, res: Response) => {
  return Entries.find()
    .then((entry) => res.status(201).json({ entry }))
    .catch((error) => res.status(500).json({ error }));
};

const updateEntry = async (req: Request, res: Response) => {
  const entryId = req.params.entryId;
  return Entries.findById(entryId)
    .then((entry) => {
      if (entry) {
        entry.set(req.body);
        return entry
          .save()
          .then((entry) => res.status(201).json({ entry }))
          .catch((error) => res.status(500).json({ error }));
      } else {
        res.status(404).json({ message: "Entry not found" });
      }
    })
    .catch((error) => res.status(500).json({ error }));
};

const deleteEntry = (req: Request, res: Response) => {
  const entryId = req.params.entryId;
  return Entries.findByIdAndDelete(entryId)
    .then((entry) =>
      entry
        ? res.status(201).json({ message: "Deleted" })
        : res.status(404).json({ message: "Not Found" }),
    )
    .catch((error) => res.status(500).json({ error }));
};

export default {
  createEntry,
  getEntryById,
  getAllEntries,
  updateEntry,
  deleteEntry,
};
