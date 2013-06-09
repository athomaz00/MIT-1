
"""
Author: Joshua Cole
Collaborators: N/A
Time: Far too long

6.00 Problem Set 8 - This is just a programming assignemnt I worked on to
improve as a programmer. Feel free to use it however you like.
"""
import numpy
import random
from matplotlib import pyplot

from ps7 import SimplePatient, SimpleVirus, NoChildException

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    resistances = {}
    mut_prob = 0.0
    
    def __init__(self, max_birth_prob, clear_prob, resistances, mut_prob):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        clearProb: Maximum clearance probability (a float between 0-1).

        max_birth_prob: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mut_prob: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """
        self.resistances = resistances.copy()
        self.mut_prob = mut_prob
        super(ResistantVirus, self).__init__(max_birth_prob, clear_prob)


    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.resistances[drug]
        except KeyError:
            return False



    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        if activeDrugs and not all(map(self.isResistantTo, activeDrugs)):
            raise NoChildException("Virus wasn't resistant to drugs.")
        elif random.random() > self.max_birth_prob * (1 - popDensity):
            raise NoChildException("Didn't manage to reproduce.")

        new_resistances = {}
        for key, value in self.resistances.items():
            new_value = value if random.random() <= 1 - self.mut_prob else not value
            new_resistances[key] = new_value

        return ResistantVirus(self.max_birth_prob,
                              self.clear_prob,
                              new_resistances,
                              self.mut_prob)

            

class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    active_drugs = []
    
    def __init__(self, viruses, max_pop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        max_pop: the  maximum virus population for this patient (an integer)
        """
        self.active_drugs = []
        super(Patient, self).__init__(viruses, max_pop)
    

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.active_drugs:
            self.active_drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.active_drugs
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistant_count = 0
        for virus in self.viruses:
            if all(map(virus.isResistantTo, drugResist)):
                resistant_count += 1
        return resistant_count
                   

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        survivors = []
        
        for virus in self.viruses:
            if not virus.doesClear():
                survivors.append(virus)

        population_density = len(survivors) / self.max_pop

        children = []
        for virus in survivors:
            try:
                child = virus.reproduce(population_density, self.active_drugs)
                children.append(child)
            except NoChildException:
                pass

        survivors.extend(children)
        self.viruses = survivors              
        return self.getTotalPop()


def run_trial_with_drug(admin_time):
    """
    Runs a drug simulation on a patient. Drug is introduced after 150 time
    steps.

    returns: a tuple containing two lists. The first list is the number of
    viruses at each time step. The second list is the number of drug resistant
    viruses at each time step.
    """
    # Initializing the population.
    max_birth_prob = 0.1
    clear_prob = 0.05
    resistances = {"guttagonol": False}
    mut_prob = 0.005
    viruses = [ResistantVirus(max_birth_prob, clear_prob, resistances, mut_prob) for i in range(100)]
    max_pop = 1000
    patient = Patient(viruses, max_pop)
    gut_resist_counts = []
    total_counts = []
    time_steps = numpy.arange(0, admin_time + 150)
    # Run simulation
    for time_step in time_steps:
        patient.update()
        # Introduce new drug /after/ 150 time steps.
        if time_step == admin_time:
            patient.addPrescription("guttagonol")

        # Compile data about the simulation
        gut_resist_counts.append(patient.getResistPop(["guttagonol"]))
        total_counts.append(patient.getTotalPop())
    return numpy.array(total_counts), numpy.array(gut_resist_counts)

#
# PROBLEM 2
#
def run_experiment_with_drug():
    """
    Runs and analyzes a number of trials with a drug. See problem  for details.

    Average number of virsues over time and average number of resistant viruses
    over time are plotted.
    """
    print("Starting exeriment.")
    admin_time = 150
    num_trials = 1000
    sum_of_total_counts = None
    sum_of_resist_counts = None
    
    print("Running trials...")
    for trial in range(num_trials):
        print "trial %s" % (trial)
        total_counts, gut_resist_counts = run_trial_with_drug(admin_time)
        if sum_of_total_counts is not None:
            sum_of_total_counts += total_counts
        else:
            sum_of_total_counts = total_counts
        if sum_of_resist_counts is not None:
            sum_of_resist_counts += gut_resist_counts
        else:
            sum_of_resist_counts = gut_resist_counts
    print("Finished running trials.")
    
    print("Contructing descriptive statistics...")
    mean_total_counts = sum_of_total_counts / num_trials
    mean_resist_counts = sum_of_resist_counts / num_trials
    pyplot.title("Average virus population over time in %s trials" % (num_trials))
    pyplot.xlabel("Time")
    pyplot.ylabel("Average virus population")
    time_steps = numpy.arange(1, 301)
    pyplot.plot(time_steps, mean_total_counts, "b.", label="All viruses")
    pyplot.plot(time_steps, mean_resist_counts, "r.", label="Guttagonol resistant viruses") 
    pyplot.legend(loc="lower right")
    pyplot.show()
    print("Descriptive statistics created.")
    print("Experiment completed.")
#run_experiment_with_drug()


#
# PROBLEM 3
#        
def run_delayed_treatment_experiment():
    """
    Runs simulations and make histograms for problem 3.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    admin_times = [0, 75, 150, 300]
    admin_time_counts = {}
    num_trials = 500
    for admin_time in admin_times:
        admin_time_counts[admin_time] = []
        for trial in range(num_trials):
            print "trial %s %s" % (admin_time, trial)
            # get the total count of virus particles at the end of the trial
            ending_virus_count = run_trial_with_drug(admin_time)[0][-1]
            admin_time_counts[admin_time].append(ending_virus_count)
        admin_time_counts[admin_time] = numpy.array(admin_time_counts[admin_time])

    for admin_time in admin_times:
        pyplot.figure()
        admin_time_count = admin_time_counts[admin_time]
        pyplot.hist(admin_time_count)
        mu = numpy.mean(admin_time_count)
        sigma = numpy.std(admin_time_count)
       
        # place a text box in the middle of the histogram
        textstr = '$\mu=%.2f$\n$\sigma=%.2f$'%(mu, sigma)
        xmin, xmax = pyplot.xlim()
        ymin, ymax = pyplot.ylim()
        pyplot.text(xmin+(xmax-xmin)/2,
                    ymin+(ymax-ymin)/2,
                    textstr) 
        pyplot.title("Drug given at T=%s" % (admin_time))
        pyplot.xlabel("Average population 150 steps after drug introduced")
        pyplot.ylabel("Number of samples within range")
        
    pyplot.show()
# run_delayed_treatment_experiment()

    

#
# PROBLEM 4
#
def run_trial_with_two_drug(admin_time, delay):
    """
    Runs a drug simulation on a patient. Drug is introduced after 150 time
    steps.

    returns: a tuple containing two lists. The first list is the number of
    viruses at each time step. The second list is the number of drug resistant
    viruses at each time step.
    """
    # Initializing the population.
    max_birth_prob = 0.1
    clear_prob = 0.05
    resistances = {"guttagonol": False, "gimpex": False}
    mut_prob = 0.005
    viruses = [ResistantVirus(max_birth_prob, clear_prob, resistances, mut_prob) for i in range(100)]
    max_pop = 1000
    patient = Patient(viruses, max_pop)
    resist_counts = []
    total_counts = []
    time_steps = numpy.arange(0, admin_time + delay + 150)
    # Run simulation
    for time_step in time_steps:
        patient.update()
        # Introduce new drug /after/ 150 time steps.
        if time_step == admin_time:
            patient.addPrescription("guttagonol")
        if time_step == admin_time + delay:
            patient.addPrescription("gimpex")

        # Compile data about the simulation
        resist_counts.append(patient.getResistPop(["guttagonol", "gimpex"]))
        total_counts.append(patient.getTotalPop())
    return numpy.array(total_counts), numpy.array(resist_counts)

def simulationTwoDrugsDelayedTreatment():
    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    admin_times = [0, 75, 150, 300]
    admin_time_counts = {}
    num_trials = 30
    for admin_time in admin_times:
        admin_time_counts[admin_time] = []
        for trial in range(num_trials):
            print "trial %s %s" % (admin_time, trial)
            # get the total count of virus particles at the end of the trial
            ending_virus_count = run_trial_with_drug(admin_time)[0][-1]
            admin_time_counts[admin_time].append(ending_virus_count)
        admin_time_counts[admin_time] = numpy.array(admin_time_counts[admin_time])

    for admin_time in admin_times:
        pyplot.figure()
        admin_time_count = admin_time_counts[admin_time]
        pyplot.hist(admin_time_count)
        mu = numpy.mean(admin_time_count)
        sigma = numpy.std(admin_time_count)
       
        # place a text box in the middle of the histogram
        textstr = '$\mu=%.2f$\n$\sigma=%.2f$'%(mu, sigma)
        xmin, xmax = pyplot.xlim()
        ymin, ymax = pyplot.ylim()
        pyplot.text(xmin+(xmax-xmin)/2,
                    ymin+(ymax-ymin)/2,
                    textstr) 
        pyplot.title("First drug given at T=%s" % (admin_time))
        pyplot.xlabel("Average population 150 steps after second drug introduced")
        pyplot.ylabel("Number of samples within range")
        
    pyplot.show()
#simulationTwoDrugsDelayedTreatment()




#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():
    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    time_steps = numpy.arange(0, 450)
    total, resistant = run_trial_with_two_drug(150, 150)
    pyplot.plot(time_steps, total, label="Total Virus Population")
    pyplot.plot(time_steps, resistant, label="Resistant Virus Population")
    pyplot.title("Virus Population Over Time w/ delay in medication")
    pyplot.legend()
    pyplot.figure()
    time_steps = numpy.arange(0, 300)
    total, resistant = run_trial_with_two_drug(150, 0)
    pyplot.plot(time_steps, total, label="Total Virus Population")
    pyplot.plot(time_steps, resistant, label="Resistant Virus Population")
    pyplot.title("Virus Population Over Time w/ no delay in medication")
    pyplot.legend()
    pyplot.show()
simulationTwoDrugsVirusPopulations()





