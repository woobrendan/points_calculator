export interface TeamPoints {
  teamName: string;
  classification: string;
  points: PointsInterface;
}

interface ManufacturerPoints {
  manufName: string;
  points: PointsInterface;
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
  name: string;
  teamPoints: TeamPoints[];
  manufPoints: ManufacturerPoints[];
}
