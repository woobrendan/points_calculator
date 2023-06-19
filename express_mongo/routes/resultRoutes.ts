import express from "express";
import controller from "../controllers/result_controller";

const router = express.Router();

router.post("/", controller.createResult);
router.get("/", controller.getAllResults);
router.get("/:resultId", controller.getResultById);
router.patch("/:resultId", controller.updateResult);
router.delete("/:resultId", controller.deleteResult);

export = router;
