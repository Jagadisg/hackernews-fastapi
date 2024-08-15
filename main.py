import httpx
from cachetools import TTLCache
from fastapi import FastAPI, HTTPException,  Depends, Query


app = FastAPI()

news_cache = TTLCache(maxsize=100, ttl=600)


async def get_session():
    async with httpx.AsyncClient() as session:
        yield session


async def fetch_news_item(client: httpx.AsyncClient, item_id: int):
    if item_id in news_cache:
        return news_cache[item_id] 

    response = await client.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json")    
    response.raise_for_status()
    news_item = response.json()
    news_cache[item_id] = news_item 
    return None
        
        
@app.get("/top-news")
async def topnews(client: httpx.AsyncClient = Depends(get_session), count: int = Query(default=10, ge=1,le=500)):
    try:
        response = await client.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        response.raise_for_status()
        story_ids = response.json()[:count]
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Error fetching top stories") from e

    for item_id in story_ids:
        try:
            await fetch_news_item(client,item_id)
        except httpx.HTTPError as e:
            print(f"Error fetching news {item_id}: {e}")
            continue

    return news_cache