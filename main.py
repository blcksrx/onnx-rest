#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os

from fastapi import FastAPI
from onnxruntime import InferenceSession

from api import router
from models import MODELS

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def load_models() -> None:
    for file in os.listdir("models"):
        if file.endswith(".onnx"):
            model = InferenceSession("models/" + file)
            metadata = {
                "input": [
                    {"name": x.name, "type": x.type, "shape": x.shape}
                    for x in model.get_inputs()
                ],
                "output": [
                    {"name": x.name, "type": x.type, "shape": x.shape}
                    for x in model.get_outputs()
                ],
            }
            MODELS[file.replace(".onnx", "")] = {
                "name": file,
                "model": model,
                "metadata": metadata,
            }
