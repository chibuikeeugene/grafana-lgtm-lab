import logging
import json
import time
import asyncio
from fastapi import FastAPI, HTTPException, Request
from prometheus_client import Counter, Histogram, make_asgi_app


# create a fastapi object
app = FastAPI(title="NovaRetail Order API")

# creating application metrics
# count each coming http requests
REQUEST_COUNT = Counter("http_requests_total", "Total number of http requests", ["method", "endpoint", "status_code"])

# calculate how long requests takes using histogram
REQUEST_DURATION = Histogram("http_request_duration_seconds", "HTTP requests processing duration", ["endpoint"])

# setting up application logger
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("order-api")

# define a middleware
# record metrics and structured json logs using middleware
@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.perf_counter()
    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response

    finally:
        duration = time.perf_counter() - start_time
        endpoint = request.url.path

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=endpoint,
            status_code=str(status_code),
        ).inc()

        REQUEST_DURATION.labels(
            endpoint=endpoint,
        ).observe(duration)

        logger.info(json.dumps({
            "service": "order-api",
            "method": request.method,
            "endpoint": endpoint,
            "status_code": status_code,
            "duration_seconds": round(duration, 4),
            "service_version": 2
        }))


#1. Get app health
@app.get("/health")
def health():
    return {"status": "healthy"}

#2. Get orders 
@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {"id":1, "status": "completed"},
            {"id":2, "status": "pending"}
        ]
    }
#3. Get simulated order error
@app.get("/orders/error")
def generate_error():
    raise HTTPException(
        status_code=500,
        detail="Simualated database failure"
    )

#4. simulating slow order endpoint
@app.get('/orders/slow')
async def slow_order():
    await asyncio.sleep(2)
    return {"message": "Order processed after a 2-second delay"}

# Prometheus metrics endpoint
app.mount("/metrics", make_asgi_app())