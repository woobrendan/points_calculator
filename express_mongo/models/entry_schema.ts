import mongoose, { Document, Schema } from "mongoose";
import { EntryInterface } from "./models";

export interface EntryModel extends EntryInterface, Document {}

const entrySchema: Schema = new Schema({
  team: { type: String, required: true },
  vehicle: { type: String, required: true },
  classification: { type: String, required: true },
  number: { type: String, required: true },
  carImage: { type: String, required: false },
  series: { type: String, required: true },
  year: { type: Number, required: true },
  driver1: {
    name: { type: String, required: true },
    rating: { type: String, required: false },
    nationality: { type: String, required: true },
  },
  driver2: {
    name: { type: String },
    rating: { type: String },
    nationality: { type: String },
  },
  driver3: {
    name: { type: String },
    rating: { type: String },
    nationality: { type: String },
  },
});

export default mongoose.model<EntryModel>("Entries", entrySchema);
export { entrySchema };
