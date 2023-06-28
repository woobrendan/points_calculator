interface EntryResultInterfance {
  team: string;
  vehicle: string;
  number: string;
  driver1: string;
  driver2?: string;
  driver3?: string;
}

export interface ResultInterface {
  class: string;
  firstPlace: EntryResultInterfance;
  secondPlace?: EntryResultInterfance;
  thirdPlace?: EntryResultInterfance;
}

export interface FullResultInterface {
  series: string;
  date: string;
  event: string;
  result1: ResultInterface;
  result2?: ResultInterface;
  result3?: ResultInterface;
  result4?: ResultInterface;
}
