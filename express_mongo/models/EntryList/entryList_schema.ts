import mongoose, { Document, Schema } from "mongoose";
import { Events, Entry, Series, SeriesList } from "./entryList_models";

const EntrySchema = new Schema<Entry>({
    number: { type: Number, required: true },
    driver1: { type: String, required: true },
    driver2: { type: String },
    driver3: { type: String },
    classification: { type: String, required: true },
    series: { type: String, required: true },
});

const SeriesSchema = new Schema<Series>({
    name: { type: String, required: true },
    entries: { type: [EntrySchema], required: true },
});

const EventsSchema: Schema = new Schema<Events>({});

// export default mongoose.model<EventsModel>("EventsModel", eventsSchema);
const EventsModel = mongoose.model<Events & Document>("Events", EventsSchema);

export default EventsModel;
