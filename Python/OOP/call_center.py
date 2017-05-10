from time import localtime, strftime, sleep
import itertools # to keep count of each class created, which will in turn be used for the id

class Call(object):
    _id = itertools.count(0)
    def __init__(self, caller_name, caller_phone_number = None, reason = None, time = strftime("%Y-%m-%d %H:%M:%S", localtime())):
        self.name = caller_name
        self.phone_number = caller_phone_number
        self.time = time
        self.reason = reason
        self.id = self._id.next()

    # will display all information about the caller
    def display_info(self):
        print self.id
        print 'Name:', self.name
        print 'Phone Number:', self.phone_number
        print 'Time of call:', self.time
        print 'Reason for call:', self.reason
        print '-' * 20

class Call_Center(object):
    """queue which will maintain all incoming calls and remove them as needed"""
    def __init__(self, calls = None):
        if calls == None:
            self.calls = []
        else:
            self.calls = calls
        self.queue_size = len(self.calls)

    # adds new calls made to the current list aka call queue
    def add(self, new_call):
        if new_call not in self.calls:
            self.calls.append(new_call)
            print new_call.name, 'has been added to the call queue'
        else:
            print new_call.name, 'is already in the call queue'
        return self

    # removes the first call from our list aka call queue
    def remove(self):
        print 'Removed first caller from queue'
        del self.calls[0]
        return self

    # removes the caller from our call list given their phone number
    def remove_by_phone(self, phone_number):
        for caller in self.calls:
            if phone_number == caller.phone_number:
                self.calls.remove(caller)
                print 'Caller with number', caller.phone_number, 'has been removed from queue'
        return self

    # sorts our call list in ascending order from the call timestamps
    def sort_call_lst(self):
        self.calls.sort(key=lambda x: x.time)
        print 'Queue has been sorted from oldest to most recent caller'
        return self

    # will print out each caller in the queue showing name and number
    def info(self):
        print ''
        print '---This is the current queue of callers by name and phone number---'
        for caller in self.calls:
            print caller.name, caller.phone_number
        print ''
        return self

call1= Call('Junior', '123-456-7890', 'Robbery', '2017-05-09 23:38:49') # manually set time to test sort later
call2= Call('Help')

call1.display_info()
call2.display_info()

call3= Call('Spiderman', '888-888-8888', 'Bit by spider')


calls= [call3,call2,call1] # added callers to list in reverse order of time called, sort method should correct it

hospital = Call_Center(calls)

hospital.info()

hospital.sort_call_lst()

hospital.info().remove_by_phone('123456').info().add(call3).remove().info()
