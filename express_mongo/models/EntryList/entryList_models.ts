interface Events {
    events: Event[];
}

interface Event {
    name: string;
    [key: string]: Series;
}

interface Series {
    name: string;
    entries: Entry[];
}

interface Entry {
    number: number;
    driver1: string;
    driver2?: string;
    driver3?: string;
    classification: string;
    series: string;
}
