from backend.planner_agent import run_research_pipeline


topic = "machine learning healthcare"

result = run_research_pipeline(topic)


print("\nFINAL OUTPUT\n")

print(result["review"])

print("\nContradictions:\n")

for c in result["contradictions"]:
    print("-", c)