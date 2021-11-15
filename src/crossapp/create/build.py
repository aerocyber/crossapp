# Copyright 2021 aerocyber
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import zipapp
import os
import json
import shutil

def buildFromSpec(spec):
    f = open(spec, 'r')
    spec = json.load(f)
    f.close()
    
    # Get src from spec
    src = spec['src']
    
    # Get name from spec
    name = spec["name"]
    
    out = shutil.copy2(src, spec["out"])
    zipapp.create_archive(out, name+spec["version"]+".pyz")
    
    # Create a base data.
    dat = {
        "version": spec["version"], 
        "appName": spec["appName"],
        "repo":    spec["repo"],
        "author":  spec["author"],
        "website": spec["website"],
        "appId":   spec["appId"],
        }
    
    d = open(os.path.join(os.path.dirname(spec), 'build'), (name+spec["version"]+".pyz"), 'rb')
    data = d.read()
    d.close()
    
    dat["Data"] = data
    
    f = open(os.path.join(spec["out"], name+spec["version"]+".cap"), 'w')
    return {
        "Status": "Done",
        "Detail": "Build Successful"
    }