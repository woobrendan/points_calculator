export interface DriverInfo {
  name: string;
  rating: string;
  nationality: string;
  totalPoints: number;
  points: number[];
}

export interface EntryInterface {
  team: string;
  vehicle: string;
  series: string;
  number: string;
  driver1: DriverInfo;
  driver2?: DriverInfo;
  driver3?: DriverInfo;
  classification: string;
  carImage: string;
  year: number;
}
