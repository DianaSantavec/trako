class Data(object):
    def __init__(self, project, subproject, description, time_estimate, due_date, status, work_time):
        self.project = project
        self.subproject = subproject
        self.description = description
        self.time_estimate = time_estimate
        self.due_date = due_date
        #status - TO DO, DOING, DONE
        self.status = status
        self.work_time = work_time
    
    def getData(self):
        return [self.project, self.subproject, self.description, self.time_estimate, self.due_date, self.status, self.work_time]

    