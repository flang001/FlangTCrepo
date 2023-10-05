def Test():
  windows = Sys.FindAllChildren("VisibleOnScreen", "true", 2)
  if (l := len(windows)) > 0:
    Log.Message(aqString.Format("There are %i visible windows on the screen", l))