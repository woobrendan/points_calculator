import express from "express";
import controller from "../controllers/manufPoints_controller";

const router = express.Router();

// url = /api/manufPoints/

router.get("/", controller.getAll);
router.get("/:series", controller.getManufPoints);

export = router;
