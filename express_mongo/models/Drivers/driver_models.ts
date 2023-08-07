import { PointsInterface } from "../Points/points_models";

export interface EntryInterface {
    team: string;
    series: string;
    number: string;
    driver1: string;
    driver2?: string;
    driver3?: string;
    classification: string;
}

// Driver values stored in th db
export interface DriverPoints {
    driverName: string;
    classification?: string;
    points: PointsInterface;
}
