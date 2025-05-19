from fastapi import FastAPI
from app.database.config import test_connection
from app.routes import signupRoute
from app.routes import loginRoute


app = FastAPI()

# 👇 include the router with a prefix
app.include_router(signupRoute.router, prefix="/api")
app.include_router(loginRoute.router,prefix='/api')

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

if __name__ == "__main__":
    test_connection()
