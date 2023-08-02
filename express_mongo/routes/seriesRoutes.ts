import express from "express";
import controller from "../controllers/series_controller";

const router = express.Router();

// url = /api/series/

router.get("/", controller.getAll);
router.get("/:series", controller.getBySeries);

export = router;
