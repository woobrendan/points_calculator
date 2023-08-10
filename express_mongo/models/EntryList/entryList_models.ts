export interface SeriesEntries {
    name: string;
    entries: Entry[];
}

export interface Entry {
    number: number;
    teamName: string;
    driver1: string;
    driver2?: string;
    driver3?: string;
    classification: string;
    series: string;
    events: EventsList;
}

export interface EventsList {
    [key: string]: boolean;
}
