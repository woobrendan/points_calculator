import express from "express";
import controller from "../controllers/driverPoints_controller";

const router = express.Router();

//  /api/drivers/

router.get("/", controller.getAllDrivers);
router.get("/:series", controller.driversBySeries);

export = router;
