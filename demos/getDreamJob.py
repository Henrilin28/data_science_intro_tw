
def getDreamJob(studying, hardworking, projects):

    isPrepared = studying & hardworking & projects

    if (isPrepared):
        print("I am ready")
        return True
    else:
        return False



