if __name__ == "__main__":
    import uvicorn
    from .logging import logger
    import os

    config = uvicorn.Config(app="navegavo.asgi:app", host="0.0.0.0", port=8000)
    server = uvicorn.Server(config=config)

    try:
        os.system("clear" if os.name != "nt" else "cls")
        server.run()
    except Exception as e:
        logger.exception(e)
