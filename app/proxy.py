import asyncio

from fastapi import APIRouter, status, Request
from sse_starlette.sse import EventSourceResponse

r = APIRouter()

STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # millisecond


@r.get('/events', responses={
    status.HTTP_200_OK: {
        "descriptions": 'hello',
        'content': {
            'text/event-stream': {
                "examples": {
                    'new_message': {
                        'summary': '',
                        'value': {
                            "event": "new_message",
                            "id": "message_id",
                            "retry": RETRY_TIMEOUT,
                            "data": "Counter value {'counter'}",
                        }

                    },
                    'something': {
                        'summary': '',
                        'value': {
                            "event": "new_message",
                            "id": "message_id",
                            "retry": RETRY_TIMEOUT,
                            "data": "Counter value {'counter'}",
                        }

                    }
                }
            }
        }

    }
})
async def events(request: Request):
    async def stream():
        while True:
            if await request.is_disconnected():
                break

            yield {
                "event": "new_message",
                "retry": RETRY_TIMEOUT,
                "data": "Counter value {'counter'}",
            }
            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(stream())
