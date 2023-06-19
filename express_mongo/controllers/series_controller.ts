import { Request, Response } from "express";
import Series from "../models/series_schema";

const getAllSeries = async (req: Request, res: Response) => {
  try {
    const series = await Series.find();
    res.status(200).json({ series });
  } catch (error) {
    res.status(500).json({ error });
  }
};

export default {
  getAllSeries,
};
