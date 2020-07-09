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

import json
import os

import numpy as np
from fastapi import APIRouter, Request
from fastapi.responses import Response

from models import MODELS

model_api = APIRouter()


@model_api.get("/")
async def model_list() -> Response:
    return Response(
        content=json.dumps({"models": list(MODELS.keys())}),
        status_code=200,
        headers={"content-type": "application/json"},
    )


@model_api.get("/{model_name}/metadata")
async def model_metadata(model_name: str) -> Response:
    if model_name not in os.listdir("models"):
        return Response(
            content=json.dumps({
                "message": "this model does not exists in the server"
            }),
            status_code=404,
            headers={"content-type": "application/json"}
        )
    return Response(
        content=json.dumps(
            {
                "name": MODELS[model_name]["name"],
                "metadata": MODELS[model_name]["metadata"],
            }
        ),
        status_code=200,
        headers={"content-type": "application/json"},
    )


@model_api.post("/{model_name}/predict")
async def predict(model_name: str, request: Request) -> Response:
    if model_name not in os.listdir("models"):
        return Response(
            content=json.dumps({
                "message": "this model does not exists in the server"
            }),
            status_code=404,
            headers={"content-type": "application/json"}
        )
    data = await request.json()
    for key, value in data.items():
        data[key] = [np.array([value], dtype=np.float32)]

    model = MODELS[model_name]["model"]
    run = model.run(["probability", "prediction"], data)

    return Response(
        content=json.dumps(
            {
                "probability": list(run[0][0].astype(float)),
                "prediction": list(run[1].astype(float))[0],
            }
        ),
        status_code=200,
        headers={"content-type": "application/json"},
    )
