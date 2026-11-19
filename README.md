
### Base app function:

- Counter counts incoming HTTP requests.
- Histogram measures how long requests take.
- Middleware records metrics and structured JSON logs.
- /health simulates an application health endpoint.
- /orders returns successful responses.
- /orders/error simulates an HTTP 500 incident.
- /metrics exposes Prometheus-formatted metrics.

### Service-port table function

| Service    | Purpose                    | Localaddress                     |
| ---------- | -------------------------- | -------------------------------- |
| Grafana    | Dashboardsandinvestigation | `<span>localhost:3000</span>`  |
| Loki       | Logsbackend                | Internalport3100                 |
| Prometheus | Metricsbackend             | `<span>localhost:9090</span>`  |
| Tempo      | Tracesbackend              | Internalport3200                 |
| Alloy      | Telemetrycollection        | `<span>localhost:12345</span>` |
| FastAPI    | Applicationbeingmonitored  | `<span>localhost:8000</span>`  |
