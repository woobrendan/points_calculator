import { ResultInterface, HardChargerInterface } from "../models/result_models";

const resultBuilder = (result: ResultInterface) => {
  const { firstPlace, secondPlace, thirdPlace } = result;
  return {
    ...result,
    firstPlace: { ...firstPlace },
    ...(secondPlace ? { secondPlace: { ...secondPlace } } : {}),
    ...(thirdPlace ? { thirdPlace: { ...thirdPlace } } : {}),
  };
};

const hardChargeResult = (result: HardChargerInterface) => {
  const { entry } = result;
  return {
    ...result,
    entry: {
      ...entry,
      driver1: {
        ...entry.driver1,
      },
      ...(entry.driver2 ? { driver2: { ...entry.driver2 } } : {}),
      ...(entry.driver3 ? { driver3: { ...entry.driver3 } } : {}),
    },
  };
};

export { resultBuilder, hardChargeResult };
