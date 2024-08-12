#!/usr/bin/python3
'''
Solution to lockboxes problem
'''


def canUnlockAll(boxes):
    '''
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained
    '''
    if (boxes):
        numOfBoxes = len(boxes)
        setOfKeys = {0}
        setOfKeys.update(boxes[0])
        visitedBoxes = {0}
        while True:
            newBoxVisited = False
            keys = setOfKeys.copy()
            for key in keys:
                if key not in visitedBoxes.copy() and key < numOfBoxes:
                    setOfKeys.update(boxes[key])
                    visitedBoxes.add(key)
                    newBoxVisited = True
            if not newBoxVisited:
                break
        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False
        return True
    return False
