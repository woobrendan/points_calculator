import mongoose, { Document, Schema } from "mongoose";
import { Series, TeamPoints, IManufPoints } from "./points_models";

export interface SeriesPointsModel extends Series, Document {}

const seriesPointsSchema: Schema = new Schema({
    name: { type: String },
    teamPoints: {
        type: Schema.Types.Mixed,
        strict: false,
    },
    manufPoints: {
        type: Schema.Types.Mixed,
    },
    manufPointsList: [
        {
            manufName: { type: String },
            points: {
                R1: { type: Schema.Types.Mixed },
                R2: { type: Schema.Types.Mixed },
                R3: { type: Schema.Types.Mixed },
                R4: { type: Schema.Types.Mixed },
                R5: { type: Schema.Types.Mixed },
                R6: { type: Schema.Types.Mixed },
                R7: { type: Schema.Types.Mixed },
                R8: { type: Schema.Types.Mixed },
                R9: { type: Schema.Types.Mixed },
                R10: { type: Schema.Types.Mixed },
                R11: { type: Schema.Types.Mixed },
                R12: { type: Schema.Types.Mixed },
                R13: { type: Schema.Types.Mixed },
                R14: { type: Schema.Types.Mixed },
            },
        },
    ],
});

export default mongoose.model<SeriesPointsModel>(
    "SeriesPoints",
    seriesPointsSchema,
);
