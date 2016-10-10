OpenStack Scheduler Weights
===========================

To install, git clone, and then `pip install scheduler-weights`. This should be
done on the machine that runs Nova Scheduler service. Normally your controller
node.


Implemented Weights
-------------------

### Instance Count
Assign most weight to a host with the least number of instances on it.

_nova.conf_:

    [DEFAULT]
    scheduler_weight_classes=scheduler-weights.nova.scheduler.weights.instance.InstanceWeigher
