# Indian Laws RAG Pipeline - Project Structure

A production-grade RAG (Retrieval-Augmented Generation) system for Indian legal documents.

```
indian-laws-rag/
│
├── README.md                          # Project overview, setup, architecture diagrams
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── Makefile                           # Common commands (setup, test, deploy, lint)
├── pyproject.toml                     # Python project config (dependencies, tools)
├── docker-compose.yml                 # Local development stack
├── docker-compose.prod.yml            # Production stack
├── .env.example                       # Environment variables template
├── .gitignore
├── .pre-commit-config.yaml            # Pre-commit hooks (linting, formatting)
│
├── docs/                              # Documentation
│   ├── architecture/
│   │   ├── system-design.md           # High-level architecture
│   │   ├── data-flow.md               # Data pipeline diagrams
│   │   └── decisions/                 # Architecture Decision Records (ADRs)
│   │       ├── 001-vector-db-choice.md
│   │       ├── 002-embedding-model.md
│   │       └── 003-chunking-strategy.md
│   ├── ontology/
│   │   ├── schema.md                  # Ontology documentation
│   │   ├── entities.md                # Entity definitions
│   │   └── relationships.md           # Relationship types
│   ├── api/
│   │   └── openapi.yaml               # API specification
│   └── runbooks/
│       ├── deployment.md
│       ├── troubleshooting.md
│       └── incident-response.md
│
├── src/                               # Main source code
│   ├── __init__.py
│   │
│   ├── config/                        # Configuration management
│   │   ├── __init__.py
│   │   ├── settings.py                # Pydantic settings (env-based config)
│   │   ├── logging_config.py
│   │   └── constants.py
│   │
│   ├── data_collection/               # Data ingestion layer
│   │   ├── __init__.py
│   │   ├── scrapers/
│   │   │   ├── __init__.py
│   │   │   ├── base_scraper.py        # Abstract base class
│   │   │   ├── india_code.py          # indiacode.nic.in scraper
│   │   │   ├── supreme_court.py       # Supreme Court judgments
│   │   │   ├── high_courts.py         # High Court judgments
│   │   │   └── gazette.py             # Government gazette
│   │   ├── parsers/
│   │   │   ├── __init__.py
│   │   │   ├── pdf_parser.py
│   │   │   ├── html_parser.py
│   │   │   └── doc_parser.py
│   │   ├── validators/
│   │   │   ├── __init__.py
│   │   │   └── document_validator.py
│   │   └── schedulers/
│   │       ├── __init__.py
│   │       └── ingestion_scheduler.py # Airflow/Prefect DAGs
│   │
│   ├── ontology/                      # Ontology & knowledge graph
│   │   ├── __init__.py
│   │   ├── schema/
│   │   │   ├── __init__.py
│   │   │   ├── legal_entities.py      # Pydantic models for entities
│   │   │   ├── relationships.py
│   │   │   └── indian_law_ontology.ttl # RDF/OWL ontology file
│   │   ├── extractors/
│   │   │   ├── __init__.py
│   │   │   ├── entity_extractor.py    # NER for legal entities
│   │   │   ├── citation_extractor.py  # Extract case/statute citations
│   │   │   └── metadata_extractor.py
│   │   └── graph/
│   │       ├── __init__.py
│   │       ├── neo4j_client.py        # Graph DB operations
│   │       └── graph_builder.py
│   │
│   ├── processing/                    # Document processing pipeline
│   │   ├── __init__.py
│   │   ├── chunking/
│   │   │   ├── __init__.py
│   │   │   ├── base_chunker.py
│   │   │   ├── semantic_chunker.py    # Meaning-based chunking
│   │   │   ├── legal_chunker.py       # Section/article aware chunking
│   │   │   └── hierarchical_chunker.py
│   │   ├── embeddings/
│   │   │   ├── __init__.py
│   │   │   ├── embedding_service.py   # Abstract embedding interface
│   │   │   ├── openai_embeddings.py
│   │   │   ├── cohere_embeddings.py
│   │   │   └── local_embeddings.py    # Sentence transformers
│   │   └── enrichment/
│   │       ├── __init__.py
│   │       ├── metadata_enricher.py
│   │       └── cross_reference_linker.py
│   │
│   ├── vectorstore/                   # Vector database layer
│   │   ├── __init__.py
│   │   ├── base_store.py              # Abstract interface
│   │   ├── pinecone_store.py
│   │   ├── weaviate_store.py
│   │   ├── qdrant_store.py
│   │   └── pgvector_store.py
│   │
│   ├── retrieval/                     # Retrieval strategies
│   │   ├── __init__.py
│   │   ├── retrievers/
│   │   │   ├── __init__.py
│   │   │   ├── base_retriever.py
│   │   │   ├── dense_retriever.py     # Vector similarity
│   │   │   ├── sparse_retriever.py    # BM25/keyword
│   │   │   ├── hybrid_retriever.py    # Dense + sparse fusion
│   │   │   └── graph_retriever.py     # Knowledge graph traversal
│   │   ├── rerankers/
│   │   │   ├── __init__.py
│   │   │   ├── cross_encoder.py
│   │   │   └── cohere_reranker.py
│   │   └── query_processing/
│   │       ├── __init__.py
│   │       ├── query_expander.py      # Query expansion
│   │       ├── query_router.py        # Route to appropriate retriever
│   │       └── legal_query_parser.py  # Parse legal terminology
│   │
│   ├── generation/                    # LLM generation layer
│   │   ├── __init__.py
│   │   ├── llm_clients/
│   │   │   ├── __init__.py
│   │   │   ├── base_client.py
│   │   │   ├── openai_client.py
│   │   │   ├── anthropic_client.py
│   │   │   └── bedrock_client.py
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   ├── templates/
│   │   │   │   ├── legal_qa.yaml
│   │   │   │   ├── case_summary.yaml
│   │   │   │   ├── statute_explanation.yaml
│   │   │   │   └── citation_check.yaml
│   │   │   └── prompt_manager.py
│   │   ├── chains/
│   │   │   ├── __init__.py
│   │   │   ├── rag_chain.py           # Main RAG chain
│   │   │   ├── multi_step_chain.py    # Complex reasoning
│   │   │   └── citation_chain.py      # Citation verification
│   │   └── guardrails/
│   │       ├── __init__.py
│   │       ├── input_validator.py
│   │       ├── output_validator.py
│   │       └── legal_safety.py        # Legal-specific safeguards
│   │
│   ├── api/                           # API layer
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI app entry
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── query.py               # /query endpoints
│   │   │   ├── documents.py           # Document management
│   │   │   ├── health.py              # Health checks
│   │   │   └── admin.py               # Admin operations
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── rate_limiter.py
│   │   │   └── request_logging.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── requests.py
│   │   │   └── responses.py
│   │   └── dependencies.py
│   │
│   └── utils/                         # Shared utilities
│       ├── __init__.py
│       ├── text_utils.py
│       ├── date_utils.py
│       ├── cache.py                   # Redis caching utilities
│       └── metrics.py                 # Custom metrics
│
├── pipelines/                         # Data/ML pipelines
│   ├── __init__.py
│   ├── airflow/                       # Airflow DAGs (if using Airflow)
│   │   ├── dags/
│   │   │   ├── daily_ingestion.py
│   │   │   ├── weekly_reindex.py
│   │   │   └── quality_check.py
│   │   └── plugins/
│   └── prefect/                       # Prefect flows (alternative)
│       └── flows/
│           ├── ingestion_flow.py
│           └── processing_flow.py
│
├── infrastructure/                    # Infrastructure as Code
│   ├── terraform/
│   │   ├── environments/
│   │   │   ├── dev/
│   │   │   │   ├── main.tf
│   │   │   │   ├── variables.tf
│   │   │   │   └── terraform.tfvars
│   │   │   ├── staging/
│   │   │   └── prod/
│   │   ├── modules/
│   │   │   ├── vpc/
│   │   │   ├── eks/                   # Kubernetes cluster
│   │   │   ├── rds/                   # PostgreSQL
│   │   │   ├── elasticache/           # Redis
│   │   │   ├── s3/                    # Document storage
│   │   │   └── monitoring/
│   │   └── backend.tf
│   │
│   ├── kubernetes/
│   │   ├── base/
│   │   │   ├── namespace.yaml
│   │   │   ├── configmap.yaml
│   │   │   ├── secrets.yaml
│   │   │   └── service-account.yaml
│   │   ├── apps/
│   │   │   ├── api/
│   │   │   │   ├── deployment.yaml
│   │   │   │   ├── service.yaml
│   │   │   │   ├── hpa.yaml           # Horizontal pod autoscaler
│   │   │   │   └── ingress.yaml
│   │   │   ├── worker/
│   │   │   └── scheduler/
│   │   └── kustomization.yaml
│   │
│   └── docker/
│       ├── api.Dockerfile
│       ├── worker.Dockerfile
│       └── scheduler.Dockerfile
│
├── monitoring/                        # Observability
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── alerts/
│   │       ├── api_alerts.yml
│   │       └── pipeline_alerts.yml
│   ├── grafana/
│   │   └── dashboards/
│   │       ├── api_dashboard.json
│   │       ├── rag_metrics.json
│   │       └── data_quality.json
│   └── logging/
│       └── fluentd.conf
│
├── evaluation/                        # RAG evaluation & testing
│   ├── __init__.py
│   ├── datasets/
│   │   ├── test_queries.json          # Test question-answer pairs
│   │   ├── golden_retrieval.json      # Expected retrieval results
│   │   └── edge_cases.json
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── retrieval_metrics.py       # MRR, NDCG, Recall@k
│   │   ├── generation_metrics.py      # RAGAS, faithfulness
│   │   └── legal_metrics.py           # Domain-specific metrics
│   ├── benchmarks/
│   │   ├── __init__.py
│   │   ├── run_benchmark.py
│   │   └── results/
│   └── ab_testing/
│       ├── __init__.py
│       └── experiment_tracker.py
│
├── tests/                             # Test suite
│   ├── __init__.py
│   ├── conftest.py                    # Pytest fixtures
│   ├── unit/
│   │   ├── test_chunking.py
│   │   ├── test_embeddings.py
│   │   ├── test_retrieval.py
│   │   └── test_generation.py
│   ├── integration/
│   │   ├── test_api.py
│   │   ├── test_pipeline.py
│   │   └── test_vectorstore.py
│   └── e2e/
│       └── test_rag_flow.py
│
├── scripts/                           # Utility scripts
│   ├── setup_dev.sh
│   ├── seed_data.py
│   ├── migrate_vectorstore.py
│   ├── export_metrics.py
│   └── cleanup_old_data.py
│
├── notebooks/                         # Jupyter notebooks (exploration)
│   ├── 01_data_exploration.ipynb
│   ├── 02_chunking_experiments.ipynb
│   ├── 03_embedding_comparison.ipynb
│   ├── 04_retrieval_tuning.ipynb
│   └── 05_prompt_engineering.ipynb
│
└── .github/                           # GitHub specific
    ├── workflows/
    │   ├── ci.yml                     # Lint, test, build
    │   ├── cd.yml                     # Deploy to environments
    │   ├── security.yml               # Dependency scanning
    │   └── docs.yml                   # Documentation build
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    ├── PULL_REQUEST_TEMPLATE.md
    └── dependabot.yml
```

---

## Key Design Decisions

### 1. **Separation of Concerns**
- Each layer (collection → processing → retrieval → generation → API) is isolated
- Easy to swap implementations (e.g., change vector DB without touching retrieval logic)

### 2. **Configuration as Code**
- Pydantic settings for type-safe configuration
- Environment-specific configs via Terraform workspaces
- Secrets managed separately (never committed)

### 3. **Abstract Base Classes**
- `base_scraper.py`, `base_retriever.py`, `base_store.py` etc.
- Enables adding new implementations without modifying existing code
- Follows Open/Closed principle

### 4. **Domain-Specific Components**
- `legal_chunker.py` - Understands sections, articles, schedules
- `citation_extractor.py` - Parses case citations (AIR, SCC format)
- `legal_query_parser.py` - Handles legal terminology

### 5. **Observability Built-In**
- Structured logging throughout
- Prometheus metrics for API and pipeline
- Grafana dashboards for visualization
- Alerts for data quality and system health

### 6. **Production-Ready Infrastructure**
- Multi-environment Terraform (dev/staging/prod)
- Kubernetes manifests with HPA
- Docker multi-stage builds
- GitHub Actions for CI/CD

### 7. **Evaluation Framework**
- Standard RAG metrics (MRR, NDCG, RAGAS)
- Golden datasets for regression testing
- A/B testing infrastructure

---

## Getting Started Commands (for README.md)

```bash
# Clone and setup
git clone https://github.com/yourusername/indian-laws-rag.git
cd indian-laws-rag
make setup

# Run locally
make dev

# Run tests
make test

# Deploy to staging
make deploy-staging
```

---

## Technologies to Showcase

| Layer | Options |
|-------|---------|
| **Data Collection** | Scrapy, BeautifulSoup, Selenium |
| **Orchestration** | Airflow, Prefect, Dagster |
| **Vector DB** | Pinecone, Weaviate, Qdrant, pgvector |
| **Graph DB** | Neo4j, Amazon Neptune |
| **LLM** | OpenAI, Anthropic, AWS Bedrock |
| **API** | FastAPI, async Python |
| **Cloud** | AWS (EKS, S3, RDS, ElastiCache) |
| **IaC** | Terraform, Kubernetes |
| **Monitoring** | Prometheus, Grafana, CloudWatch |
| **CI/CD** | GitHub Actions |

---

## What Makes This Portfolio-Worthy

1. **Clean Architecture** - Shows you understand software design principles
2. **Domain Expertise** - Legal-specific components demonstrate depth
3. **Production Patterns** - Monitoring, testing, IaC show real-world readiness
4. **Extensibility** - Abstract interfaces show OOP mastery
5. **Documentation** - ADRs, runbooks show communication skills
6. **DevOps Skills** - Full CI/CD pipeline, Kubernetes, Terraform