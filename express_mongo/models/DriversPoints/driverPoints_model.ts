import { PointsInterface } from "../Points/points_models";

interface DriverPoints {
    name: string;
    points: PointsInterface;
}

export interface SeriesDrivers {
    name: string;
    drivers: DriverPoints[];
}
