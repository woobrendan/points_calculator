import {
    ReqPointsArr,
    ReqPoints,
    ManufacturerPoints,
    IManufPoints,
} from "../models/Points/points_models";
import SeriesPoints from "../models/Points/seriesPoints_schema";
import { setNewTeamPoints } from "./teamPointsHelper";

const handleManufPoints = (
    manufObj: ReqPointsArr,
    backendManufPoints: IManufPoints,
    round: string,
) => {
    // Loop through keys (class) from the incoming array manufObj
    for (const classification in manufObj) {
        if (classification in backendManufPoints) {
            // Once found, declare variables for each backend and incoming array for the appropriate class
            const dbArr = backendManufPoints[classification];
            const reqArr = manufObj[classification];

            for (const newResult of reqArr) {
                const { Manufacturer, Points } = newResult;
                let found = false;

                for (const dbEntry of dbArr) {
                    if (dbEntry.manufName === Manufacturer) {
                        dbEntry.points[round] = Points;
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    const newManuf: ManufacturerPoints = {
                        manufName: Manufacturer,
                        classification: newResult.Class,
                        points: setNewTeamPoints(round, Points),
                    };

                    dbArr.push(newManuf);
                }
            }
        }
    }
    return backendManufPoints;
};

const handleGT3GT4ManufPts = async (
    reqList: ReqPoints[],
    backendManufPoints: ManufacturerPoints[],
    round: string,
) => {
    for (const newResult of reqList) {
        const { Manufacturer, Points } = newResult;
        const foundManuf = backendManufPoints.find(
            (manuf) => manuf.manufName === Manufacturer,
        );

        if (foundManuf) {
            foundManuf.points[round] = Points;
        } else {
            const newManuf: ManufacturerPoints = {
                manufName: Manufacturer,
                classification: newResult.Class,
                points: setNewTeamPoints(round, Points),
            };

            backendManufPoints.push(newManuf);
        }
    }

    return backendManufPoints;
};

export { handleGT3GT4ManufPts, handleManufPoints };

//REQUEST || manufObj
// {'Pro': [{'Pos': '1', 'PIC': '1', '#': '93', 'Class': 'Pro', 'Points': 25, 'Team': 'Racers Edge Motorsports', 'Vehicle': 'Acura NSX GT3 EVO22', 'Series': 'gtwca', 'Manufacturer': 'Acura'}, {'Pos': '2', 'PIC': '2', '#': '28', 'Class': 'Pro', 'Points': 18, 'Team': 'RS1', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca', 'Manufacturer': 'Porsche'}, {'Pos': '13', 'PIC': '4', '#': '94', 'Class': 'Pro', 'Points': 15, 'Team': 'BimmerWorld', 'Vehicle': 'BMW M4 GT3', 'Series': 'gtwca', 'Manufacturer': 'BMW'}], 'Pro-Am': [{'Pos': '3', 'PIC': '1', '#': '120', 'Class': 'Pro-Am', 'Points': 25, 'Team': 'Wright Motorsports', 'Vehicle': 'Porsche 911 GT3-R (991.ii)', 'Series': 'gtwca', 'Manufacturer': 'Porsche'}, {'Pos': '4', 'PIC': '2', '#': '007', 'Class': 'Pro-Am', 'Points': 18, 'Team': 'TRG - The Racers Group', 'Vehicle': 'Aston Martin Vantage AMR GT3', 'Series': 'gtwca', 'Manufacturer': 'Aston Martin'}, {'Pos': '7', 'PIC': '4', '#': '91', 'Class': 'Pro-Am', 'Points': 15, 'Team': 'DXDT Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca', 'Manufacturer': 'Mercedes AMG GmbH'}, {'Pos': '8', 'PIC': '5', '#': '38', 'Class': 'Pro-Am', 'Points': 12, 'Team': 'ST Racing', 'Vehicle': 'BMW M4 GT3', 'Series': 'gtwca', 'Manufacturer': 'BMW'}, {'Pos': '9', 'PIC': '6', '#': '33', 'Class': 'Pro-Am', 'Points': 10, 'Team': 'Triarsi Competizione', 'Vehicle': 'Ferrari 296 GT3', 'Series': 'gtwca', 'Manufacturer': 'Ferrari'}], 'Am': [{'Pos': '15', 'PIC': '1', '#': '43', 'Class': 'Am', 'Points': 25, 'Team': 'RealTime Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca', 'Manufacturer': 'Mercedes AMG GmbH'}]}

// teamsBySeries: {
//     _id: "64a883d00c5298fa6cfe74fa",
//     name: "GT World Challenge",
//     teamPoints: [
//     ],
//     manufPoints: {
//     Pro: [
//         points: {
//         R1: 18,
//         R2: null,
//         R3: null,
//         R4: null,
//         R5: null,
//         R6: null,
//         R7: null,
//         R8: null,
//         R9: null,
//         R10: null,
//         R11: null,
//         R12: null,
//         R13: null,
//         R14: null,
//         R15: null,
//         R16: null,
//         R17: null,
//         R18: null
//         },
//         manufName: "Acura",
//         classification: "Pro",
//         _id: "64ac4e24d8ba27b76d327875"
//         ]
// },
