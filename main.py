import time
import datetime


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():
    name = None
    priority = -1
    period = -1
    execution_time = -1
    last_deadline = -1
    last_execution_time = None

    ############################################################################
    def __init__(self, name, priority, period, execution_time, last_execution):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution

    ############################################################################
    def run(self):
        # Update last_execution_time

        self.last_execution_time = datetime.datetime.now()

        print("\t" + self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")

        time.sleep(self.execution_time)

        print("\t" + self.name + " : Ending task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = []
    task_list.append(my_task(name="thread_1", priority=1, period=20, execution_time=10, last_execution=last_execution))
    task_list.append(my_task(name="thread_2", priority=1, period=30, execution_time=5, last_execution=last_execution))
    task_list.append(my_task(name="thread_3", priority=1, period=60, execution_time=20, last_execution=last_execution))

    while (1):

        time_now = datetime.datetime.now()

        print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))

        # Find the task with Earliest deadline

        task_to_run = None
        earliest_deadline = time_now + datetime.timedelta(hours=1)  # Init ... not perfect but will do the job

        for current_task in task_list:

            current_task_next_deadline = current_task.last_execution_time + datetime.timedelta(seconds=current_task.period)

            print("\tDeadline for task " + current_task.name + " : " + current_task_next_deadline.strftime("%H:%M:%S"))

            if (current_task_next_deadline < earliest_deadline):
                earliest_deadline = current_task_next_deadline
                task_to_run = current_task

        # Start task
        task_to_run.run()
        #modification test