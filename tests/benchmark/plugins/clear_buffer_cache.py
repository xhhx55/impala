#!/usr/bin/env python
# Copyright (c) 2012 Cloudera, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tests.util.cluster_controller import ClusterController
from tests.benchmark.plugins import Plugin

class ClearBufferCache(Plugin):
  """Plugin that clears the buffer cache before a query is run."""

  __name__ = "ClearBufferCache"

  def __init__(self, *args, **kwargs):
    self.cluster_controller = ClusterController(*args, **kwargs)
    Plugin.__init__(self, *args, **kwargs)

  def run_pre_hook(self, context=None):
    try:
      cmd = "sysctl -w vm.drop_caches=3 vm.drop_caches=0"
      self.cluster_controller.run_cmd(cmd)
    except Exception as e:
      print "Could not run command: %s" % cmd
