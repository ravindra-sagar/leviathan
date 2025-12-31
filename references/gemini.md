justice-rag-india/
├── .github/                  # CI/CD workflows (GitHub Actions)
├── assets/                   # Architecture diagrams and demo GIFs
├── config/                   # Configuration files (YAML/TOML)
│   ├── model_config.yaml     # LLM parameters, embedding models
│   └── database_config.yaml  # Vector DB and Neo4j settings
├── data/                     # (Gitignored) Raw and processed data
│   ├── raw/                  # Original PDFs/Scraped HTML
│   └── processed/            # Cleaned markdown/JSON for ingestion
├── deployment/               # Cloud infrastructure files
│   ├── docker/               # Dockerfile and docker-compose
│   └── terraform/            # Infrastructure as Code (AWS/Azure/GCP)
├── notebooks/                # EDA, prompt prototyping, and experiments
├── scripts/                  # One-off scripts (e.g., DB migration, data scraping)
├── src/                      # Core application logic
│   ├── __init__.py
│   ├── ingestion/            # Scrapers, OCR, and cleaning logic
│   ├── ontology/             # Knowledge Graph construction (Neo4j) logic
│   ├── indexing/             # Chunking and Vector DB upserts
│   ├── retrieval/            # Hybrid search (Vector + Keyword + Graph)
│   ├── generation/           # LLM chains and prompt engineering
│   └── api/                  # FastAPI/Flask entry points
├── tests/                    # Unit, integration, and RAG evaluation tests
├── .env.example              # Template for environment variables
├── pyproject.toml            # Modern python dependency management
└── README.md                 # Project documentation