import logging

from fastapi import FastAPI


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s",
    handlers=[
        logging.FileHandler("logs/logs.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


app = FastAPI()
