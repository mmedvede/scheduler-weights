# Copyright (c) 2011 OpenStack Foundation
# Copyright (c) 2015 IBM
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Instance Weigher.  Weigh hosts by number of instances they have. Host with
less instances would have larger weight.
"""

from nova.scheduler import weights


class InstanceWeigher(weights.BaseHostWeigher):
    minval = 0

    def _weigh_object(self, host_state, weight_properties):
        """Higher weights win. Spread by default."""
        # [mmedvede]: Returning negated num_instances should suffice, as they
        # would get normalized anyway.
        return -host_state.num_instances
