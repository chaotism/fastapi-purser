"""
Here you should do all needed actions. Standart configuration of docker container
will run your application with this file.
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
