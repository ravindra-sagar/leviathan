indian-laws-rag-pipeline/
│
├── .github/
│   ├── workflows/
│   │   ├── ci-cd.yml          # CI/CD pipeline
│   │   ├── tests.yml          # Automated testing
│   │   └── security-scan.yml  # Security checks
│   └── pull_request_template.md
│
├── config/
│   ├── __init__.py
│   ├── settings.py            # Main configuration
│   ├── environments/
│   │   ├── development.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   └── logging_config.yaml    # Logging configuration
│
├── data/
│   ├── raw/
│   │   ├── acts/              # Raw legal acts/statutes
│   │   ├── case_laws/         # Court judgments
│   │   ├── amendments/        # Legal amendments
│   │   └── rules_regulations/ # Rules & notifications
│   ├── processed/
│   │   ├── cleaned/           # Cleaned documents
│   │   ├── chunked/           # Text chunks for RAG
│   │   └── embeddings/        # Generated embeddings
│   ├── ontology/
│   │   ├── legal_ontology.ttl # OWL/RDF ontology
│   │   ├── taxonomy.json      # Legal hierarchy
│   │   └── metadata_schema.yaml # Document metadata schema
│   └── scripts/
│       ├── data_collector.py  # Web scraping/data collection
│       ├── data_cleaner.py    # Data preprocessing
│       └── ontology_builder.py # Ontology construction
│
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── document_processor.py
│   │   ├── chunking_strategies.py
│   │   ├── embedding_service.py
│   │   └── ontology_manager.py
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── vector_store.py    # Vector DB operations
│   │   ├── retriever.py       # Hybrid retrieval
│   │   ├── reranker.py        # Result reranking
│   │   └── semantic_search.py
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── llm_handler.py     # LLM abstraction
│   │   ├── prompt_templates/
│   │   │   ├── legal_qa.yaml
│   │   │   ├── summarization.yaml
│   │   │   └── comparison.yaml
│   │   └── response_formatter.py
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── drift_detection.py
│   │   ├── performance_tracker.py
│   │   └── alert_manager.py
│   └── api/
│       ├── __init__.py
│       ├── main.py            # FastAPI/FastAPI app
│       ├── routes/
│       │   ├── query.py       # Query endpoint
│       │   ├── ingestion.py   # Data ingestion endpoint
│       │   └── monitoring.py  # Monitoring endpoints
│       ├── schemas/           # Pydantic models
│       └── middleware/        # Auth, rate limiting
│
├── infrastructure/
│   ├── docker/
│   │   ├── Dockerfile.api
│   │   ├── Dockerfile.processor
│   │   └── docker-compose.yaml
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── network/
│   │   │   ├── compute/
│   │   │   └── database/
│   │   └── environments/
│   │       ├── dev/
│   │       ├── staging/
│   │       └── prod/
│   └── kubernetes/
│       ├── manifests/
│       └── helm-charts/
│
├── tests/
│   ├── unit/
│   │   ├── test_document_processor.py
│   │   ├── test_retriever.py
│   │   └── test_llm_handler.py
│   ├── integration/
│   │   ├── test_api_endpoints.py
│   │   └── test_data_pipeline.py
│   ├── e2e/
│   │   └── test_rag_pipeline.py
│   └── fixtures/              # Test data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_ontology_development.ipynb
│   ├── 03_embedding_evaluation.ipynb
│   └── 04_prompt_engineering.ipynb
│
├── docs/
│   ├── architecture.md
│   ├── api_documentation.md
│   ├── data_sources.md
│   ├── deployment_guide.md
│   └── ontology_specification.md
│
├── scripts/
│   ├── setup_environment.sh
│   ├── run_etl_pipeline.sh
│   ├── deploy.sh
│   └── monitor_health.sh
│
├── .env.example               # Environment variables template
├── .gitignore
├── .pre-commit-config.yaml    # Code quality hooks
├── pyproject.toml             # Python dependencies & config
├── Makefile                   # Common commands
├── README.md                  # Project overview
├── CONTRIBUTING.md
├── LICENSE
└── requirements/
    ├── base.txt              # Core dependencies
    ├── dev.txt               # Development dependencies
    └── prod.txt              # Production dependencies