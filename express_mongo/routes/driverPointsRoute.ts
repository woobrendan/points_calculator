import express from "express";
import controller from "../controllers/driverPoints_controller";

const router = express.Router();

//  /api/drivers/

router.get("/", controller.getAlldrivers);
router.get("/:series", controller.driversBySeries);

export = router;
