# Monitoring Stack: Prometheus + Grafana + Alerting

Observability lab for portfolio:
- Prometheus scrapes node-exporter and cAdvisor
- Grafana with provisioned datasource
- Alert rules for instance down / high CPU

## Start
```bash
docker compose up -d
open http://localhost:3000   # admin / admin_change_me
open http://localhost:9090   # Prometheus
```

## Skills shown
metrics, dashboards, alert design, container observability
