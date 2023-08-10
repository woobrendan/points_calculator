import mongoose, { Document, Schema } from "mongoose";
import { SeriesEntries } from "./entryList_models";

export interface EntryListModel extends SeriesEntries, Document {}

const entryListSchema: Schema = new Schema({
    name: { type: String },
    entries: [
        {
            number: String,
            teamName: String,
            driver1: String,
            driver2: String,
            driver3: String,
            classification: String,
            series: String,
            events: {
                "St Petersburg": Boolean,
                Sonoma: Boolean,
                NOLA: Boolean,
                COTA: Boolean,
                VIR: Boolean,
                Nashville: Boolean,
                RoadAm: Boolean,
                Sebring: Boolean,
                Indy: Boolean,
            },
        },
    ],
});

export default mongoose.model<EntryListModel>("EntryLists", entryListSchema);
