import express from "express";
import controller from "../controllers/series_controller";

const router = express.Router();

// url = series/

router.get("/:series", controller.getAll);

export = router;
