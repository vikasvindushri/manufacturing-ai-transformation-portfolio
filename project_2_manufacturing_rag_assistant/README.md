# Project 2 — Manufacturing Knowledge Assistant (RAG)

## Business problem

Manufacturing and engineering knowledge is often distributed across troubleshooting guides, quality reports, service procedures and lessons learned. Engineers lose time searching for the right information.

## AI opportunity

Use retrieval-augmented generation (RAG) to retrieve the most relevant source passages before producing an answer.

## Demonstrated architecture

User question
→ document chunking
→ TF-IDF semantic-style retrieval
→ top evidence
→ answer grounded in evidence
→ source references

A production system can replace the local retrieval/generation layer with an enterprise-approved vector database and Gemini/other approved model.

## Why RAG?

RAG is preferred over asking a model to rely only on its internal knowledge when answers need to be grounded in company-specific information.
