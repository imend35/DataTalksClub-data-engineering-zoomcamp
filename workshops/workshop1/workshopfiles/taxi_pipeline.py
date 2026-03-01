import dlt
from dlt.sources.rest_api import rest_api_source


def nyc_taxi_source():
    """
    dlt REST API source for the NYC taxi demo API.

    The API returns paginated JSON with 1,000 records per page (server-side cap).
    Pagination is controlled via the `page` query parameter and
    stops when an empty page is returned.
    """
    config = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/",
        },
        "resources": [
            {
                "name": "nyc_taxi_trips",
                "columns": {
                    "rate_code": {"data_type": "text"},
                    "mta_tax": {"data_type": "double"},
                },
                "endpoint": {
                    "path": "data_engineering_zoomcamp_api",
                    "params": {
                        "limit": 1000,
                    },
                "paginator": {
                    "type": "page_number",
                    "page_param": "page",
                    "base_page": 1,
                    "total_path": None,
                    "stop_after_empty_page": True,
                    },
                },
            },
        ],
    }

    return rest_api_source(config, name="nyc_taxi")


def taxi_pipeline():
    """Build and run the NYC taxi pipeline."""
    pipeline = dlt.pipeline(
        pipeline_name="nyc_taxi_pipeline",
        destination="duckdb",
        dataset_name="nyc_taxi",
        progress="log",
    )
    source = nyc_taxi_source()
    return pipeline.run(source)


if __name__ == "__main__":
    print("Starting NYC taxi pipeline...", flush=True)
    load_info = taxi_pipeline()
    print(load_info, flush=True)


