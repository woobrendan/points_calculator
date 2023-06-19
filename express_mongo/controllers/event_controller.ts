import { Request, Response } from "express";
import Event from "../models/events_schema";

const getAllEvents = async (req: Request, res: Response) => {
  return Event.find()
    .then((events) => res.status(201).json({ events }))
    .catch((error) => res.status(500).json({ error }));
};

const getEventById = async (req: Request, res: Response) => {
  const eventId = req.params.EventId;
  try {
    const event = await Event.findById(eventId);
    return Event
      ? res.status(200).json({ event })
      : res.status(400).json({ message: "Event Not Found" });
  } catch (error) {
    return res.status(500).json({ error });
  }
};

const updateEvent = async (req: Request, res: Response) => {
  const eventId = req.params.eventId;
  return Event.findById(eventId)
    .then((event) => {
      if (event) {
        event.set(req.body);
        return event
          .save()
          .then((event) => res.status(201).json({ event }))
          .catch((error) => res.status(500).json({ error }));
      } else {
        res.status(404).json({ message: "event not found" });
      }
    })
    .catch((error) => res.status(500).json({ error }));
};

export default {
  getAllEvents,
  getEventById,
  updateEvent,
};
