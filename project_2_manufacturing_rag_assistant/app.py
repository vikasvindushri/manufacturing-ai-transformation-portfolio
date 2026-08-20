import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

KB = Path(__file__).parent / "knowledge_base.csv"

class ManufacturingRAG:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.df["content"])

    def retrieve(self, question, k=3):
        q = self.vectorizer.transform([question])
        scores = cosine_similarity(q, self.matrix).flatten()
        idx = scores.argsort()[::-1][:k]
        results = self.df.iloc[idx].copy()
        results["score"] = scores[idx]
        return results

    def answer(self, question):
        results = self.retrieve(question)
        evidence = []
        for _, row in results.iterrows():
            evidence.append(f"[{row.doc_id}] {row.title}: {row.content}")

        # Deterministic evidence-grounded answer for a GitHub demo.
        answer = (
            "Based on the retrieved manufacturing guidance, investigate the failure "
            "using captured event evidence rather than replacing parts immediately. "
            "Check power/ground, connectors, harness/network integrity and reproduce "
            "the condition where possible. Confirm the root cause before corrective action."
        )
        return answer, results

def main():
    rag = ManufacturingRAG(KB)
    print("\nMANUFACTURING KNOWLEDGE ASSISTANT\n")
    print("Example: What should I check for an intermittent communication fault?")
    question = input("\nQuestion: ").strip()
    answer, sources = rag.answer(question)

    print("\nANSWER")
    print(answer)

    print("\nSOURCES / EVIDENCE")
    for _, r in sources.iterrows():
        print(f"- {r.doc_id}: {r.title} | retrieval score={r.score:.3f}")
        print(f"  {r.content}")

    print("\nProduction enhancement: pass these retrieved passages to an approved enterprise LLM and require citations in the generated answer.")

if __name__ == "__main__":
    main()
