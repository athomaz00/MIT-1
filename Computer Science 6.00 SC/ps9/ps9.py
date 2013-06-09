# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    subjects_dict = {}
    inputFile = open(filename)
    for line in inputFile:
        name, value, work = line.strip().split(",")
        subjects_dict[name] = (int(value), int(work))
    return subjects_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[0] - subInfo2[0]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo2[1] - subInfo1[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    if subInfo1[0] / float(subInfo1[1]) > subInfo2[0] / float(subInfo2[1]):
        return 1
    elif subInfo1[0] / float(subInfo1[1]) == subInfo2[0] / float(subInfo2[1]):
        return 0
    else:
        return -1

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    subjects_to_take = {}
    for item in sorted(subjects.iteritems(), cmp=comparator, key=lambda x:x[1], reverse=True):
        if item[1][1] <= maxWork:
            maxWork -= item[1][1]
            subjects_to_take[item[0]] = item[1]
    return subjects_to_take

subjects = loadSubjects(SHORT_SUBJECT_FILENAME)
printSubjects(greedyAdvisor(subjects, 7, cmpValue))
printSubjects(greedyAdvisor(subjects, 7, cmpWork))
printSubjects(greedyAdvisor(subjects, 5, cmpRatio))


#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisorH(taken, subjects, maxWork, subject_dict):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    if len(subjects) == 0:
        return taken
    if maxWork == 0:
        return taken
    dont_take = bruteForceAdvisorH(taken, subjects[1:], maxWork, subject_dict)
    subject = subjects[0]
    work = subject_dict[subject][1]
    if work <= maxWork:
        take = bruteForceAdvisorH(taken + [subject], subjects[1:], maxWork - work, subject_dict)
    else:
        take = taken
    dont_value = sum([subject_dict[s][0] for s in dont_take])
    take_value = sum([subject_dict[s][0] for s in take])
    if dont_value > take_value:
        return dont_take
    else:
        return take

def bruteForceAdvisor(subjects, maxWork):
    list_of_classes = bruteForceAdvisorH([], subjects.keys(), maxWork, subjects)
    taken = {}
    for subject in list_of_classes:
        taken[subject] = subjects[subject]
    return taken


printSubjects(bruteForceAdvisor(subjects, 5))
    

        
        
        
    
