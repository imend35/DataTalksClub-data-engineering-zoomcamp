SELECT
    subject ,
    COUNT(DISTINCT repo_name) AS repo_count
FROM {{ ref('stg_ai_repositories') }}
GROUP BY subject
ORDER BY repo_count DESC
