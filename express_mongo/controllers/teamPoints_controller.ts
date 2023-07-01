import { NextFunction, Request, Response } from "express";
import mongoose from "mongoose";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import {
  setNewTeamPoints,
  getSeriesName,
  updateTeamPoints,
} from "../functions/teamPointsHelper";

const getAll = async (req: Request, res: Response) => {
  return SeriesPoints.find()
    .then((series) => res.status(201).json({ series }))
    .catch((error) => res.status(500).json({ error }));
};

const getBySeries = async (req: Request, res: Response) => {
  const series = req.params.series;
  let seriesName = getSeriesName(series);

  try {
    const teamsBySeries = await SeriesPoints.findOne({ name: seriesName });
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

//** RIGHT NOW WILL CHANGE PREVIOUS ROUND NULL VALUES NEED TO LOOP */

const handleTeamPoints = async (req: Request, res: Response) => {
  const { teamName, classification, round, points } = req.body;
  const seriesName = getSeriesName(req.params.series);

  try {
    const series = await SeriesPoints.findOne({ name: seriesName });
    let found = false;
    if (series) {
      series.teamPoints.forEach((entry, index) => {
        if (entry.teamName === teamName) {
          series.teamPoints[index] = {
            ...entry,
            points: updateTeamPoints(round, points, entry.points),
          };
          found = true;
        }
      });

      const newTeam = {
        teamName,
        classification,
        points: setNewTeamPoints(round, points),
      };

      if (!found) {
        series.teamPoints.push(newTeam);
      }
      await series.save();
      res.status(200).json({ newTeam });
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
  handleTeamPoints,
  getAll,
};

// {
//     "teamName": "MDK",
//     "classification": "Pro",
//     "points": {
//       "R1": null,
//       "R2": null,
//       "R3": null,
//       "R4": null,
//       "R5": null,
//       "R6": null,
//       "R7": null,
//       "R8": null,
//       "R9": null,
//       "R10": null,
//       "R11": null,
//       "R12": null,
//       "R13": null,
//       "R14": null,
//       "R15": null,
//       "R16": null,
//       "R17": null,
//       "R18": null,
//     },
//   }
