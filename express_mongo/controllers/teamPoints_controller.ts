import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import TeamPoints from "../models/Points/teamPoints_schema";

const getBySeries = async (req: Request, res: Response) => {
  const series = req.params.series;

  try {
    const teamsBySeries = await TeamPoints.findOne({ name: series });
    return teamsBySeries
      ? res.status(200).json({ teamsBySeries })
      : res.status(400).json({ message: "Series Not Found" });
  } catch (error) {
    return res.status(500).json({ error });
  }
};

export default {
  getBySeries,
};
