import express from "express";
import controller from "../controllers/teamPoints_controller";

const router = express.Router();

router.get("/:series", controller.getBySeries);

export = router;
