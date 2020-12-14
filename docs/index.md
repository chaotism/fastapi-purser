# FastAPI Tortoise

Here I was tried to describe how to use it and that ideas I followed when was creating it.

## Main ideas

    * All typed.
    I very like modern Python. Python with type-hints. It let to you write a code that will be understood by everybody.
    * All tested.
    I'm a big fan of TDD ideas. I have tried to test all components in this project.
    * Respects to OpenAPI ideas.
    OpenAPI schema is great thing, really. When I was creating it I was hoping that you will use the OpenAPI capatibilites which FastAPI provides to you fully.
    * Easy to deploy.
    No comments.

## The project structure

`application/main_web.py` file for start server instead `uvicorn` load.
`application/dbs` folder for db adapters.
`application/domain` folder for business logic of application.
`application/server` folder for web server logic of application.
`application/tests` folder for tests.
