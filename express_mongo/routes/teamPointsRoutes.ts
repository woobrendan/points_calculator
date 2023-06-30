import express from "express";
import controller from "../controllers/teamPoints_controller";

const router = express.Router();

// url = teamPoints/

router.get("/", controller.getAll);
router.get("/:series", controller.getBySeries);
router.post("/:series", controller.handleTeamPoints);
router.get("/:series", controller.getBySeries);

export = router;
