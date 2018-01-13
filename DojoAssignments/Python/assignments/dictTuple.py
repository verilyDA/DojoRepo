def dicTuple(myDict):
    newList = []

    for each in myDict:
        newTuple = (each , myDict[each])
        newList.append(newTuple)

    print(newList)


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dicTuple(my_dict)
