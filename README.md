# ONNX-REST

A **simple** and **fast** Rest API for productionization the ONNX models.

![travic-ci](https://travis-ci.org/blcksrx/onnx-rest.svg?branch=master)

## How to use?
Simply **clone** this repository and  copy your **ONNX** models into the `models` directory and just run the project with **uvicorn**!
The rest api docs are presents in the `/docs` path

1. `git clone git@github.com:blcksrx/onnx-rest.git`
2. `cd onnx-rest`
3. `pip install -r requirements.txt`
4. `uvicorn main:app`
5.  verify the project is running well:
   ```
   $ curl localhost:8000/actuator/health
   {"Status": "Up"}
```

## Contributing |

Wanna help? Just fork it and create PRs!