import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import SeriesPoints from "../models/Points/seriesPoints_schema";

const getBySeries = async (req: Request, res: Response) => {
  const series = req.params.series;

  try {
    const teamsBySeries = await SeriesPoints.findOne({ name: series });
    return teamsBySeries
      ? res.status(200).json({ teamsBySeries })
      : res.status(400).json({ message: "Series Not Found" });
  } catch (error) {
    return res.status(500).json({ error });
  }
};

const getTeamPoints = async (req: Request, res: Response) => {
  const seriesName = req.params.series;

  try {
    const series = await SeriesPoints.findOne({ name: seriesName });
    if (series) {
      const teamPointsList = series.teamPoints;
      return res.status(200).json({ teamPointsList });
    } else {
      return res.status(400).json({ message: "Series Not Found" });
    }
  } catch (error) {
    return res.status(500).json({ error });
  }
};

export default {
  getBySeries,
  getTeamPoints,
};
