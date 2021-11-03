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

import os
import json

def create_dir(path):
    dirs = ["bin", "build", "src", "test"]
    for d in dirs:
        os.makedirs(os.path.join(path, d), exist_ok=True)


def create_spec(path, name, version, description, author, license, url, src_dir, output_dir):
    spec = {
        "name": name,
        "version": version,
        "description": description,
        "author": author,
        "license": license,
        "url": url,
        "src": src_dir,
        "out": output_dir
    }
    with open(os.path.join(path, "package.json"), "w") as f:
        json.dump(spec, f, indent=4)
    
