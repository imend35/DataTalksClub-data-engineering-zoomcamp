{{ config(
    materialized='table',
    partition_by={
      "field": "created_at",
      "data_type": "timestamp"
    },
    cluster_by=["language","subject"]
) }}

SELECT
   *
FROM `braided-keel-490209-q8.ai_open_source_dw.ai_repositories`
