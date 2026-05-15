from fastapi import FastAPI, Depends
from routing.auth_routing import router as auth_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from helpers.dependencies import get_current_user

app = FastAPI(title="Auth Service", version="1.0.0")

app.include_router(auth_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):

    errors = []

    for error in exc.errors():
        if "ctx" in error:
            error["ctx"] = {
                key: str(value)
                for key, value in error["ctx"].items()
            }
        errors.append(error)

    return JSONResponse(
        status_code=422,
        content={
            "detail": errors,
            "body": exc.body
        },
    )

@app.get("/", dependencies=[Depends(get_current_user)])
def read_root():
    return {"message": "Welcome to the Auth Service!"}