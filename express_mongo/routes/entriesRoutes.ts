import express from "express";
import controller from "../controllers/entry_controller";

const router = express.Router();

router.post("/", controller.createEntry);
router.get("/", controller.getAllEntries);
router.get("/:entryId", controller.getEntryById);
router.patch("/:entryId", controller.updateEntry);
router.delete("/:entryId", controller.deleteEntry);

export = router;
