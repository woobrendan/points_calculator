export interface Events {
    [key: string]: SeriesList;
}

export interface SeriesList {
    [key: string]: Series;
}

export interface Series {
    name: string;
    entries: Entry[];
}

export interface Entry {
    number: number;
    driver1: string;
    driver2?: string;
    driver3?: string;
    classification: string;
    series: string;
}
