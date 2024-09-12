if __name__ == "__main__":
    import uvicorn
    from .logging import logger

    config = uvicorn.Config(app="navegavo.asgi:app", host="0.0.0.0", port=8000)
    server = uvicorn.Server(config=config)

    try:
        server.run()
    except Exception as e:
        logger.exception(e)
