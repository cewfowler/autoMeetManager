# Opens the command prompt to return context
def resetContext(resetContext):
    return;

# Load the starting positions from the config object
#   config: the config object
# Returns the starting position for:
#   1. The positions to reset the context to the command prompt (resetContext)
#   2. The app start button
#   3. The athlete button
#   4. The add athlete button
#   5. (TODO) The events
def loadStartingPos(config):
    try:
        resetContext = config["resetContext"];
    except:
        commandPromptPos = {"x": 10, "y": 10};
        commandPromptToolbarPos = {"x": 10, "y": 10};
        resetContext = {"commandPromptToolbarPos": commandPromptToolbarPos,
                         "commandPromptPos": commandPromptPos}

    try:
        startAppBtnPos = config["startAppBtnPos"];
    except:
        startAppBtnPos = {"x": 10, "y": 10};

    try:
        athletesBtnPos = config["athletesBtnPos"];
    except:
        athletesBtnPos = {"x": 10, "y": 10};

    try:
        addAthleteBtnPos = config["addAthleteBtnPos"];
    except:
        addAthleteBtnPos = {"x": 10, "y": 10};

    #try:
    #    events = config["events"];
    #except:
    #    events = { "50 fly":        {"x": 10, "y": 10},
    #               "50 back":       {"x": 10, "y": 10},
    #               "50 breast":     {"x": 10, "y": 10},
    #               "50 free":       {"x": 10, "y": 10},
    #               "100 fly":       {"x": 10, "y": 10},
    #               "100 back":      {"x": 10, "y": 10},
    #               "100 breast":    {"x": 10, "y": 10},
    #               "100 free":      {"x": 10, "y": 10},
    #               "100 im":        {"x": 10, "y": 10},
    #               "200 fly":       {"x": 10, "y": 10},
    #               "200 back":      {"x": 10, "y": 10},
    #               "200 breast":    {"x": 10, "y": 10},
    #               "200 free":      {"x": 10, "y": 10},
    #               "200 im":        {"x": 10, "y": 10},
    #               "400 im":        {"x": 10, "y": 10},
    #               "500 free":      {"x": 10, "y": 10},
    #               "1000 free":     {"x": 10, "y": 10},
    #             };

    return [resetContext, startAppBtnPos, athletesBtnPos, addAthleteBtnPos]
