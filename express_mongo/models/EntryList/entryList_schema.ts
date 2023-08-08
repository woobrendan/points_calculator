import mongoose from "mongoose";

const entrySchema = new mongoose.Schema({
    number: Number,
    teamName: String,
    driver1: String,
    driver2: String,
    driver3: String,
    classification: String,
    series: String,
    events: {
        type: Map,
        of: Boolean,
        default: {},
    },
});

const seriesSchema = new mongoose.Schema({
    name: String,
    entries: [entrySchema],
});

const seriesListSchema = new mongoose.Schema({
    series: {
        type: Map,
        of: seriesSchema,
        default: {},
    },
});

// export default mongoose.model<EventsModel>("EventsModel", eventsSchema);
const SeriesListModel = mongoose.model("SeriesList", seriesListSchema);

module.exports = SeriesListModel;
