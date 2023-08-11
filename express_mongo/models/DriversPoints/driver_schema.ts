import mongoose, { Document, Schema } from "mongoose";
import { SeriesDrivers } from "./driverPoints_model";

export interface DriverPointsModel extends SeriesDrivers, Document {}

const driverPointsSchema: Schema = new Schema({
    name: { type: String },
    entries: [
        {
            name: String,
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

export default mongoose.model<DriverPointsModel>(
    "DriverPoints",
    driverPointsSchema,
);
