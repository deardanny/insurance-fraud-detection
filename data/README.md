# Input data

The course project used `carclaims.csv`: 15,420 records, a `FraudFound` label (`Yes` / `No`), and policy/claim attributes. The source notebook does not establish a redistribution license; the data is therefore not bundled here.

Use an authorized course copy or a source whose terms permit your intended use. Similar public insurance-fraud datasets can have different column names, target encodings and rows; they are not automatically interchangeable.

Expected columns include `FraudFound`, `PolicyNumber`, `RepNumber`, `Year`, `Age`, `Sex`, `MaritalStatus`, `Month`, `WeekOfMonth`, `DayOfWeek`, `MonthClaimed`, `WeekOfMonthClaimed`, `DayOfWeekClaimed`, `Fault`, `PoliceReportFiled`, `WitnessPresent`, `AccidentArea`, `AgentType`, `VehicleCategory`, `VehiclePrice`, `PastNumberOfClaims`, `AgeOfVehicle`, `AgeOfPolicyHolder`, `NumberOfSuppliments`, `AddressChange-Claim`, `Days:Policy-Accident`, `Days:Policy-Claim`, `NumberOfCars`, `Deductible`, `DriverRating`, `PolicyType`, and `BasePolicy`.

The publication run used a local authorized copy. Raw rows and the input file are not committed. Place your file at `data/carclaims.csv` or set `FRAUD_DATA_PATH`.
