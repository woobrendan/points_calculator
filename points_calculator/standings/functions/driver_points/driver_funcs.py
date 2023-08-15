def sortDriverPoints(driversArr):
    classDrivers = {}
    for driver in driversArr:
        classification = driver.classification

        if classDrivers[classification]:
            classDrivers[classification].append(driver)
        else:
            classDrivers[classification] = [driver]
    return classDrivers
