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

from fastapi import APIRouter
from fastapi.responses import Response

actuator_api = APIRouter()


@actuator_api.get("/health")
async def health() -> Response:
    return Response(
        content=json.dumps({"Status": "Up"}),
        status_code=200,
        headers={"content-type": "application/json"},
    )


@actuator_api.get("/info")
async def info() -> Response:
    return Response(
        content=json.dumps({
            "name": "ONNX Runtime Scoring Server",
            "version": "dev"
        }),
        status_code=200,
        headers={"content-type": "application/json"},
    )
