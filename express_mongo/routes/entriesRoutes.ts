import express from "express";
import controller from "../controllers/entry_controller";

const router = express.Router();

router.get("/", controller.getAllEntries);

export = router;
