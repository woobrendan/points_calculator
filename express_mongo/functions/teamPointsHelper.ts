import { PointsInterface } from "../models/Points/points_models";

const setNewTeamPoints = (round: string, points: number) => {
  const pts: PointsInterface = {
    R1: null,
    R2: null,
    R3: null,
    R4: null,
    R5: null,
    R6: null,
    R7: null,
    R8: null,
    R9: null,
    R10: null,
    R11: null,
    R12: null,
    R13: null,
    R14: null,
    R15: null,
    R16: null,
    R17: null,
    R18: null,
  };

  for (const roundNum in pts) {
    if (roundNum === round) {
      pts[roundNum] = points;
    }
  }

  return pts;
};

const getSeriesName = (val: string) => {
  if (val === "gtwca") return "GT World Challenge America";
  if (val === "pgt4a") return "Pirelli GT4 America";
  if (val === "gta") return "GT America";
  if (val === "tca") return "TC America";
  if (val === "tgr") return "Toyota GR Cup";
};

export { setNewTeamPoints, getSeriesName };
