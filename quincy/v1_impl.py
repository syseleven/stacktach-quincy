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


class Stream(object):
    def __init__(self, stream_id, trigger_name, state):
        self.last_updated = datetime.datetime.utcnow()
        self.stream_id = stream_id
        self.trigger_name = trigger_name
        self.state = state

    def to_dict(self):
        return {"last_updated": str(self.last_updated),
                "stream_id": self.stream_id,
                "trigger_name": self.trigger_name,
                "state": self.state}


class Impl(object):
    def get_stream(self, resp):
        sid = str(uuid.uuid4())
        return [Stream(sid, "EOD-Exists", "Collecting")
                Stream(sid, "EOD-Exists", "Error")
                Stream(sid, "Request-ID", "Ready")]
