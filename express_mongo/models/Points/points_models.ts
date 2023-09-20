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

//** Interfaces for Team and Manuf Array */
export interface TeamPoints {
    teamName?: string;
    classification?: string;
    points: PointsInterface;
}

export interface ITeamPoints {
    [key: string]: TeamPoints[];
}

export interface ManufacturerPoints {
    manufName?: string;
    classification?: string;
    points: PointsInterface;
}

export interface IManufPoints {
    [key: string]: ManufacturerPoints[];
}

//** Interface for Series Points Schema */
export interface Series {
    name: string;
    teamPoints: ITeamPoints;
    manufPoints: IManufPoints;
    manufPointsList: ManufacturerPoints[];
    driversPoints: SeriesDrivers[];
}

//** Interfaces for points coming from front end */
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

//** Interfaces for Driver Points */

export interface DriverPoints {
    name: string;
    classification: string;
    points: PointsInterface;
}

export interface SeriesDrivers {
    [key: string]: DriverPoints[];
}
