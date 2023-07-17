import express from "express";
import controller from "../controllers/resultsController";

const router = express.Router();

// url = results/

router.post("/:series", controller.handleTeamManufPoints);

export = router;
