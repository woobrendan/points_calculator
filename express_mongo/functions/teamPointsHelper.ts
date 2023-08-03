import {
    PointsInterface,
    ReqPointsArr,
    ITeamPoints,
    TeamPoints,
} from "../models/Points/points_models";
import { setNewPoints } from "./functions";

const updateTeamPoints = (
    round: string,
    points: number,
    ptsObj: PointsInterface,
) => {
    for (const roundNum in ptsObj) {
        if (roundNum === round) {
            ptsObj[roundNum] = points;
        }
    }

    return ptsObj;
};

const updateTeamPointsObj = (
    teamPointsObj: ReqPointsArr,
    backendTeamPts: ITeamPoints,
    round: string,
): ITeamPoints => {
    // Loop through keys (class) from the incoming array teamPointsObj
    for (const classification in teamPointsObj) {
        if (classification in backendTeamPts) {
            // Once found, declare variables for each backend and incoming array for the appropriate class
            const dbArr = backendTeamPts[classification];
            const reqArr = teamPointsObj[classification];

            for (const newResult of reqArr) {
                const { Points, Team } = newResult;
                let found = false;

                for (const dbEntry of dbArr) {
                    if (dbEntry.teamName === Team) {
                        dbEntry.points[round] = Points;
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    const newEntry: TeamPoints = {
                        teamName: Team,
                        classification: newResult.Class,
                        points: setNewPoints(round, Points),
                    };

                    dbArr.push(newEntry);
                }
            }
        }
    }

    return backendTeamPts;
};

export { updateTeamPoints, updateTeamPointsObj };
