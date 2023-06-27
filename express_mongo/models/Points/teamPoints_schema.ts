import mongoose, { Document, Schema } from "mongoose";
import { TeamPoints } from "./teamPoints_models";

export interface TeamPointsModel extends TeamPoints, Document {}

const teamPointsSchema: Schema = new Schema({
  name: { type: String, required: true },
  series: { type: String, required: true },
  classification: { type: String, required: true },
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
    R15: { type: Schema.Types.Mixed },
    R16: { type: Schema.Types.Mixed },
    R17: { type: Schema.Types.Mixed },
    R18: { type: Schema.Types.Mixed },
  },
});

export default mongoose.model<TeamPointsModel>("TeamPoints", teamPointsSchema);
