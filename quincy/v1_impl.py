# Copyright (c) 2014 Dark Secret Software Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import uuid


class Event(object):
    def __init__(self, request_id, name):
        self.when = datetime.datetime.utcnow()
        self.name = name
        self.request_id = request_id
        self.message_id = str(uuid.uuid4())

    def to_dict(self):
        return {"when": str(self.when),
                "name": self.name,
                "request_id": self.request_id,
                "message_id": self.message_id}


class Impl(object):
    def get_events(self, resp):
        rid = str(uuid.uuid4())
        return [Event(rid, "scheduler.run_instance.start"),
                Event(rid, "scheduler.run_instanace.scheduled"),
                Event(rid, "scheduler.run_instance.end")]