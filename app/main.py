import asyncio
from typing import Any, List, Optional

import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from scheme import GetPage, InfoMessage, PageOut


class PageDownloader:
    """Aiohttp client as singleton to better utlize resources in async mode.

    Before running we should setup our clinet by invoking `get_client` that would
    set class level client which can be used in other places before closing session.
    After finishing our jobs we should close client by invoking `close_client`.

    Example:
        PageDownloader.get_client()
        PageDownloader.get_page(...)
        PageDownloader.get_page(...)
        ...
        PageDownloader.close_client()


    """

    client: Optional[aiohttp.ClientSession] = None
    size: int = 5

    @classmethod
    def get_client(cls) -> aiohttp.ClientSession:
        if cls.client is None:
            timeout = aiohttp.ClientTimeout(total=2)
            connector = aiohttp.TCPConnector(verify_ssl=False, limit_per_host=cls.size)
            cls.client = aiohttp.ClientSession(timeout=timeout, connector=connector)
        return cls.client

    @classmethod
    async def close_client(cls) -> None:
        if cls.client:
            await cls.client.close()
            cls.client = None

    @classmethod
    async def get_page(cls, page: GetPage) -> Any:
        """Gets page content
        If given resource is a API - json-like object will be returend in case of regular web page -> body of response
        In case of any error instead of regular reponse with {"contnet": ...}
        additional key would be present  "error" containing error message for
        future debuging.

        """
        url = page.url
        client = cls.get_client()
        try:
            async with client.get(url) as response:
                if response.status != 200:
                    return {"error": str(await response.text()), "content": None}
                content = await response.json()
        except aiohttp.ContentTypeError:
            content = await response.text()
        except Exception as e:
            return {"error": e, "content": None}

        return {"content": content}


async def on_startup() -> None:
    PageDownloader.get_client()


async def on_shutdown() -> None:
    await PageDownloader.close_client()


app = FastAPI(
    description="CISCO Assignment API helps you do awesome stuff. 🚀",
    version="0.0.1",
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
    contact={
        "name": "Rafal Kesik",
        "url": "https://www.linkedin.com/in/rafalkesik/",
        "email": "rafal.kesik@gmail.com",
    },
)


@app.get("/")
async def docs_page_redirection(request: Request) -> RedirectResponse:
    """Redirection to a docs page"""
    return RedirectResponse(url="/docs")


@app.post("/ping")
async def download_page(page: GetPage) -> PageOut:
    """Downloads a page content as a string"""
    content = await PageDownloader.get_page(page)
    return content


@app.post("/pings")
async def download_pages(pages: List[GetPage]) -> List[PageOut]:
    """Downloads many pages content as a string"""
    tasks = []
    for page in pages:
        task = asyncio.create_task(PageDownloader.get_page(page))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


@app.get("/info")
async def info() -> InfoMessage:
    """Returns message"""
    return {"Receiver": "Cisco is the best!"}


if __name__ == "__main__":
    import uvicorn  # noqa

    uvicorn.run(app, port=8001, host="0.0.0.0")
