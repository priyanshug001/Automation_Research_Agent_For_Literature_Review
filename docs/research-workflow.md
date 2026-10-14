# Research workflow

1. Create a project with a topic and optional research question.
2. Search Crossref, OpenAlex, and arXiv; the API returns a status per source and retains successful results when another provider fails.
3. Review the candidates. Relevance is a lexical ranking hint only; it is not evidence verification.
4. Mark records INCLUDED or EXCLUDED. Human screening is required before synthesis.
5. Generate a literature review only with included papers and an available LLM key. The prompt is grounded in stored records and abstracts and instructs the model to disclose missing full text.
6. Run the heuristic title-reference audit and export DOCX or PDF.
7. Manually validate claim support, citation formatting, source access, and novelty before academic submission.
