export interface TeamPoints {
  teamName: string;
  classification: string;
  points: PointsInterface;
}

export interface ManufacturerPoints {
  manufName: string;
  classification: string;
  points: PointsInterface;
}

export interface IManufPoints {
  [key: string]: ManufacturerPoints[];
}

export interface PointsInterface {
  [key: string]: number | null;
  R1: number | null;
  R2: number | null;
  R3: number | null;
  R4: number | null;
  R5: number | null;
  R6: number | null;
  R7: number | null;
  R8: number | null;
  R9: number | null;
  R10: number | null;
  R11: number | null;
  R12: number | null;
  R13: number | null;
  R14: number | null;
  R15: number | null;
  R16: number | null;
  R17: number | null;
  R18: number | null;
}

export interface Series {
  seriesName: string;
  teamPoints: TeamPoints[];
  manufPoints: IManufPoints;
}

export interface ReqPoints {
  [key: string]: string | number;
  Pos: string;
  PIC: string;
  Class: string;
  Points: number;
  Team: string;
  Vehicle: string;
  Series: string;
  Manufacturer: string;
}

export interface ReqPointsArr {
  [key: string]: ReqPoints[];
}
